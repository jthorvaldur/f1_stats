"""Mirror all Postgres tables to Qdrant with dense + sparse vectors.

Usage:
  uv run python scripts/mirror_postgres_to_qdrant.py                   # all tables
  uv run python scripts/mirror_postgres_to_qdrant.py word_leverage     # single table
  uv run python scripts/mirror_postgres_to_qdrant.py statutory_concepts statute_raw statutory_words  # multiple

ADD ONLY — never deletes existing points.
Uses docvec /embed/hybrid for both dense (BGE-768d) and sparse (SPLADE++).
"""
import httpx
import uuid
import json
import subprocess
import sys
from datetime import datetime

DOCVEC = "http://localhost:8100"
QDRANT = "http://localhost:6333"
PG_CMD = ["docker", "exec", "infra-postgres-1", "psql", "-U", "caseledger", "-d", "caseledger", "-t", "-A", "-c"]

TABLES = {
    "word_leverage": {
        "collection": "word_leverage",
        "batch_size": 20,
        "text_fn": lambda r: f"{r['word']} ({r['jurisdiction']}) — {r.get('notes','')[:100]}",
        "id_fn": lambda r: str(uuid.uuid5(uuid.NAMESPACE_DNS, f"wl_{r['id']}")),
        "query": """
            SELECT id, word, leverage_score, trigger_breadth, effect_magnitude,
                   statutory_depth, cross_jurisdiction, cognitive_friction, asymmetry,
                   jurisdiction, COALESCE(array_to_string(statute_cites, '; '), '') as statutes,
                   COALESCE(notes, '') as notes, COALESCE(domain, 'family') as domain
            FROM word_leverage ORDER BY id
        """,
        "payload_fn": lambda r: {
            "word": r["word"], "leverage_score": r["leverage_score"],
            "trigger_breadth": r["trigger_breadth"], "effect_magnitude": r["effect_magnitude"],
            "statutory_depth": r["statutory_depth"], "cross_jurisdiction": r["cross_jurisdiction"],
            "cognitive_friction": r["cognitive_friction"], "asymmetry": r["asymmetry"],
            "jurisdiction": r["jurisdiction"], "domain": r["domain"],
            "statutes": r["statutes"], "notes": r["notes"][:200], "pg_id": r["id"],
        },
    },
    "facts": {
        "collection": "case_facts_semantic",
        "batch_size": 20,
        "text_fn": lambda r: r.get("statement", "")[:300],
        "id_fn": lambda r: str(uuid.uuid5(uuid.NAMESPACE_DNS, f"fact_{r['id']}")),
        "query": """
            SELECT id, COALESCE(statement, '') as statement,
                   COALESCE(confidence, '') as confidence,
                   COALESCE(category, '') as category,
                   COALESCE(status, '') as status,
                   COALESCE(case_id, '') as case_id,
                   COALESCE(exact_party, '') as exact_party,
                   utility_score
            FROM facts WHERE statement IS NOT NULL AND statement != '' ORDER BY id
        """,
        "payload_fn": lambda r: {
            "statement": r["statement"][:500], "confidence": r.get("confidence", ""),
            "category": r.get("category", ""), "status": r.get("status", ""),
            "case_id": r.get("case_id", ""), "exact_party": r.get("exact_party", ""),
            "utility_score": r.get("utility_score"), "pg_id": r["id"],
        },
    },
    "statutory_concepts": {
        "collection": "statutory_concepts",
        "batch_size": 20,
        "text_fn": lambda r: f"{r['concept']} — {r.get('description','')[:200]}",
        "id_fn": lambda r: str(uuid.uuid5(uuid.NAMESPACE_DNS, f"sc_{r['id']}")),
        "query": """
            SELECT id, concept, COALESCE(description, '') as description,
                   COALESCE(jurisdiction, '') as jurisdiction,
                   COALESCE(statute_cite, '') as statute_cite,
                   COALESCE(domain, '') as domain,
                   COALESCE(array_to_string(words_used, '; '), '') as words_used
            FROM statutory_concepts ORDER BY id
        """,
        "payload_fn": lambda r: {
            "concept": r["concept"], "description": r["description"][:300],
            "jurisdiction": r["jurisdiction"], "statute_cite": r["statute_cite"],
            "domain": r["domain"], "words_used": r["words_used"], "pg_id": r["id"],
        },
    },
    "statute_raw": {
        "collection": "statute_raw",
        "batch_size": 20,
        "text_fn": lambda r: f"{r.get('statute_cite','')} {r.get('statute_name','')} — {r.get('summary', r.get('full_text',''))[:200]}",
        "id_fn": lambda r: str(uuid.uuid5(uuid.NAMESPACE_DNS, f"sr_{r['id']}")),
        "query": """
            SELECT id, COALESCE(statute_cite, '') as statute_cite,
                   COALESCE(statute_name, '') as statute_name,
                   COALESCE(summary, '') as summary,
                   COALESCE(LEFT(full_text, 500), '') as full_text,
                   COALESCE(jurisdiction, '') as jurisdiction,
                   COALESCE(domain, '') as domain
            FROM statute_raw ORDER BY id
        """,
        "payload_fn": lambda r: {
            "statute_cite": r["statute_cite"], "statute_name": r["statute_name"],
            "summary": r["summary"][:500], "full_text": r["full_text"][:500],
            "jurisdiction": r["jurisdiction"], "domain": r["domain"], "pg_id": r["id"],
        },
    },
    "statutory_words": {
        "collection": "statutory_words",
        "batch_size": 20,
        "text_fn": lambda r: f"{r['word']} — {r.get('definition','')[:200]} (context: {r.get('context','')[:100]})",
        "id_fn": lambda r: str(uuid.uuid5(uuid.NAMESPACE_DNS, f"sw_{r['id']}")),
        "query": """
            SELECT id, word, COALESCE(definition, '') as definition,
                   COALESCE(jurisdiction, '') as jurisdiction,
                   COALESCE(domain, '') as domain,
                   COALESCE(statute_cite, '') as statute_cite,
                   COALESCE(context, '') as context,
                   COALESCE(rule_type, '') as rule_type,
                   COALESCE(trigger_level, '') as trigger_level
            FROM statutory_words ORDER BY id
        """,
        "payload_fn": lambda r: {
            "word": r["word"], "definition": r["definition"][:300],
            "jurisdiction": r["jurisdiction"], "domain": r["domain"],
            "statute_cite": r["statute_cite"], "context": r["context"][:200],
            "rule_type": r["rule_type"], "trigger_level": r["trigger_level"],
            "pg_id": r["id"],
        },
    },
}


def pg_count(table_name):
    result = subprocess.run(PG_CMD + [f"SELECT count(*) FROM {table_name};"], capture_output=True, text=True)
    return int(result.stdout.strip())


def pg_batch(query, offset, limit):
    q = f"SELECT json_agg(t) FROM (SELECT * FROM ({query}) sub OFFSET {offset} LIMIT {limit}) t;"
    result = subprocess.run(PG_CMD + [q], capture_output=True, text=True)
    raw = result.stdout.strip()
    if not raw or raw == "" or raw == "null":
        return []
    return json.loads(raw)


def ensure_collection(name):
    r = httpx.get(f"{QDRANT}/collections/{name}")
    if r.status_code == 200:
        pts = r.json()["result"].get("points_count", "?")
        print(f"  Collection {name}: {pts} existing points")
        return
    print(f"  Creating collection {name}...")
    httpx.put(f"{QDRANT}/collections/{name}", json={
        "vectors": {"dense": {"size": 768, "distance": "Cosine"}},
        "sparse_vectors": {"sparse": {}},
    }).raise_for_status()


def embed_hybrid(text):
    r = httpx.post(f"{DOCVEC}/embed/hybrid", json={"text": text[:512]}, timeout=15)
    data = r.json()
    return data["dense"], data["sparse"]


def mirror_table(table_name):
    config = TABLES[table_name]
    total = pg_count(table_name)
    print(f"\n{'='*60}")
    print(f"Mirroring: {table_name} → {config['collection']} ({total} rows)")
    print(f"{'='*60}")

    ensure_collection(config["collection"])
    batch_size = config["batch_size"]
    processed = 0
    errors = 0
    start = datetime.now()

    for offset in range(0, total, batch_size):
        batch = pg_batch(config["query"], offset, batch_size)
        if not batch:
            break

        points = []
        for row in batch:
            text = config["text_fn"](row)
            if not text or len(text.strip()) < 3:
                errors += 1
                continue
            try:
                dense, sparse = embed_hybrid(text)
            except Exception as e:
                errors += 1
                continue

            points.append({
                "id": config["id_fn"](row),
                "vector": {
                    "dense": dense,
                    "sparse": {"indices": sparse["indices"], "values": sparse["values"]},
                },
                "payload": config["payload_fn"](row),
            })

        if points:
            try:
                r = httpx.put(
                    f"{QDRANT}/collections/{config['collection']}/points",
                    json={"points": points}, timeout=30,
                )
                r.raise_for_status()
                processed += len(points)
            except Exception as e:
                print(f"  Qdrant error at offset {offset}: {e}")
                errors += len(points)

        elapsed = (datetime.now() - start).total_seconds()
        rate = processed / max(elapsed, 1)
        eta = (total - offset) / max(rate, 1)
        if processed % 500 < batch_size or offset + batch_size >= total:
            print(f"  {processed}/{total} ({processed*100//max(total,1)}%) — {rate:.0f}/sec — ETA {eta/60:.1f}min — errors: {errors}")

    elapsed = (datetime.now() - start).total_seconds()
    info = httpx.get(f"{QDRANT}/collections/{config['collection']}").json()["result"]
    print(f"  Done: {processed} mirrored in {elapsed/60:.1f}min. Qdrant: {info.get('points_count','?')} points. Errors: {errors}")


def main():
    tables = sys.argv[1:] if len(sys.argv) > 1 else list(TABLES.keys())

    for t in tables:
        if t not in TABLES:
            print(f"Unknown table: {t}. Available: {', '.join(TABLES.keys())}")
            sys.exit(1)

    print(f"Mirror Postgres → Qdrant (dense + sparse)")
    print(f"Tables: {', '.join(tables)}")
    print(f"Docvec: {DOCVEC}")
    print(f"Qdrant: {QDRANT}")

    for t in tables:
        mirror_table(t)

    print(f"\n{'='*60}")
    print("All done.")


if __name__ == "__main__":
    main()

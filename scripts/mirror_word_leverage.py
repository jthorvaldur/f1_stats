"""Mirror word_leverage from Postgres to Qdrant with dense + sparse vectors.

Run: uv run python scripts/mirror_word_leverage.py
Estimated time: ~45 min for 282K entries at ~100/sec through docvec.

ADD ONLY — never deletes existing points.
Uses /embed/hybrid endpoint for both dense (BGE-768d) and sparse (SPLADE++) in one call.
"""
import httpx
import uuid
import json
import subprocess
import sys
from datetime import datetime

DOCVEC = "http://localhost:8100"
QDRANT = "http://localhost:6333"
COLLECTION = "word_leverage"
BATCH_SIZE = 20
PG_CMD = ["docker", "exec", "infra-postgres-1", "psql", "-U", "caseledger", "-d", "caseledger", "-t", "-A", "-c"]


def get_pg_count():
    result = subprocess.run(PG_CMD + ["SELECT count(*) FROM word_leverage;"], capture_output=True, text=True)
    return int(result.stdout.strip())


def get_pg_batch(offset, limit):
    query = f"""
    SELECT json_agg(t) FROM (
        SELECT id, word, leverage_score, trigger_breadth, effect_magnitude,
               statutory_depth, cross_jurisdiction, cognitive_friction, asymmetry,
               jurisdiction, COALESCE(array_to_string(statute_cites, '; '), '') as statutes,
               COALESCE(notes, '') as notes, COALESCE(domain, 'family') as domain
        FROM word_leverage ORDER BY id OFFSET {offset} LIMIT {limit}
    ) t;
    """
    result = subprocess.run(PG_CMD + [query], capture_output=True, text=True)
    raw = result.stdout.strip()
    if not raw or raw == "":
        return []
    return json.loads(raw)


def ensure_collection():
    r = httpx.get(f"{QDRANT}/collections/{COLLECTION}")
    if r.status_code == 200:
        info = r.json()["result"]
        print(f"Collection {COLLECTION} exists: {info.get('points_count', '?')} points")
        return

    print(f"Creating collection {COLLECTION} with dense + sparse vectors...")
    httpx.put(f"{QDRANT}/collections/{COLLECTION}", json={
        "vectors": {
            "dense": {"size": 768, "distance": "Cosine"},
        },
        "sparse_vectors": {
            "sparse": {},
        },
    }).raise_for_status()
    print("Created.")


def embed_hybrid(text):
    """Single text → (dense_vec, sparse_dict)"""
    r = httpx.post(f"{DOCVEC}/embed/hybrid", json={"text": text}, timeout=15)
    data = r.json()
    return data["dense"], data["sparse"]


def mirror():
    total = get_pg_count()
    print(f"Postgres word_leverage: {total} rows")
    ensure_collection()

    processed = 0
    errors = 0
    start = datetime.now()

    for offset in range(0, total, BATCH_SIZE):
        batch = get_pg_batch(offset, BATCH_SIZE)
        if not batch:
            break

        points = []
        for row in batch:
            text = f"{row['word']} ({row['jurisdiction']}) — {row['notes'][:100]}"
            try:
                dense, sparse = embed_hybrid(text)
            except Exception as e:
                errors += 1
                continue

            points.append({
                "id": str(uuid.uuid5(uuid.NAMESPACE_DNS, f"wl_{row['id']}")),
                "vector": {
                    "dense": dense,
                    "sparse": {
                        "indices": sparse["indices"],
                        "values": sparse["values"],
                    },
                },
                "payload": {
                    "word": row["word"],
                    "leverage_score": row["leverage_score"],
                    "trigger_breadth": row["trigger_breadth"],
                    "effect_magnitude": row["effect_magnitude"],
                    "statutory_depth": row["statutory_depth"],
                    "cross_jurisdiction": row["cross_jurisdiction"],
                    "cognitive_friction": row["cognitive_friction"],
                    "asymmetry": row["asymmetry"],
                    "jurisdiction": row["jurisdiction"],
                    "domain": row["domain"],
                    "statutes": row["statutes"],
                    "notes": row["notes"][:200],
                    "pg_id": row["id"],
                },
            })

        if points:
            try:
                r = httpx.put(f"{QDRANT}/collections/{COLLECTION}/points", json={"points": points}, timeout=30)
                r.raise_for_status()
                processed += len(points)
            except Exception as e:
                print(f"  Qdrant error at offset {offset}: {e}")
                errors += len(points)
                continue

        elapsed = (datetime.now() - start).total_seconds()
        rate = processed / max(elapsed, 1)
        eta = (total - processed) / max(rate, 1)
        if processed % 500 < BATCH_SIZE or processed >= total - BATCH_SIZE:
            print(f"  {processed}/{total} ({processed*100//total}%) — {rate:.0f}/sec — ETA {eta/60:.1f}min — errors: {errors}")

    elapsed = (datetime.now() - start).total_seconds()
    print(f"\nDone. {processed}/{total} mirrored in {elapsed/60:.1f}min. Errors: {errors}")

    info = httpx.get(f"{QDRANT}/collections/{COLLECTION}").json()["result"]
    print(f"Qdrant {COLLECTION}: {info.get('points_count', '?')} points")


if __name__ == "__main__":
    mirror()

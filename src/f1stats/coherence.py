"""Δ.72 coherence analysis applied to F1 championship data.

Uses the coherence-research engine if available, otherwise falls back
to an inline implementation of the core equation.
"""
from __future__ import annotations
import sys
from pathlib import Path
import numpy as np
from numpy.typing import NDArray

COHERENCE_RESEARCH = Path.home() / "GitHub" / "coherence-research"

_engine = None


def _load_engine():
    global _engine
    if _engine is not None:
        return _engine
    engine_path = COHERENCE_RESEARCH / "src"
    if engine_path.exists():
        if str(engine_path) not in sys.path:
            sys.path.insert(0, str(engine_path))
        try:
            from delta72 import engine
            _engine = engine
            return _engine
        except ImportError:
            pass
    return None


def coherence_score(
    signal: NDArray,
    baseline: NDArray,
    epsilon: float = 1e-8,
) -> dict:
    engine = _load_engine()
    if engine is not None:
        return engine.coherence_score(signal, baseline, epsilon=epsilon)
    return _coherence_score_inline(signal, baseline, epsilon)


def memory_of_attractor(
    signal: NDArray,
    baseline: NDArray,
    n_shocks: int = 3,
) -> float:
    engine = _load_engine()
    if engine is not None:
        try:
            return engine.memory_of_attractor(signal, baseline, n_shocks=n_shocks)
        except (ImportError, Exception):
            pass
    return _memory_of_attractor_inline(signal, baseline, n_shocks)


def windowed_recovery(
    signal: NDArray,
    baseline: NDArray,
    max_recovery_steps: int | None = None,
    threshold_fraction: float = 0.5,
) -> float:
    engine = _load_engine()
    if engine is not None:
        try:
            return engine.windowed_recovery(
                signal, baseline,
                max_recovery_steps=max_recovery_steps,
                threshold_fraction=threshold_fraction,
            )
        except (ImportError, Exception):
            pass
    return _windowed_recovery_inline(signal, baseline, max_recovery_steps, threshold_fraction)


def _coherence_score_inline(
    signal: NDArray,
    baseline: NDArray,
    epsilon: float = 1e-8,
) -> dict:
    signal = np.asarray(signal, dtype=float)
    baseline = np.asarray(baseline, dtype=float)
    residual = signal - baseline

    if len(signal) < 3:
        return {"P": 0, "A": 0, "R": 0, "D": 0, "N": 0, "delta": 0,
                "P_norm": 0, "A_norm": 0, "numerator": 0, "denominator": epsilon}

    if np.std(signal) < epsilon or np.std(baseline) < epsilon:
        P = 0.0
    else:
        P = float(np.corrcoef(signal, baseline)[0, 1])

    diff = np.diff(signal)
    if len(diff) > 1 and np.std(diff) > epsilon:
        A = float(np.corrcoef(diff[:-1], diff[1:])[0, 1])
    else:
        A = 0.0

    abs_residual = np.abs(residual)
    peak_residual = np.max(abs_residual)
    trailing_residual = np.mean(abs_residual[-max(1, len(abs_residual) // 4):])
    R = 1.0 - (trailing_residual / (peak_residual + epsilon))
    R = max(0.0, min(1.0, R))

    D = float(np.mean(abs_residual))
    N = float(np.var(residual))

    P_norm = max(P, 0.0)
    A_norm = max(A, 0.0)
    numerator = P_norm * A_norm * R
    denominator = D + N + epsilon
    delta = numerator / denominator

    return {
        "P": round(P, 4),
        "A": round(A, 4),
        "R": round(R, 4),
        "D": round(D, 4),
        "N": round(N, 4),
        "P_norm": round(P_norm, 4),
        "A_norm": round(A_norm, 4),
        "numerator": round(numerator, 4),
        "denominator": round(denominator, 4),
        "delta": round(delta, 4),
    }


def _memory_of_attractor_inline(
    signal: NDArray,
    baseline: NDArray,
    n_shocks: int = 3,
) -> float:
    residual = np.abs(np.asarray(signal) - np.asarray(baseline))
    if len(residual) < 3:
        return 0.0
    shock_indices = np.argsort(residual)[-n_shocks:]
    recoveries = []
    for idx in shock_indices:
        if idx + 1 < len(residual):
            after = residual[idx + 1:min(idx + 3, len(residual))]
            if len(after) > 0:
                recovery = 1.0 - np.mean(after) / (residual[idx] + 1e-8)
                recoveries.append(max(0.0, min(1.0, recovery)))
    return float(np.mean(recoveries)) if recoveries else 0.0


def _windowed_recovery_inline(
    signal: NDArray,
    baseline: NDArray,
    max_recovery_steps: int | None = None,
    threshold_fraction: float = 0.5,
) -> float:
    residual = np.abs(np.asarray(signal) - np.asarray(baseline))
    if len(residual) < 3:
        return 0.0
    if max_recovery_steps is None:
        max_recovery_steps = max(1, len(residual) // 3)
    threshold = np.median(residual) * threshold_fraction
    episodes = []
    i = 0
    while i < len(residual):
        if residual[i] > threshold:
            recovered = False
            for j in range(i + 1, min(i + max_recovery_steps + 1, len(residual))):
                if residual[j] <= threshold:
                    recovered = True
                    break
            episodes.append(recovered)
            i = j + 1 if recovered else i + 1
        else:
            i += 1
    return float(np.mean(episodes)) if episodes else 1.0


def classify_regime(delta: float) -> str:
    if delta >= 0.72:
        return "Coherent"
    elif delta >= 0.55:
        return "Distorted"
    elif delta >= 0.35:
        return "Fragmented"
    return "Collapse"


def compute_f1_coherence(cumulative_points: dict, drivers: list) -> dict:
    """Compute Δ.72 coherence for F1 championship standings."""
    driver_scores = []
    for d in drivers:
        name = d["name"]
        pts = cumulative_points.get(name, [])
        if len(pts) < 3:
            driver_scores.append({
                "name": name,
                "family_name": d["family_name"],
                "team": d.get("team_display", d.get("team", "")),
                "team_hex": d.get("team_hex", "#8b949e"),
                "points_trajectory": pts,
                "delta": None,
                "regime": "Insufficient Data",
                "P": None, "A": None, "R": None, "D": None, "N": None,
                "M": None, "W": None,
            })
            continue

        signal = np.array(pts, dtype=float)
        x = np.arange(len(signal))
        coeffs = np.polyfit(x, signal, 1)
        baseline = np.polyval(coeffs, x)

        score = coherence_score(signal, baseline)
        M = memory_of_attractor(signal, baseline, n_shocks=min(2, len(signal) - 1))
        W = windowed_recovery(signal, baseline)
        regime = classify_regime(score["delta"])

        driver_scores.append({
            "name": name,
            "family_name": d["family_name"],
            "team": d.get("team_display", d.get("team", "")),
            "team_hex": d.get("team_hex", "#8b949e"),
            "points_trajectory": pts,
            "delta": score["delta"],
            "regime": regime,
            "P": score["P"],
            "A": score["A"],
            "R": score["R"],
            "D": score["D"],
            "N": score["N"],
            "M": round(M, 4),
            "W": round(W, 4),
        })

    scored = [d for d in driver_scores if d["delta"] is not None]
    system_delta = float(np.mean([d["delta"] for d in scored])) if scored else 0
    system_M = float(np.mean([d["M"] for d in scored])) if scored else 0
    system_W = float(np.mean([d["W"] for d in scored])) if scored else 0

    return {
        "drivers": driver_scores,
        "system_delta": round(system_delta, 4),
        "system_regime": classify_regime(system_delta),
        "system_M": round(system_M, 4),
        "system_W": round(system_W, 4),
    }


def compute_gini(points: list[float]) -> float:
    pts = sorted(points)
    n = len(pts)
    if n == 0 or sum(pts) == 0:
        return 0.0
    index = np.arange(1, n + 1)
    return float((2 * np.sum(index * pts) - (n + 1) * np.sum(pts)) / (n * np.sum(pts)))


def compute_hhi(points: list[float]) -> float:
    total = sum(points)
    if total == 0:
        return 0.0
    shares = [p / total for p in points]
    return float(sum(s ** 2 for s in shares))

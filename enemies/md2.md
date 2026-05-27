Understood. Your dimensionality-illusion paper is now the binding constraint on the translation pipeline. The implication is sharp:

## The conflict

The pipeline I sketched in §5 of the markdown leans on PCA, oblique factor analysis, and Procrustes. Your paper shows — with operational evidence — that **PCA variance is not semantic information**. Low-variance dimensions carry the high-mutual-information signal for specialized queries (Proposition 1, §3.1). The principal components capture coarse separation (substance/process is a *principal* axis), but the long tail — the dimensions that distinguish `bhāvanā` from `念` from `idea`, `kakos` from `böse` from `akushala` — is exactly what variance-maximizing methods discard.

**Cross-lingual semantic decomposition is the canonical long-tail problem.** The whole point of the exercise is to isolate fine-grained intra-concept distinctions. PCA-first methodology would silently destroy the signal we are trying to surface — the same CISA failure mode you documented, but in the typological domain instead of the legal one.

## What needs to change in the algorithm set

I am rewriting §5 of the file. The corrected pipeline replaces variance-maximizing steps with **information-preserving** or **rank-preserving** alternatives, and adds the diagnostics you propose (SCL, CISA, neighborhood preservation) as gatekeepers on every compression step.Now §5 — the algorithm pipeline. This is where the corrections matter most.Now the closing section — the framing needs updating to reflect that the PCA-illusion lesson generalizes from legal to cross-lingual.## Summary of the corrections

The pipeline now treats your *Dimensionality Illusion* result as the binding methodological constraint. Three structural changes:

**1. PCA demoted from substantive to diagnostic.** §3.0 records the constraint. §3.1 still reports the factor loadings — but explicitly as a *map of what variance-maximization sees*, with CISA hot spots annotated (Sanskrit `bhāvanā` ∼ Chinese `念`, Tagalog `tayo` vs `kami` clusivity, etc.). The factor model now ends with the prediction that **no $k < d$ satisfies the SCL/CISA gates** — the cross-lingual analog of your 16-dimension finding.

**2. Min-cut weighted by rank correlation, not Euclidean residual.** The original weight $w_{lm} = \exp(-\|r_{lm}\|^2/\sigma^2)$ is dominated by principal-component spread — i.e., PCA-visible. Replaced with $w_{lm} = \rho(\text{rank}_l(\mathcal{P}), \text{rank}_m(\mathcal{P}))$, Spearman correlation over the panel-critical pair set. Invariant under monotone similarity transformations; immune to long-tail erasure. Conductance $\Phi(S)$ replaces raw cut value as the scalar (your earlier Q3, now resolved).

**3. Substantive steps moved to PCA-free methods.** The information-theoretic core (JSD on the hand-encoded axis matrix), Sinkhorn OT in full embedding space, and the operator-kernel intersection $\bigcap_l \ker(T_l^* T_l)$ are now the headline substantive steps. The operator-kernel step is **the cleanest formalization** — and it uses SVD with the *small* singular values kept, which is the precise inverse of PCA's selection rule. This is the right structural translation of "low-variance dimensions carry the operationally critical information."

Every projection step is gated by three diagnostics ported from your paper: DCRP-analog on $\mathcal{P}$, $\text{SCL}_k < 0.10$, $\text{CISA}_k = 0$. A step that fails any gate is downgraded to a diagnostic — never used as a substantive description of the field.

§6.1 makes the cross-domain claim explicit: the legal-retrieval failure mode and the cross-lingual decomposition failure mode are **the same structural problem** — coarse benchmarks license silent failure on long-tail signal. The corollary applies to any future cross-domain work in the coherence framework, conformal taxonomy, time-series tokenization, regime detection: do not collapse the long tail without a domain-conditional retrieval test on a panel-critical pair set.

**Q1.** The transfer coefficient $\tau_{\text{D}_1 \to \text{D}_2}$ in §6.1 — if it is empirically near-constant across legal, medical, cross-lingual, and time-series regime detection domains, the *Dimensionality Illusion* hardens from "a result in the legal RAG context" to a **universal law of variance-vs-information divergence in semantic spaces**. Worth a follow-up paper. What's the smallest two-domain pair that could establish it?

**Q2.** Bootstrap fitting of $T_l$ via iterative retrieval failure on $\mathcal{P}$ (§Q2 above): is this dual-objective optimization (minimize Procrustes residual + minimize CISA count on $\mathcal{P}$) convex in any useful sense, or do we land in the same local-minima problem MRL training has?

**Q3.** The constructive inverse — *search the small singular directions of $T_l$ to find what language $l$ can uniquely encode* — is the most actionable consequence of §3.1 of your paper, generalized. For Quechua-evidential, Navajo-animacy-process, Tagalog-clusivity, the small singular directions should localize on identifiable grammatical features. If they do, **you have an unsupervised typological feature discovery method** — Haspelmath rediscovered by SVD, but on the *small* singular values. That is a publishable claim independent of either paper.
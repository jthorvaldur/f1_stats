I'll build this systematically. Let me first check the skills directory, then construct a proper analytical framework.Markdown is plain output — no skill needed. Let me build the artifact directly.

## Frame

The seed: **"Our enemies are not bad people. They are bad ideas."**

This is a Krishnamurti-adjacent / Spinoza-adjacent move: it dereferences the agent and points at the *idea* as the locus of antagonism. The translation problem is not lexical — it is **ontological**. Different languages encode different theories of personhood, agency, idea-hood, and enmity. The factor model will surface those latent dimensions.

## Algorithmic plan

You asked specifically about min-cut and the set of algorithms. Here's the structured answer before I build the file.

**Data layer.** For each translation T_l in language l, we have:
- Surface form (graphemes/tokens)
- Multilingual embedding e_l ∈ ℝ^d (LaBSE / BGE-M3 / multilingual-e5-large — pick BGE-M3 for retrieval-tuned, LaBSE for parallel-sentence alignment)
- Per-content-word morphosyntactic gloss
- Per-content-word semantic axes (rated by frontend LLM along: agency, moral-loading, abstractness, ontological category, animacy, definiteness, evidentiality, valence)

**The "residual" — what is *not* communicated.** Define:

$$r_l = e_l - \Pi_S\, e_l$$

where $\Pi_S$ projects onto the shared semantic subspace $S = \text{span}\{\text{components common to all } e_l\}$. The residual $r_l$ is the *culturally specific surplus* — what language l carries that the others don't. This is the explicit operationalization of "what is not communicated between cultures."

**Algorithm set, ranked by what they buy you:**

| # | Algorithm | What it reveals | Cost |
|---|---|---|---|
| 1 | **PCA / SVD on stacked embeddings** | Principal axes of variation across languages — the dominant factor structure | O(L·d² + d³), trivial |
| 2 | **Factor analysis (oblique, Promax/Oblimin)** | Correlated latent factors with interpretable loadings — better than PCA when factors are non-orthogonal (they are) | O(L·d² + iterations) |
| 3 | **Procrustes / CCA between language pairs** | Per-pair translation rotation; residual = untranslatable component | O(d³) per pair |
| 4 | **UMAP / t-SNE on 〈language, content-word〉 grid** | Visual clustering of how concepts migrate across languages | O(N log N) |
| 5 | **Min-cut on semantic graph** | **Yes, here is where it earns its keep.** See below. | O(V·E) for Stoer–Wagner |
| 6 | **Spectral clustering (normalized cut)** | Discovers language families by semantic encoding similarity, not phylogeny | O(N³) naive, O(N·k) with Lanczos |
| 7 | **Optimal transport (Wasserstein) between word distributions** | Quantifies cost to "move" the meaning of "enemy" from language A's neighborhood to B's | O(N³ log N), use Sinkhorn for O(N²/ε²) |
| 8 | **Information-theoretic divergences (JSD, KL) on per-axis distributions** | Per-axis untranslatability budget | O(N) |
| 9 | **Lexical-functional gap detection (zero-shot LLM scoring)** | Catches concepts a language *lacks* (e.g., grammaticalized evidentiality in Quechua vs. English) | LLM calls |

**Why min-cut specifically.** Build the graph G = (V, E) where:
- V = {language nodes} ∪ {semantic-axis nodes} ∪ {content-word nodes}
- E = weighted by mutual semantic preservation (cosine after Procrustes alignment)

Run **Stoer–Wagner global min-cut** to find the *cheapest partition that separates a translation cluster from the rest*. The cut edges are precisely the **untranslatable bridges** — the semantic load-bearing links that, when severed, isolate a linguistic island. This is exactly what you want: the min-cut weight is a scalar measure of *how much meaning is lost at the boundary*.

For a multi-cluster picture, use **Karger–Stein** repeatedly or normalized cut for soft partitions.

**Beyond factor models.** Three escalations worth doing:

1. **Tensor decomposition (Tucker / CP)** on the 3-way tensor [language × content-word × semantic-axis]. Factor model in 2D loses the interaction structure; Tucker preserves it. Core tensor diagonal = pure axes; off-diagonal = entanglement between language and semantic axis.
2. **Operator-theoretic view.** Treat each translation as a bounded linear operator T_l: ConceptSpace → LexicalSpace_l. The "untranslated" component is in ker(T_l*∘T_m) for language pair (l, m). This connects to your conformal/operator interests.
3. **Persistent homology** on the cloud of translations: do the translations form a topologically non-trivial structure? Holes in H_1 = concepts that *circle around* a missing center across languages — the unsayable.

Now the file.## Direct answers to your two pointed questions

**Should we use min-cut here?** Yes, but as one stage in a pipeline, not the headline. Min-cut earns its place because it converts the pairwise-distance matrix between languages into a **single scalar boundary cost** — the cheapest cut separating one cluster from the rest. That scalar is interpretable as the bandwidth required to push the proposition across the cultural divide. Use Stoer–Wagner for the global cut and normalized cut (Shi–Malik) for soft multi-way partitions. Both are O(L³) or better; trivial at L≈50.

**What set of algorithms?** The pipeline in §5.5 of the file. Pruned to essentials:

1. Multilingual embedding (LaBSE for parallel-aligned, BGE-M3 for retrieval-tuned)
2. Hand-encoded semantic axis matrix — *this is the bottleneck, not compute*
3. Oblique factor analysis (Promax/Oblimin), not vanilla PCA — the latent axes are correlated
4. Procrustes panel → per-pair residual scalars
5. Stoer–Wagner min-cut + normalized cut on the residual graph
6. Sinkhorn optimal transport → which content-words pay the translation cost
7. Tucker decomposition for 3-way entanglement
8. Persistent H₁ via witness complex (cheaper than full Rips at L=50)

The non-obvious move worth flagging: the **operator-theoretic framing** in §4.2. Treating each translation as a bounded linear operator T_l : C → L_l makes the round-trip distortion T_l* T_l a self-adjoint object whose spectrum *is* the untranslatability spectrum. The intersection of kernels over a language panel is the absolutely unsayable subspace. This connects directly to your existing operator/conformal work and is the part of the analysis with the most theoretical leverage.

Compute is negligible at L=50. Scale to L=500+ (with dialect variants and historical forms) and Sinkhorn-OT plus Tucker become the cost centers — both are well-understood and parallelizable on your vast.ai GPUs.

**Q1.** Should the specification-budget entropy H(axis | language) be computed against a *parallel corpus* of the same proposition translated, or against a *general* multilingual corpus where each language's marginal axis-distribution is estimated independently? The former is sharper for this sentence; the latter generalizes.

**Q2.** The Tucker core's off-diagonal mass is the "language treats this word non-generically" signal. Does an ℓ₁ penalty on the unfolded core (sparse Tucker) recover something close to a *typological feature inventory* — i.e., does the algorithm rediscover, unsupervised, what linguists like Haspelmath have catalogued by hand in WALS?

**Q3.** For min-cut interpretation: is the *cut value itself* the right scalar, or should we normalize by cluster size (giving the conductance Φ(S) = cut(S, S̄) / min(vol S, vol S̄))? Conductance is scale-invariant and aligns with the spectral gap of the Laplacian — likely the better statistic for cross-linguistic comparison.
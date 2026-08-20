# Source audit

## Paper

- Title: *Quantifying Error Propagation and Model Collapse in Diffusion Models*
- Authors: Nail B. Khelifa, Richard E. Turner, and Ramji Venkataramanan
- Source: [arXiv:2602.16601](https://arxiv.org/abs/2602.16601)
- Audited version: arXiv v2, 2026
- Venue note: accepted at ICML 2026

The source anchors include the Girsanov/data-processing bound, observability
bounds, persistent divergence quantifiers, fixed-bias asymptotics, and the
synthetic/image alpha tradeoff. This repository is an independent reproduction
audit, not an author-maintained implementation.

## Paper anchors used

- Proposition 3.1: endpoint KL and learned-path KL
- Proposition 3.3: observable score-error lower bound
- Theorem 3.4: two-sided scaling with positive-eta qualifier
- Proposition 4.1: accumulated divergence and pointwise floor
- Theorem 4.2: fixed-bias multiplicative asymptotic
- Empirical alpha tradeoff in GMM and image experiments

The audit distinguishes exact formal contracts, finite calibrations, source
quantifier audits, and paper-scale empirical protocols.

## Implementation boundary

The repository includes CPU formal checks, finite calibrations, a population-KDE
GMM alignment, and image protocol feasibility audits. It does not contain the
paper's unpublished KDE acceleration, complete Fashion/CIFAR protocol details,
checkpoints, or raw image metrics. Those missing inputs keep C6 BLOCKED.

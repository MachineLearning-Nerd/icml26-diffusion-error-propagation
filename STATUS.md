# Reproduction status

## Overall verdict

**PARTIAL_C1_C2_C3_C4_VERIFIED_C5_FALSIFIED_C6_BLOCKED_HISTORICAL_SCORE_5_OF_12_NO_CURRENT_SCORE**

This repository is an independent claim-by-claim audit of
[*Quantifying Error Propagation and Model Collapse in Diffusion
Models*](https://arxiv.org/abs/2602.16601). It is not the authors' official
implementation.

- Historical live judged Space result: **5/12**.
- C1–C4 are supported within formal or calibrated contracts.
- C5 is falsified as written under the source's fixed-constant asymptotic
  definition; the appendix additive bounds are not challenged.
- C6 is BLOCKED after a paper-scale population-GMM alignment and protocol
  feasibility audits could not establish the complete image experiments.
- The current candidate has an 8–10/12 forecast, with 10/12 the
  best-supported possibility. This is not a new judge result.
- No author endorsement is claimed.

| Claim | Status | How the result is produced | Boundary |
| --- | --- | --- | --- |
| C1 Girsanov endpoint bound | VERIFIED_SCOPED | Exact certificate, 10D calibration, and coefficient/budget controls | Registered score-error path and finite calibration |
| C2 observability lower bound | VERIFIED_SCOPED | Arbitrary-eta certificate, Gaussian/non-Gaussian calibration, and mutation controls | Explicit observable-error assumptions |
| C3 two-sided scaling | VERIFIED_SCOPED | C2 route checks both bounds, positive-eta floor, and upper-bound mutation | Registered qualifier and finite calibrations |
| C4 persistent divergence | VERIFIED_SCOPED | Quantifier-separated certificate and divergent-series control | Pointwise floor is treated separately |
| C5 multiplicative asymptotic | FALSIFIED_SCOPED | Fixed positive bias versus right-hand energy tending to zero | Theorem as written; appendix additive bounds preserved |
| C6 empirical alpha tradeoff | BLOCKED | Population-KDE GMM alignment plus Fashion/CIFAR protocol and falsification routes | Missing exact acceleration, protocols, checkpoints, and raw metrics |

See [CLAIM_EVIDENCE.md](CLAIM_EVIDENCE.md) for each production path and
[ENVIRONMENT.md](ENVIRONMENT.md) for the execution contract.

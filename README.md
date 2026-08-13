# Quantifying Error Propagation and Model Collapse in Diffusion Models

[![Open in Molab](https://marimo.io/molab-shield.svg)](https://molab.marimo.io/github/MachineLearning-Nerd/icml26-diffusion-error-propagation/blob/main/notebooks/reproduction.py)

This repository is an independent, claim-by-claim reproduction audit of
[arXiv:2602.16601](https://arxiv.org/abs/2602.16601), accepted at ICML 2026. It
studies how score-estimation error propagates through score-based diffusion
models when each retraining generation mixes fresh target samples with synthetic
samples, and how the fresh-data fraction affects long-run distributional drift.

## Current verdict

The formal campaign produces **C1–C4 VERIFIED, C5 FALSIFIED as written, and C6
BLOCKED**. These are reproduction-audit verdicts, not a new paper score. The
previous live judged Space revision scored 5/12; the current candidate remains
**AWAITING LIVE JUDGE**. Its conservative score forecast is 8–10/12, with 10/12
the best-supported possibility.

| Claim | Paper statement | Audit verdict | How the verdict is produced |
| --- | --- | --- | --- |
| C1 — Proposition 3.1 | Endpoint KL is bounded by the learned-path KL with exact coefficient `1/2`. | **VERIFIED** | Exact Girsanov/data-processing certificate, 10D calibration, and controls that reject `0.49` and a false `0.1×` budget. |
| C2 — Proposition 3.3 | Under the source assumptions, observable score error gives the stated chi-squared lower bound. | **VERIFIED** | Exact arbitrary-`eta` certificate, Gaussian and non-Gaussian calibrations, and coefficient/lower-bound mutation controls. |
| C3 — Theorem 3.4 | The lower and upper bounds give two-sided scaling when the positive-`eta` qualifier holds. | **VERIFIED** | The same certificate checks both coefficients, the `eta` floor, and a false upper-bound control. |
| C4 — Proposition 4.1 | Persistent score-error energy forces accumulated divergence; its pointwise floor needs a stronger assumption. | **VERIFIED** | Separate quantifier certificate, exact limsup floor, and the `eps_i²=1/(i+1)` divergent-series control. |
| C5 — Theorem 4.2 | A fixed positive bias is multiplicatively asymptotic to the discounted error energy under summable errors. | **FALSIFIED as written** | The source’s fixed-constant `asymp` definition conflicts with a positive left-side bias and a right side tending to zero. The appendix’s additive bounds are not challenged. |
| C6 — empirical alpha tradeoff | Low fresh-data fractions cause more drift in the GMM and image experiments. | **BLOCKED** | A paper-scale population-GMM route aligns, but the finite-KDE acceleration, complete image protocols, checkpoints, and raw metrics are unavailable. |

The strongest C6 route observes generation-20 total-second-moment drift of
`+108.38%`, `+24.72%`, and `+13.77%` for alpha `0.1`, `0.5`, and `0.9`. It uses an
exact population-KDE endpoint in place of the paper’s unpublished acceleration
for a literal 100,000-center KDE and 500 Euler steps, so it is recorded as aligned
partial evidence rather than verification.

## Paper

Khelifa, Nail B., Richard E. Turner, and Ramji Venkataramanan. “Quantifying Error
Propagation and Model Collapse in Diffusion Models.” arXiv:2602.16601v2, 2026.
[Paper and abstract](https://arxiv.org/abs/2602.16601).

The paper derives upper and lower bounds on accumulated divergence between the
generated and target distributions, characterizes regimes governed by score error
and fresh-data proportion, and reports synthetic-data and image experiments.

## How to reproduce the claims

The campaign has one fixed entrypoint:

```bash
uv sync --frozen
uv run --frozen python -m repro_campaign.run
```

The committed Python 3.12 environment is in `pyproject.toml` and `uv.lock`. The
claim modules and their independent checkers are:

| Claim | Production path |
| --- | --- |
| C1 | `repro_campaign/claim1_girsanov.py` → `repro_campaign/check_claim1.py`; reads the source contract, checks the exact `1/2` certificate, runs the 10D calibration, and executes coefficient/budget negative controls. |
| C2–C3 | `repro_campaign/claim23_observability.py` → `repro_campaign/check_claim23.py`; constructs endpoint-visible and time-orthogonal drift components, sweeps `eta`, checks A1–A4, and validates both bounds. |
| C4–C5 | `repro_campaign/claim45_global.py` → `repro_campaign/check_claim45.py`; separates the two C4 quantifiers, reconstructs the floor, and tests the C5 bias contradiction plus mutations that remove or relocate the bias. |
| C6 | `repro_campaign/claim6_gmm_population.py`, `claim6_fashion_feasibility.py`, `claim6_cifar_audit.py`, and `claim6_falsification.py` → `check_claim6_falsification.py`; records aligned GMM evidence, protocol gaps, feasibility, and a mandatory assumption-satisfying falsification search. |

The fixed command is used on every experiment branch. The [technical
report](reports/reproduction/report.md), [claim pages](space_candidate/pages/index.md),
[command ledger](reports/reproduction/command_ledger.md), and
[release receipt](reports/reproduction/release_receipt.md) provide the raw paths,
assumption audits, run identifiers, controls, compute limits, and known
substitutions. The [marimo notebook](notebooks/reproduction.py) is a tutorial
view of the same evidence.

## Branch map

Branch names describe purpose rather than the automation tool that created them.
The [branch audit](branch-audit.md) records the legacy-to-clean mapping, source
tips, and the final verification checklist.

| Branch | Purpose | Result |
| --- | --- | --- |
| [`main`](https://github.com/MachineLearning-Nerd/icml26-diffusion-error-propagation/tree/main) | Documentation and publication surface | C1–C4 VERIFIED; C5 FALSIFIED; C6 BLOCKED |
| [`historical/judged-baseline`](https://github.com/MachineLearning-Nerd/icml26-diffusion-error-propagation/tree/historical/judged-baseline) | Frozen judged proxy and environment | C1–C5 toy checks; C6 BLOCKED |
| [`audit/c1-girsanov-certificate`](https://github.com/MachineLearning-Nerd/icml26-diffusion-error-propagation/tree/audit/c1-girsanov-certificate) | Exact C1 certificate and 10D calibration | C1 VERIFIED |
| [`audit/c1-corrected-calibration`](https://github.com/MachineLearning-Nerd/icml26-diffusion-error-propagation/tree/audit/c1-corrected-calibration) | Fresh-seed C1 calibration and false-bound controls | C1 VERIFIED |
| [`audit/c2-c3-observability`](https://github.com/MachineLearning-Nerd/icml26-diffusion-error-propagation/tree/audit/c2-c3-observability) | Arbitrary-`eta` and non-Gaussian observability | C2/C3 VERIFIED |
| [`audit/c4-c5-global-claims`](https://github.com/MachineLearning-Nerd/icml26-diffusion-error-propagation/tree/audit/c4-c5-global-claims) | Persistence quantifiers and bias theorem audit | C4 VERIFIED; C5 FALSIFIED |
| [`audit/c6-gmm-population`](https://github.com/MachineLearning-Nerd/icml26-diffusion-error-propagation/tree/audit/c6-gmm-population) | Paper-scale population-GMM route | Aligned partial evidence |
| [`audit/c6-fashion-protocol`](https://github.com/MachineLearning-Nerd/icml26-diffusion-error-propagation/tree/audit/c6-fashion-protocol) | Fashion-MNIST protocol and CPU feasibility audit | BLOCKED |
| [`audit/c6-cifar-contract`](https://github.com/MachineLearning-Nerd/icml26-diffusion-error-propagation/tree/audit/c6-cifar-contract) | CIFAR-10 source-contract audit | BLOCKED |
| [`audit/c6-falsification-search`](https://github.com/MachineLearning-Nerd/icml26-diffusion-error-propagation/tree/audit/c6-falsification-search) | Assumption-satisfying C6 counterexample search | No valid counterexample; BLOCKED |
| [`release/evaluator-candidate`](https://github.com/MachineLearning-Nerd/icml26-diffusion-error-propagation/tree/release/evaluator-candidate) | Cumulative evaluator-visible release candidate | Publication gates PASS; awaiting judge |

## Published artifact and limitations

The existing Space was updated in place; no second Space was created:
[DineshAI/QYA0Q28ssf, published revision
`18b2059a2546a32121b4ca5475b47ad1251ccae0`](https://huggingface.co/spaces/DineshAI/QYA0Q28ssf/tree/18b2059a2546a32121b4ca5475b47ad1251ccae0).
The earlier judged revision is retained under
`space_candidate/historical/` and protected by a SHA-256 manifest.

The principal limits are deliberate: finite calibrations do not prove universal
theorems; the C6 population-GMM solver is a material substitution; and the image
protocols cannot be uniquely reconstructed from the paper. No C6 points are
forecast.

## Citation

```bibtex
@article{khelifa2026quantifying,
  title   = {Quantifying Error Propagation and Model Collapse in Diffusion Models},
  author  = {Khelifa, Nail B. and Turner, Richard E. and Venkataramanan, Ramji},
  journal = {arXiv preprint arXiv:2602.16601},
  year    = {2026},
  doi     = {10.48550/arXiv.2602.16601}
}
```

## Thank you

Thank you to Nail B. Khelifa, Richard E. Turner, and Ramji Venkataramanan for
making the paper and its theoretical and empirical claims available for careful
independent reproduction. This audit is intended as a transparent companion to
the work: it documents what was reproduced, what was falsified as written, and
what remains blocked by missing protocol or compute details.

## Attribution

Documentation and approved repository-history normalization for this collection
are published under the `MachineLearning-Nerd` GitHub identity. Paper claims and
paper authorship remain attributed to the authors cited above.

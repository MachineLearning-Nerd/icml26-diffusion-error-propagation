# Claim evidence ledger

Each result comes from a committed claim contract, formal or numerical route,
independent checker, control, and limitation record. VERIFIED_SCOPED supports
the registered theorem or calibration contract. FALSIFIED_SCOPED records a
counterexample to the literal written claim. BLOCKED records unavailable
paper-scale inputs or protocols.

| Claim | Verdict | Primary evidence | Production path |
| --- | --- | --- | --- |
| C1 | VERIFIED_SCOPED | space_candidate/evidence/artifacts/C1 | repro_campaign/claim1_girsanov.py |
| C2 | VERIFIED_SCOPED | space_candidate/evidence/artifacts/C2-C3 | repro_campaign/claim23_observability.py |
| C3 | VERIFIED_SCOPED | space_candidate/evidence/artifacts/C2-C3 | repro_campaign/claim23_observability.py |
| C4 | VERIFIED_SCOPED | space_candidate/evidence/artifacts/C4-C5 | repro_campaign/claim45_global.py |
| C5 | FALSIFIED_SCOPED | space_candidate/evidence/artifacts/C4-C5 | repro_campaign/claim45_global.py |
| C6 | BLOCKED | space_candidate/evidence/artifacts/C6 | claim6_gmm_population.py and protocol routes |

## C1 — Girsanov endpoint bound

The exact certificate checks the 1/2 coefficient in the learned-path KL
bound, then calibrates ten-dimensional score-error trajectories across five
seeds. The raw run records no significant violation, rejects a 0.49
coefficient mutation, and rejects a false 0.1 budget under both endpoint
estimators.

The result supports the registered score-error path and finite calibration.
It does not replace every diffusion regularity assumption in the paper.

## C2 — Observable score-error lower bound

The arbitrary-eta certificate constructs endpoint-visible and time-orthogonal
drift components, checks the lower coefficient, and calibrates Gaussian and
non-Gaussian families. The raw summary records all A1–A4 audits passing,
positive-eta chi-square over eta-epsilon-squared in the range 1.00005–1.01725,
and rejection of false 1.10 and 0.50 mutations.

## C3 — Two-sided scaling

The same C2 route checks both lower and upper bounds and the positive-eta
qualifier. It is reported separately so that the scaling conclusion is not
silently inferred from a single finite calibration.

## C4 — Persistent divergence

The C4 route separates persistence quantifiers, verifies the exact limsup
floor, and tests a divergent-series control with epsilon_i squared equal to
1/(i+1). The uniform-floor mutation is rejected. This supports the registered
formal persistence contract.

## C5 — Fixed-bias multiplicative asymptotic

The source defines asymp with a fixed positive multiplicative constant. Under
summable errors, the right-hand discounted error energy tends to zero while
the fixed positive bias remains nonzero. The route therefore falsifies the
literal Theorem 4.2 claim as written. Mutation controls reject moving the bias
to zero or to the right-hand side. The appendix additive inequalities are
explicitly outside this falsification.

## C6 — Empirical alpha tradeoff

Four routes are preserved:

1. A population-KDE GMM route observes generation-20 total-second-moment drift
   of 108.38%, 24.72%, and 13.77% for alpha 0.1, 0.5, and 0.9, respectively.
2. A Fashion-MNIST route identifies 11 missing protocol fields and an
   optimistic CPU lower bound of 6.59 hours.
3. A CIFAR-10 source-contract route identifies 20 missing protocol fields and
   four missing direct tradeoff evidence items.
4. An assumption-satisfying falsification search accepts the negative control
   but finds no valid counterexample to the registered empirical claim.

The population-KDE route substitutes an exact population endpoint for the
paper's unpublished literal 100,000-center KDE acceleration and 500 Euler
steps. C6 remains BLOCKED rather than promoted to verified.

## Release and historical evidence

The historical judged artifact, evaluator-visible pages, release receipt,
red-team checks, and command ledger remain committed under space_candidate and
reports/reproduction. They document provenance and visibility, while the
current statuses come from the claim-level evidence above.

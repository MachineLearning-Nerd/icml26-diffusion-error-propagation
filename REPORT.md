# Audit report

## Result boundary

The previous live judged Space revision scored 5/12. The current candidate is
awaiting a live judge and has an 8–10/12 forecast, with 10/12 the
best-supported possibility. This is not a new paper score.

| Claim | Result | Evidence boundary |
| --- | --- | --- |
| C1 | VERIFIED_SCOPED | Exact Girsanov certificate and calibrated endpoint bounds |
| C2 | VERIFIED_SCOPED | Arbitrary-eta observability certificate and calibrations |
| C3 | VERIFIED_SCOPED | Two-sided scaling checks with qualifier controls |
| C4 | VERIFIED_SCOPED | Quantifier-separated persistence certificate |
| C5 | FALSIFIED_SCOPED | Fixed-bias asymptotic contradiction as written |
| C6 | BLOCKED | Population alignment and protocol audits without complete empirical inputs |

## Release integrity

The evaluator-visible release, historical artifact, command ledger, and red-team
receipt are preserved. The release checks all required claim artifact fields,
but release readiness is not the same as a new judge result or author
endorsement.

## Limitations

Finite calibrations do not prove universal theorems. C5 targets the literal
fixed-constant asymp wording and leaves additive appendix bounds untouched. C6
has a material population-KDE substitution and missing image protocols,
checkpoints, and raw metrics.

# Branch audit

This repository’s branch names are part of its reproducibility record. The
original experiment runner created opaque `orx/*` refs; they have been mapped to
purpose-driven names below. The legacy names are retained only as provenance in
this table and are not the final public branch interface.

## Legacy-to-clean mapping

| Final branch | Legacy source ref | Source tip before documentation changes | Purpose |
| --- | --- | --- | --- |
| `main` | `main` | `0c30ea70acd8c7d4d8468e3509bee4b94515ea41` | Documentation and publication surface |
| `historical/judged-baseline` | `orx/judged-toy-baseline-and-frozen-environment` | `4120eb776bc1a0b089d12a31781f4835e0c49081` | Frozen judged proxy and environment |
| `audit/c1-girsanov-certificate` | `orx/c1-exact-girsanov-certificate-and-10d-calibratio` | `9debb483e7bc38f17b4d741fc9bb2c4a40d472f2` | Exact C1 certificate and 10D calibration |
| `audit/c1-corrected-calibration` | `orx/c1-calibrated-violation-test-and-false-bound-con` | `20bf5fed2d69b8b16017516b6bfe70b03b9bf816` | Fresh-seed C1 calibration and false-bound controls |
| `audit/c2-c3-observability` | `orx/c2-c3-exact-observability-certificates-and-non-g` | `82ebd6a282101409cde92fbf81fb1dedbd08a386` | Arbitrary-eta and non-Gaussian observability |
| `audit/c4-c5-global-claims` | `orx/c4-exact-persistence-proof-and-c5-bias-contradic` | `a6ace14d8ab3a444861e439e687da44af80586fd` | Persistence quantifiers and bias theorem audit |
| `audit/c6-gmm-population` | `orx/c6-route-1-full-scale-gmm-population-kde-closure` | `6bdd221a95fa1782cc0816d79aaaf3e0a63f5ea6` | Paper-scale population-GMM route |
| `audit/c6-fashion-protocol` | `orx/c6-route-2-fashion-mnist-protocol-and-cpu-lower` | `970446a85031a49c66d33be7ee07f33452ac8c9a` | Fashion-MNIST protocol and CPU feasibility audit |
| `audit/c6-cifar-contract` | `orx/c6-route-3-cifar-10-source-contract-audit` | `6784a9e14d5b65a02b7921cd736e0d0b980c1ed7` | CIFAR-10 source-contract audit |
| `audit/c6-falsification-search` | `orx/c6-route-4-assumption-satisfying-falsification-s` | `19aa5251ca0b02fab27d16a5b09a46ee2b62ce70` | Assumption-satisfying C6 counterexample search |
| `release/evaluator-candidate` | `orx/evaluator-visible-cumulative-release-candidate` | `195c2dbb517e9bc1ddbc7dbc6032de5bd077e679` | Cumulative evaluator-visible release candidate |

## Verification contract

After normalization, the public repository must satisfy all of the following:

- only the 11 final branches in the table are present;
- `main` is the default branch;
- every commit author and committer is
  MachineLearning-Nerd <MachineLearning-Nerd@users.noreply.github.com>;
- every branch contains the current README and this audit record;
- all commit authors and committers resolve to `MachineLearning-Nerd`’s verified
  no-reply identity;
- active README/report links resolve to the renamed repository and final branch
  names; and
- `git diff --check`, identity scans, and remote API metadata checks pass.

The historical Space snapshot and the legacy ref names above are evidence of
lineage, not active reproduction branches.

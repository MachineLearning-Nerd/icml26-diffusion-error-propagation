# Environment and reproduction contract

## Fixed command

~~~bash
uv sync --frozen
uv run --frozen python -m repro_campaign.run
~~~

The fixed entrypoint runs the historical baseline, claim modules, independent
checkers, controls, and release validation. The committed Python 3.12
environment is described by pyproject.toml and uv.lock.

## Runtime

- Backend: CPU
- Requested numerical threads: 1 where recorded
- Formal and calibration routes: small, seeded local/HF CPU jobs
- C6 population route: eight active worker processes in the recorded run
- Image routes: feasibility and protocol audits, not paper-scale training
- External data: no complete paper-scale image dataset/checkpoint bundle

The recorded raw files preserve runtime and visible CPU allocations. No
unavailable image pipeline is silently substituted for the C6 verdict.

## Evidence locations

- Current code: repro_campaign/
- Space candidate code: space_candidate/evidence/code/repro_campaign/
- Claim artifacts: space_candidate/evidence/artifacts/
- Published pages: space_candidate/pages/
- Detailed report: reports/reproduction/report.md
- Release receipt: reports/reproduction/release_receipt.md
- Environment pins: pyproject.toml and uv.lock

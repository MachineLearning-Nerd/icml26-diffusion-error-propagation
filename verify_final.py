from __future__ import annotations

import json
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parent
CANONICAL_NAME = "MachineLearning-Nerd"
CANONICAL_EMAIL = "MachineLearning-Nerd@users.noreply.github.com"
EXPECTED_BRANCHES = {
    "main",
    "historical/judged-baseline",
    "audit/c1-girsanov-certificate",
    "audit/c1-corrected-calibration",
    "audit/c2-c3-observability",
    "audit/c4-c5-global-claims",
    "audit/c6-gmm-population",
    "audit/c6-fashion-protocol",
    "audit/c6-cifar-contract",
    "audit/c6-falsification-search",
    "release/evaluator-candidate",
}
EXPECTED_COMMITS = 27
EXPECTED_STATUSES = {
    "C1": "VERIFIED_SCOPED",
    "C2": "VERIFIED_SCOPED",
    "C3": "VERIFIED_SCOPED",
    "C4": "VERIFIED_SCOPED",
    "C5": "FALSIFIED_SCOPED",
    "C6": "BLOCKED",
}
EXPECTED_OVERALL = (
    "PARTIAL_C1_C2_C3_C4_VERIFIED_C5_FALSIFIED_C6_BLOCKED_"
    "HISTORICAL_SCORE_5_OF_12_NO_CURRENT_SCORE"
)


def run(*args: str) -> str:
    return subprocess.check_output(["git", *args], cwd=ROOT, text=True).strip()


def read_json(relative_path: str) -> dict:
    return json.loads((ROOT / relative_path).read_text())


def require(condition: bool, message: str) -> None:
    if not condition:
        raise SystemExit(f"VERIFY_FAILED: {message}")


def published_branches() -> set[str]:
    try:
        output = run("ls-remote", "--heads", "origin")
    except subprocess.CalledProcessError:
        output = run("for-each-ref", "--format=%(refname:short)", "refs/heads/")
        return {line for line in output.splitlines() if line}
    return {
        line.split("refs/heads/", 1)[1]
        for line in output.splitlines()
        if "refs/heads/" in line
    }


def main() -> None:
    claims = read_json("claims.json")
    verdicts = read_json("reproduction_verdicts.json")
    manifest = read_json("EVIDENCE_MANIFEST.json")
    state = read_json("AUTONOMOUS_STATE.json")
    c1 = read_json("space_candidate/evidence/artifacts/C1/raw_formal.json")
    c23 = read_json("space_candidate/evidence/artifacts/C2-C3/raw_formal_summary.json")
    c45 = read_json("space_candidate/evidence/artifacts/C4-C5/raw_formal_summary.json")
    c6r1 = read_json("space_candidate/evidence/artifacts/C6/route1/raw_formal_summary.json")
    c6r2 = read_json("space_candidate/evidence/artifacts/C6/route2/raw_formal_summary.json")
    c6r3 = read_json("space_candidate/evidence/artifacts/C6/route3/raw_formal_summary.json")
    c6r4 = read_json("space_candidate/evidence/artifacts/C6/route4/raw_formal_summary.json")
    release = read_json("space_candidate/evidence/artifacts/release/red_team_release_pass.json")

    branches = published_branches()
    require(branches == EXPECTED_BRANCHES, f"published branch set is {sorted(branches)}")
    require("orx" not in " ".join(branches), "legacy orx branch remains")
    require(run("symbolic-ref", "--short", "HEAD") == "main", "main is not checked out")
    require(int(run("rev-list", "--count", "--all")) == EXPECTED_COMMITS, "reachable commit count changed")

    identities = run("log", "--all", "--format=%an%x09%ae%x09%cn%x09%ce").splitlines()
    expected_identity = "\t".join(
        [CANONICAL_NAME, CANONICAL_EMAIL, CANONICAL_NAME, CANONICAL_EMAIL]
    )
    require(identities and all(line == expected_identity for line in identities), "commit identity is not canonical")

    require(claims["overall_status"] == EXPECTED_OVERALL, "claims overall status mismatch")
    require(verdicts["overall_status"] == EXPECTED_OVERALL, "verdict overall status mismatch")
    require(state["overall_status"] == EXPECTED_OVERALL, "state overall status mismatch")
    require(claims["current_score_claim"] is False, "claims make a current score claim")
    require(verdicts["historical_evaluation"]["current_score_claim"] is False, "verdicts make a current score claim")
    require(state["current_score_claim"] is False, "state makes a current score claim")
    require(verdicts["publication"]["publication_allowed"] is False, "publication boundary changed")

    claim_statuses = {claim["id"]: claim["status"] for claim in claims["claims"]}
    require(claim_statuses == EXPECTED_STATUSES, f"claim statuses are {claim_statuses}")
    require(
        {claim_id: item["status"] for claim_id, item in verdicts["claims"].items()}
        == EXPECTED_STATUSES,
        "machine-readable verdict statuses mismatch",
    )

    require(c1["certificate"]["accepted"] is True, "C1 certificate changed")
    require(c1["certificate"]["coefficient_0p49_mutation_observed"] == "REJECT", "C1 mutation changed")
    require(c23["proof"]["accepted"] is True, "C2-C3 certificate changed")
    require(c23["verdicts"] == {"C2": "VERIFIED", "C3": "VERIFIED"}, "C2-C3 verdicts changed")
    require(c45["verdicts"]["C4"] == "VERIFIED", "C4 result changed")
    require(c45["verdicts"]["C5"] == "FALSIFIED", "C5 result changed")
    require(c6r1["C6_verdict"] == "BLOCKED", "C6 route 1 boundary changed")
    require(c6r2["C6_verdict"] == "BLOCKED", "C6 route 2 boundary changed")
    require(c6r3["C6_verdict"] == "BLOCKED", "C6 route 3 boundary changed")
    require(c6r4["C6_verdict"] == "BLOCKED", "C6 route 4 boundary changed")
    require(c6r1["assessment"] == "ALIGNED_ON_POPULATION_KDE_GMM_ONLY", "C6 alignment boundary changed")
    require(c6r4["accepted_counterexamples"] == 0, "C6 falsification search changed")

    for claim_id, checks in release["claim_checks"].items():
        require(all(checks.values()), f"release check failed for {claim_id}")

    missing = [
        path for path in manifest["required_paths"] if not (ROOT / path).exists()
    ]
    require(not missing, f"manifest paths missing: {missing}")
    require(state["canonical_identity"]["email"] == CANONICAL_EMAIL, "state identity mismatch")

    readme = (ROOT / "README.md").read_text()
    for required_text in (
        "arXiv:2602.16601",
        "STATUS.md",
        "CLAIM_EVIDENCE.md",
        "Thank you",
        "not a new paper score",
    ):
        require(required_text in readme, f"README is missing {required_text!r}")

    branch_audit = (ROOT / "branch-audit.md").read_text()
    require(
        f"{CANONICAL_NAME} <{CANONICAL_EMAIL}>" in branch_audit,
        "branch audit identity is not canonical",
    )

    print(
        "FINAL_AUDIT=VERIFIED branches=11 commits=27 "
        "claims=C1:C2:C3:C4_verified_scoped,C5_falsified_scoped,C6_blocked "
        "historical_score=5/12 current_score_claim=false publication_allowed=false"
    )


if __name__ == "__main__":
    main()

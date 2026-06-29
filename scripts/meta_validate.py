#!/usr/bin/env python3
"""Lightweight MetaProject scaffold validator.

This intentionally uses only the Python standard library so it can run in
minimal local/CI environments.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FILES = [
    "README.md",
    "PROJECT_KERNEL.md",
    "PRODUCT_SPEC.md",
    "FEATURE_GRAPH.yaml",
    "PHASE_PLAN.md",
    "BRANCH_MANIFEST.yaml",
    "DEFINITION_OF_DONE.md",
    "AGENT_PROTOCOL.md",
    "CEO_NOTES.md",
    "PM_STATUS.md",
    ".agents/prompts/CHATGPT_PROJECT_SEED.md",
    ".agents/prompts/LOCAL_CODEX_PM_SEED.md",
    ".agents/roles/ceo.md",
    ".agents/roles/pm.md",
    ".agents/roles/developer.md",
    ".agents/roles/reviewer.md",
    ".github/pull_request_template.md",
    ".github/workflows/meta-check.yml",
    "tasks/README.md",
    "reviews/README.md",
]

REQUIRED_JOB_SECTIONS = [
    "## Job ID",
    "## Branch",
    "## Objective",
    "## Scope In",
    "## Scope Out",
    "## Acceptance Criteria",
    "## Validation Commands",
    "## Required Output",
    "## Status",
]


def fail(message: str) -> None:
    print(f"[FAIL] {message}")


def ok(message: str) -> None:
    print(f"[OK] {message}")


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def validate_required_files(errors: list[str]) -> None:
    for rel in REQUIRED_FILES:
        path = ROOT / rel
        if path.exists() and path.stat().st_size > 0:
            ok(f"required file exists: {rel}")
        else:
            errors.append(f"missing or empty required file: {rel}")
            fail(errors[-1])


def parse_frontmatter(text: str) -> dict[str, str]:
    if not text.startswith("---\n"):
        return {}
    end = text.find("\n---", 4)
    if end == -1:
        return {}

    block = text[4:end].strip()
    result: dict[str, str] = {}
    current_key: str | None = None

    for raw_line in block.splitlines():
        line = raw_line.rstrip()
        if not line.strip():
            continue

        if re.match(r"^[A-Za-z_][A-Za-z0-9_-]*:", line):
            key, value = line.split(":", 1)
            current_key = key.strip()
            result[current_key] = value.strip().strip('"').strip("'")
        elif current_key:
            # Multi-line/list values are not fully parsed; existence is enough
            result[current_key] += "\n" + line

    return result


def validate_job_file(path: Path, errors: list[str]) -> None:
    rel = path.relative_to(ROOT).as_posix()
    text = read(path)

    meta = parse_frontmatter(text)
    for key in ["id", "phase", "title", "branch", "status", "feature"]:
        if key not in meta or not meta[key]:
            errors.append(f"{rel}: missing frontmatter key `{key}`")
            fail(errors[-1])

    branch = meta.get("branch", "")
    if branch and not branch.startswith("job/"):
        errors.append(f"{rel}: branch should start with `job/`, got `{branch}`")
        fail(errors[-1])

    job_id = meta.get("id")
    if job_id and not re.match(r"^P\d{2}-J\d{3}$", job_id):
        errors.append(f"{rel}: job id should match Pxx-Jxxx, got `{job_id}`")
        fail(errors[-1])

    for section in REQUIRED_JOB_SECTIONS:
        if section not in text:
            errors.append(f"{rel}: missing section `{section}`")
            fail(errors[-1])

    if not any(marker in text for marker in ["- [ ]", "- [x]"]):
        errors.append(f"{rel}: acceptance criteria should use checkboxes")
        fail(errors[-1])

    if not any(rel in line or path.name in line for line in text.splitlines()):
        # Not a hard failure. Keep output informative.
        pass

    if not any(e.startswith(rel) for e in errors):
        ok(f"job contract valid: {rel}")


def validate_tasks(errors: list[str]) -> None:
    job_files = sorted((ROOT / "tasks").glob("P*/J*.md"))
    if not job_files:
        errors.append("no job files found under tasks/P*/J*.md")
        fail(errors[-1])
        return

    for path in job_files:
        validate_job_file(path, errors)


def validate_manifest_mentions_jobs(errors: list[str]) -> None:
    manifest = read(ROOT / "BRANCH_MANIFEST.yaml")
    job_files = sorted((ROOT / "tasks").glob("P*/J*.md"))

    for path in job_files:
        text = read(path)
        meta = parse_frontmatter(text)
        job_id = meta.get("id", "")
        branch = meta.get("branch", "")
        rel = path.relative_to(ROOT).as_posix()

        if job_id and job_id not in manifest:
            errors.append(f"BRANCH_MANIFEST.yaml does not mention job {job_id}")
            fail(errors[-1])
        if branch and branch not in manifest:
            errors.append(f"BRANCH_MANIFEST.yaml does not mention branch {branch}")
            fail(errors[-1])
        if rel and rel not in manifest:
            errors.append(f"BRANCH_MANIFEST.yaml does not mention task file {rel}")
            fail(errors[-1])

    if not any("BRANCH_MANIFEST.yaml does not mention" in e for e in errors):
        ok("branch manifest mentions all job files")


def validate_no_common_secret_patterns(errors: list[str]) -> None:
    suspicious_patterns = [
        re.compile(r"ghp_[A-Za-z0-9_]{20,}"),
        re.compile(r"github_pat_[A-Za-z0-9_]{20,}"),
        re.compile(r"sk-[A-Za-z0-9]{20,}"),
        re.compile(r"AKIA[0-9A-Z]{16}"),
    ]

    checked = 0
    for path in ROOT.rglob("*"):
        if not path.is_file():
            continue
        if ".git" in path.parts:
            continue
        if path.stat().st_size > 512_000:
            continue
        try:
            text = read(path)
        except UnicodeDecodeError:
            continue
        checked += 1
        for pattern in suspicious_patterns:
            if pattern.search(text):
                rel = path.relative_to(ROOT).as_posix()
                errors.append(f"possible secret pattern in {rel}")
                fail(errors[-1])

    ok(f"secret-pattern scan completed over {checked} text files")


def main() -> int:
    errors: list[str] = []

    print("MetaProject scaffold validation")
    print(f"Root: {ROOT}")

    validate_required_files(errors)
    validate_tasks(errors)
    validate_manifest_mentions_jobs(errors)
    validate_no_common_secret_patterns(errors)

    if errors:
        print()
        print(f"Validation failed with {len(errors)} error(s):")
        for err in errors:
            print(f" - {err}")
        return 1

    print()
    print("Validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

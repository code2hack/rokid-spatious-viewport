#!/usr/bin/env bash
set -euo pipefail

PHASE="${1:-P01}"
TASK_DIR="tasks/$PHASE"

if ! command -v gh >/dev/null 2>&1; then
  echo "GitHub CLI 'gh' is required for this helper." >&2
  exit 2
fi

if [[ ! -d "$TASK_DIR" ]]; then
  echo "No task directory found: $TASK_DIR" >&2
  exit 1
fi

for task_file in "$TASK_DIR"/J*.md; do
  [[ -f "$task_file" ]] || continue

  job_id="$(grep -m1 '^id:' "$task_file" | sed 's/^id:[[:space:]]*//')"
  title="$(grep -m1 '^title:' "$task_file" | sed 's/^title:[[:space:]]*//')"
  status="$(grep -m1 '^status:' "$task_file" | sed 's/^status:[[:space:]]*//')"

  labels="job,$PHASE"
  if [[ "$title" == *"discovery"* ]] || [[ "$title" == *"Discovery"* ]]; then
    labels="$labels,discovery"
  fi
  if [[ "$status" == "blocked" ]]; then
    labels="$labels,blocked"
  fi

  echo "[GitHub] Creating issue for $job_id — $title"
  gh issue create \
    --title "[JOB] $job_id: $title" \
    --body-file "$task_file" \
    --label "$labels" || true
done

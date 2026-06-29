#!/usr/bin/env bash
set -euo pipefail

PHASE="${1:-P01}"
BASE_REF="${2:-origin/main}"
TASK_DIR="tasks/$PHASE"

if [[ ! -d "$TASK_DIR" ]]; then
  echo "No task directory found: $TASK_DIR" >&2
  exit 1
fi

echo "[PM] Dispatching phase: $PHASE"
echo "[PM] Base ref: $BASE_REF"

for task_file in "$TASK_DIR"/J*.md; do
  [[ -f "$task_file" ]] || continue

  status="$(grep -m1 '^status:' "$task_file" | sed 's/^status:[[:space:]]*//')"
  branch="$(grep -m1 '^branch:' "$task_file" | sed 's/^branch:[[:space:]]*//')"
  job_id="$(grep -m1 '^id:' "$task_file" | sed 's/^id:[[:space:]]*//')"
  title="$(grep -m1 '^title:' "$task_file" | sed 's/^title:[[:space:]]*//')"

  if [[ -z "$branch" ]]; then
    echo "[PM] Skip $task_file: no branch in frontmatter"
    continue
  fi

  case "$status" in
    ready_for_dispatch|dispatched|in_progress)
      echo "[PM] Creating worktree for $job_id — $title"
      scripts/pm_create_worktree.sh "$branch" "$BASE_REF"
      ;;
    *)
      echo "[PM] Skip $job_id ($status): $title"
      ;;
  esac
done

echo "[PM] Phase dispatch complete."

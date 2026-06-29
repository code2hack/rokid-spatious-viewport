#!/usr/bin/env bash
set -euo pipefail

if [[ $# -lt 1 ]]; then
  echo "Usage: $0 <job-branch> [base-ref]" >&2
  echo "Example: $0 job/P01-J001-termux-environment-discovery origin/phase/P01-discovery" >&2
  exit 2
fi

BRANCH="$1"
BASE_REF="${2:-origin/main}"
REPO_ROOT="$(git rev-parse --show-toplevel)"
WORKTREE_ROOT="${WORKTREE_ROOT:-$(dirname "$REPO_ROOT")/worktrees}"
SAFE_NAME="$(echo "$BRANCH" | sed 's#[/:]#-#g')"
WORKTREE_PATH="$WORKTREE_ROOT/$SAFE_NAME"

mkdir -p "$WORKTREE_ROOT"

echo "[PM] repo: $REPO_ROOT"
echo "[PM] branch: $BRANCH"
echo "[PM] base: $BASE_REF"
echo "[PM] worktree: $WORKTREE_PATH"

git fetch --all --prune || true

if [[ -d "$WORKTREE_PATH/.git" ]] || [[ -f "$WORKTREE_PATH/.git" ]]; then
  echo "[PM] worktree already exists: $WORKTREE_PATH"
  exit 0
fi

if git show-ref --verify --quiet "refs/heads/$BRANCH"; then
  git worktree add "$WORKTREE_PATH" "$BRANCH"
elif git ls-remote --exit-code --heads origin "$BRANCH" >/dev/null 2>&1; then
  git branch --track "$BRANCH" "origin/$BRANCH" || true
  git worktree add "$WORKTREE_PATH" "$BRANCH"
else
  git worktree add -b "$BRANCH" "$WORKTREE_PATH" "$BASE_REF"
fi

echo "[PM] created worktree: $WORKTREE_PATH"

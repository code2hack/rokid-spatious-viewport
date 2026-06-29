#!/usr/bin/env bash
set -euo pipefail

echo "# Repo Snapshot"
echo
echo "Date: $(date -Iseconds)"
echo "Branch: $(git branch --show-current 2>/dev/null || echo unknown)"
echo
echo "## Files"
find . \
  -path './.git' -prune -o \
  -path './.git/*' -prune -o \
  -type f \
  -print | sort
echo
echo "## Git status"
git status --short || true

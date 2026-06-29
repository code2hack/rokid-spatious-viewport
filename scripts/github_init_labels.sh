#!/usr/bin/env bash
set -euo pipefail

if ! command -v gh >/dev/null 2>&1; then
  echo "GitHub CLI 'gh' is required for this helper." >&2
  exit 2
fi

create_label() {
  local name="$1"
  local color="$2"
  local desc="$3"
  gh label create "$name" --color "$color" --description "$desc" 2>/dev/null \
    || gh label edit "$name" --color "$color" --description "$desc"
}

create_label "phase" "5319e7" "MetaProject phase"
create_label "feature" "1d76db" "MetaProject feature"
create_label "job" "0e8a16" "MetaProject job"
create_label "pm-review" "fbca04" "Needs or contains PM review"
create_label "ceo-review" "b60205" "Needs or contains CEO review"
create_label "boss-review" "d93f0b" "Needs Boss/User verification"
create_label "blocked" "b60205" "Blocked by dependency or decision"
create_label "discovery" "0052cc" "Discovery/research work"
create_label "scaffold" "cfd3d7" "Scaffold/setup work"

echo "Labels initialized."

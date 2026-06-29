# GitHub Bootstrap

The repository was empty when this scaffold was prepared, so the first commit can go directly to `main`.

## Initial push

From the applied scaffold:

```bash
python3 scripts/meta_validate.py
git add .
git commit -m "chore: initialize MetaProject scaffold"
git push -u origin main
```

## After initial push

Do not push directly to `main` for normal work.

Create a phase branch:

```bash
git switch main
git pull --ff-only
git switch -c phase/P01-discovery
git push -u origin phase/P01-discovery
```

Create job worktrees:

```bash
scripts/pm_dispatch_phase.sh P01 origin/phase/P01-discovery
```

## Optional GitHub CLI setup

Initialize labels:

```bash
scripts/github_init_labels.sh
```

Create issues for a phase:

```bash
scripts/github_create_phase_issues.sh P01
```

## Recommended manual repository settings

After initial push, consider enabling:

- Pull requests before merge to `main`.
- Required status checks.
- No direct pushes to `main`.
- Branch naming discipline.

Keep this lightweight until the workflow proves itself.

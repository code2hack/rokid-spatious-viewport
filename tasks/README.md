# Tasks

Tasks are executable job contracts.

Naming:

```text
tasks/Pxx/Jxxx-short-name.md
```

Each job must include YAML front matter:

```yaml
---
id: P01-J001
phase: P01
title: Example
branch: job/P01-J001-example
status: ready_for_dispatch
feature: F001
depends_on: []
owner: developer-sub-agent
---
```

A task should be understandable without chat history.

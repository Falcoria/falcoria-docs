# Concepts

This section covers the mechanisms behind Falcoria's scan pipeline — from targets to [shared scope state](scope-state.md).

```
Targets
  ↓
Deduplication  — removes duplicates, resolves hostnames,
                 skips already-scanned targets by default
  ↓
Distribution   — splits work across workers
  ↓
Workers        — execute scans
  ↓
Import Modes   — merge results into scope state
  ↓
Change History — records what changed
```

All of the above is configured through a [scan config](scan-configs.md).

## How it all connects

A single scan command triggers the full pipeline:

1. Targets go through [deduplication](deduplication.md) — duplicates are removed, hostnames are resolved and unified by IP, and already-scanned targets are skipped by default
2. Remaining targets are [distributed](distribution.md) across workers, each scanning from its own IP. The task queue tracks progress, so interrupted scans resume without rescanning
3. Each worker's results are merged into the [scope state](scope-state.md) through [import modes](import-modes.md) — the merge strategy determines whether ports are added, updated, or replaced
4. [Change history](change-history.md) records what changed since the last run

The result is one [shared scope state](scope-state.md) that stays current without manual file management. It can be exported as Nmap XML or JSON at any point. See [Benchmarks](../benchmarks.md) for measured examples.

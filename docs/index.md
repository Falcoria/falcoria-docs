# Falcoria

Falcoria is a system for team-based port scanning on large scopes. It maintains one shared report that every scan updates — no separate files to merge.

## The problem

On a large engagement, scan output multiplies fast. Different people use different tools, the scope gets split into chunks, rescans add more files. After a few days, there's no single place to check what's open — the answer is spread across dozens of files from different people and points in time.

Teams deal with this using whatever is at hand — shared folders, spreadsheets, Notion, Slack. None of these are built for scan data, and the results still have to be merged.

![Traditional vs Falcoria](images/algo_diff.png){ width="700" align=center }

## How Falcoria approaches this

Falcoria treats scans as state updates. Each scan — whether Falcoria's own or an imported scan report — writes directly into a shared dataset called [ScanLedger](architecture.md). New results extend or update existing records. Additions, removals, and changes are tracked over time. There is no intermediate file step.

### Key features

- **[Import modes](concepts/import-modes.md)** — control how each scan updates ScanLedger. Add ports without overwriting, or replace the current view entirely.
- **[Change tracking](concepts/change-history.md)** — records what changed between scans: ports opening/closing, services updating.
- **[Deduplication](concepts/deduplication.md)** — filters out duplicate and already-scanned targets before scanning starts, reducing scan time and network load.
- **[Distributed execution](concepts/distribution.md)** — splits work across multiple workers, each on its own network path.
- **[Resumable scans](workflows.md#resuming-interrupted-scans)** — interrupted scans pick up where they left off.

All of this runs from a single scan command — deduplication, distribution, result merging, and change tracking happen automatically. The scope state can be exported as Nmap XML or JSON when needed.

![Shared report evolution](images/state_evolution.png){ width="700" align=center }

At any point, querying ScanLedger returns the current scope state across every scan that's been done.

## Who it is for

- Penetration testers managing large scopes with a team
- Red team operators running repeated discovery across changing networks
- Security engineers maintaining current host/port/service visibility
- Security automation teams looking for an API-driven backend to aggregate scan data from various sources

## Next steps

- [Getting Started](getting-started.md) — setup and first scan
- [Architecture](architecture.md) — how the system is structured
- [Concepts](concepts/index.md) — how the pipeline works end to end
- [Workflows](workflows.md) — common usage patterns

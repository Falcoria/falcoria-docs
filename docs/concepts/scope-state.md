# Scope state

Scope state is the current view of all hosts, ports, and services in a project — built from every scan applied through [import modes](import-modes.md). A single scan updates it, but the scope state reflects all scans combined.

The state is shared across the team. One project has one scope state, accessible to every team member through the API or [falcli](https://github.com/Falcoria/falcli). When someone runs a scan or imports a report, the scope state updates for everyone.

Changes between scans — ports opening, closing, services updating — are recorded separately in [change history](change-history.md).

## Data model

IP is the primary entity in the data model.

```
Project
  ├── IP
  │     ├── Ports
  │     │     └── Service info
  │     └── Hostnames (many-to-many)
  └── Hostname
        └── IPs (many-to-many)
```

- Each IP is unique per project. Each port is unique per IP, protocol, and port number.
- Hostnames are linked to IPs through a many-to-many relationship: one hostname can resolve to multiple IPs, and one IP can have multiple hostnames. This is why [deduplication](deduplication.md) resolves hostnames before scanning — to avoid scanning the same IP twice under different names.
- Everything is scoped to a project. Different projects have independent scope states.

## How scope state gets updated

Each scan is applied through an [import mode](import-modes.md) that determines what happens to existing data:

- New IPs and ports are added
- Existing service info can be refreshed or left unchanged
- Ports can be marked as closed (in [replace mode](import-modes.md#replace))

The system parses the original scan command to know which ports were in scope — so it can distinguish "this port was not scanned" from "this port was scanned and found closed".

## Scope state vs scan report

Scope state is built from all applied scans. It reflects which hosts are known, which ports are open, what services are running. When a new scan is applied, the scope state gets updated accordingly.

A scan report is a file from one scan at one point in time. It exists on its own and has no context about previous scans.

The scope state can be [exported](../workflows.md#exporting-results) as Nmap XML or JSON at any time — a snapshot of whatever the current state is.

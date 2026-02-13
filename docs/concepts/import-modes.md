# Import Modes

Import modes control how scan results are merged into [ScanLedger](../architecture.md) — whether to add ports, update service info, or mark ports as closed.

## IP-level behavior

All modes share the same IP-level logic:

- New IPs from the report are always added.
- Existing IPs are never removed.

The difference between modes is in how they handle ports.

## Port-level reference

How existing data and an incoming report are combined for a single port. INSERT is not in the table — it operates on whole hosts, not individual ports.

| ScanLedger (before) | Incoming report | APPEND | UPDATE | REPLACE |
|:---|:---|:---|:---|:---|
| 22/tcp open OpenSSH | 22/tcp open | ⚪ unchanged | ⚪ unchanged | 🟡 updated |
| 22/tcp open | 22/tcp open OpenSSH | ⚪ unchanged | 🟡 updated | 🟡 updated |
| 22/tcp open | 22/tcp closed | ⚪ unchanged | ⚪ unchanged | 🔴 closed |
| — | 22/tcp open OpenSSH | 🟢 added | 🟢 added | 🟢 added |
| 22/tcp open | — (port in scanned range) | ⚪ unchanged | ⚪ unchanged | 🔴 closed |

- 🟢 **added** — port was created
- 🟡 **updated** — existing port was modified
- ⚪ **unchanged** — existing port was not touched
- 🔴 **closed** — port state changed to closed

## Insert

- New hosts are added with their ports.
- Existing hosts are skipped entirely.

## Append

- New ports are added.
- Existing ports are not modified.
- Ports are never closed.

## Update

- New ports are added.
- Existing ports are updated if the report has new data (service, banner).
- Empty fields in the report do not overwrite existing data.
- Ports are never closed.

## Replace

- New ports are added.
- Existing ports are updated if the report has new data (service, banner).
- Empty fields in the report do not overwrite existing data.
- Ports reported as closed or filtered are marked as closed.
- Ports absent from the report but within the scanned range are also marked as closed. Falcoria parses the scan command line to determine which ports were in scope — if a known port falls within that range but has no result, it is treated as closed.

## When to use each mode

- **Insert** — merging host lists from different sources, importing repeated scans of the same scope, aggregating recon output.
- **Append** — partial or fast scans where some ports may be missed. Adds what was found without overwriting existing data.
- **Update** — follow-up service detection scans. Refreshes service info on known ports while protecting against false closures.
- **Replace** — complete, high-confidence scans where results should be applied as-is.

## Specifying a mode

When scanning:

```bash
falcli scan start --config <config> --mode append --targets-file hosts.txt
```

When importing:

```bash
falcli project ips import -f report.xml --mode replace
```

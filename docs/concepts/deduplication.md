# Deduplication Behavior

Falcoria applies deduplication at multiple stages of the scanning workflow. This ensures efficient resource usage, consistent scan results, and seamless support for resuming interrupted scans. This document describes how deduplication works both during the import of external scan reports and during the scan phase itself.

---

## Deduplication During Scan Report Imports

When importing external Nmap reports, Falcoria uses import modes to control how incoming data is merged with existing results. These modes prevent duplication of previously scanned ports, IPs, or entries that match known states.

The deduplication logic depends entirely on the selected import mode. For example:

- `insert` will skip any existing entries
- `replace` will remove and overwrite previous data
- `update` only modifies ports that already exist

To understand these behaviors in depth, see the following resources:

- [Import External Reports Use Case](../use-cases/import-external-reports.md)
- [Import Modes Overview](../import-modes/index.md)

---

## Why Deduplication Matters

Falcoria’s deduplication mechanisms are critical for:

- Reducing scan duration by avoiding repeated work
- Preventing duplicate entries in the project database
- Minimizing network and system load
- Enabling scan resumption without reconfiguration or manual filtering

Once a host is scanned or queued, Falcoria will skip it on repeated execution of the same scan command. This allows the system to resume scans from where they stopped and prevents duplicate tasks from being created.

---

## Deduplication During Scanning

Falcoria applies three layers of deduplication during the scan phase:

### 1. Deduplication of User-Provided Hosts

If the user supplies a target file that contains duplicate entries, only unique hosts will be accepted. The deduplication occurs at the [Tasker](../architecture.md) level before queueing begins.

**Example: Hosts file with duplicates**
```bash
$ cat hosts_with_duplicates.txt
159.223.15.22
159.223.15.22
188.166.121.245
```

**Scan execution after input deduplication**
```bash
$ ./falcli.py scan start --targets-file hosts_with_duplicates.txt
[+] Scan targets sent for project 4e0d5a24-791d-4abb-a1fd-212f738b48b8.
[+] Sent to scan:
  - 159.223.15.22
  - 188.166.121.245
```

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

---

### 2. Deduplication Against Queued Targets

If a host is already queued for scanning and the same target is submitted again, Falcoria will reject it without duplication. This prevents redundant load and preserves system efficiency.

**Initial scan submission**
```bash
$ ./falcli.py scan start --targets-file hosts.txt
[+] Scan targets sent for project 4e0d5a24-791d-4abb-a1fd-212f738b48b8.
[+] Sent to scan:
  - 188.166.121.245
  - 128.199.62.51
  - 159.223.15.22
  - 134.209.203.62
```

**Verifying that targets are already in the scan queue**
```bash
$ ./falcli.py scan status
[+] Scan status for project 4e0d5a24-791d-4abb-a1fd-212f738b48b8: 4
```

**Re-submitting the same targets**
```bash
$ ./falcli.py scan start --targets-file hosts.txt
[+] Scan targets sent for project 4e0d5a24-791d-4abb-a1fd-212f738b48b8.
[!] No targets were accepted for scanning.
[!] Rejected targets:
  - 188.166.121.245
  - 128.199.62.51
  - 159.223.15.22
  - 134.209.203.62
```

---

### 3. Deduplication Against Previously Scanned Hosts

Falcoria checks the project’s scan history in ScanLedger. If a host has already been scanned and recorded in the database, it will not be accepted for scanning again using the same command and project context.

**Database contents**
```bash
$ ./falcli.py project ips list
IP               PORT_COUNT
128.199.62.51    6         
134.209.203.62   6         
159.223.15.22    6         
188.166.121.245  8         
```

**Attempting to rescan the same IPs**
```bash
$ cat hosts.txt
134.209.203.62
159.223.15.22
188.166.121.245
128.199.62.51

$ ./falcli.py scan start --targets-file hosts.txt
[+] Scan targets sent for project 4e0d5a24-791d-4abb-a1fd-212f738b48b8.
[!] No targets were accepted for scanning.
[!] Rejected targets:
  - 188.166.121.245
  - 128.199.62.51
  - 159.223.15.22
  - 134.209.203.62
```

---

## Summary

Falcoria enforces deduplication at the following stages:

- When importing external reports
- When parsing user input
- When filtering against the current queue
- When validating against the project’s historical records

These mechanisms work together to prevent waste, accelerate scans, and allow users to safely repeat scan commands without unintended repetition. This makes Falcoria suitable for large-scale, iterative scanning across complex infrastructures.
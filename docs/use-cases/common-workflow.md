# Common Workflow

This section provides the typical workflow for using Falcoria — from project creation to scanning, status checks, results retrieval, and cleanup.

---

## 1. Create a Project

All scanned data and related information in Falcoria are grouped under **projects**. This allows clear separation of different assessments.

To create a project:

```bash
./falcli.py project create pentest_project
```

Example output:

```bash
[+] Project 'pentest_project' created successfully (26e73c7f-c1e3-4131-8ee5-99a01681af9f).
  project_name  : pentest_project
  id            : 26e73c7f-c1e3-4131-8ee5-99a01681af9f
  users         : admin
First project saved.
```

To set the active project:

```bash
./falcli.py project set-active <uuid>
```

List all projects stored on the server:

```bash
./falcli.py project list
```

---

## 2. Start a Scan

To launch a scan for the active project:

```bash
./falcli.py scan start --targets-file hosts.txt
```

Example output:

```bash
[+] Scan initiated for project: 'pentest_project' (26e73c7f-c1e3-4131-8ee5-99a01681af9f).

Scan Settings
  Import mode        : insert
  Nmap (open ports)  : -n --max-retries 1 --min-rate 300 -Pn -p 1-65535
  Nmap (services)    : -sV -Pn
  Scan config        : app/data/scan_configs/default.yaml

Scan Summary
  Targets provided         : 6
  Duplicates removed       : 1
  Skipped (already known)  : 0
  Rejected                 : 0
  Accepted and sent        : 5
```

To use a different scan configuration:

```bash
./falcli.py scan start --config ./app/data/scan_configs/web.yaml --targets-file hosts.txt
```

By default, Falcoria skips targets that were already scanned within the project. Only new, unknown hosts are accepted.

To re-scan all targets regardless of previous results, use **replace mode**. See details [here](../import-modes/replace.md).

All available scan options can be reviewed in:

```bash
./app/data/scan_configs/all_options_example.yaml
```

Before launching a scan, check available workers:

```bash
./falcli.py workers ips
```

Example output:

```bash
[+] Fetched external IP addresses of active workers.

HOSTNAME      IP               LAST_UPDATED         LAST_UPDATED_AGO
d2b5c09fe876  134.209.200.222  2025-06-26 15:44:02  25 min ago
c21da8b747db  146.190.27.214   2025-06-26 15:44:02  25 min ago
e323a82d28d3  159.223.225.154  2025-06-26 15:44:02  25 min ago
a5ef4e44ca7b  64.225.64.155    2025-06-26 15:44:02  25 min ago

4 workers online.
```

Each worker processes one host at a time.

---

## 3. Scan Status

To check current scan status:

```bash
./falcli.py scan status
```

Example output:

```bash
[+] Scan status for project 26e73c7f-c1e3-4131-8ee5-99a01681af9f fetched successfully.

Scan Status Summary
  Tasks total    : 5
  Tasks running  : 4
  Tasks queued   : 1

Running Targets:
IP               HOSTNAMES  WORKER        STARTED_AT (UTC)     ELAPSED
142.93.156.194              a5ef4e44ca7b  2025-06-29 17:24:28  0:00:10
147.182.157.118             d2b5c09fe876  2025-06-29 17:24:28  0:00:10
143.110.223.7               e323a82d28d3  2025-06-29 17:24:28  0:00:10
165.22.231.248              c21da8b747db  2025-06-29 17:24:28  0:00:10
```

For interactive status with auto-refresh:

```bash
./falcli.py scan status -i
```

Example interactive output:

```bash
Scan status for project 'pentest_project' (26e73c7f-c1e3-4131-8ee5-99a01681af9f) fetched successfully.

Scan Status Summary
  Tasks total    : 5
  Tasks running  : 4
  Tasks queued   : 1

Running Targets:
IP               HOSTNAMES  WORKER        STARTED_AT (UTC)     ELAPSED
142.93.156.194              a5ef4e44ca7b  2025-06-29 17:24:28  0:00:10
147.182.157.118             d2b5c09fe876  2025-06-29 17:24:28  0:00:10
143.110.223.7               e323a82d28d3  2025-06-29 17:24:28  0:00:10
165.22.231.248              c21da8b747db  2025-06-29 17:24:28  0:00:10

Remaining: 5/5 | Elapsed: 5s
```

---

## 4. Stop Scan

To stop an active scan and terminate all Nmap processes:

```bash
./falcli.py scan stop
```

Example output:

```bash
[+] Scan stopped successfully for project: 'pentest_project' (26e73c7f-c1e3-4131-8ee5-99a01681af9f).
Revoked 5 tasks.
```

If some hosts were partially scanned, re-running the scan will skip already scanned hosts automatically.

---

## 5. Get Scan Results

List results:

```bash
./falcli.py project ips get
```

Download results:

```bash
./falcli.py project ips download
```

Example output:

```bash
[Active Project]: 'pentest_project' (26e73c7f-c1e3-4131-8ee5-99a01681af9f)
[+] Downloaded IPs report for project '26e73c7f-c1e3-4131-8ee5-99a01681af9f'.
Saved to: app/data/reports/26e73c7f-c1e3-4131-8ee5-99a01681af9f_ips.xml
```

---

## 6. Delete Data

To delete all scanned IPs from the project:

```bash
./falcli.py project ips delete
```

To delete the entire project:

```bash
./falcli.py project delete <uuid>
```

This operation removes project data completely from the server.

---

This represents the essential workflow in Falcoria — project setup, scanning, monitoring, retrieving results, and cleaning up.

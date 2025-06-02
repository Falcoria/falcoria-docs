# Common Workflow

This page covers the common workflow in Falcoria — from creating a project and performing scans to importing results and cleaning up data. It reflects typical steps in a penetration testing or infrastructure assessment flow.

This guide walks through the typical CLI-driven lifecycle: project setup, scanning, result inspection, and cleanup. It is based on real-world usage and helps you quickly adopt Falcoria for internal assessments or red team engagements.

Falcoria CLI supports a descriptive `--help` mechanism. You can inspect available commands and parameters with:

```bash
falcli.py --help
falcli.py <subcommand> --help
```

---

## 1. Create a Project

All scanned data in Falcoria is organized into **projects**. Each project has a unique UUID. Internally, Falcoria works with UUIDs, not names.

To create a project:

```bash
falcli.py project create pentest_example
```

Once created, the project will be stored in local **memory** (you’ll be prompted to save it — and it’s recommended, so you don’t have to enter the UUID manually later).

Memory is a local file that remembers saved project IDs and the last used project. This mechanism helps you avoid typing the UUID every time. 
To list saved projects in memory and see which one is currently active:

```bash
falcli.py memory list
```

To switch the default project used by all future commands:

```bash
falcli.py memory set-default <project_uuid>
```

> Projects themselves live on the server via **ScanLedger**, while memory is managed locally on your machine.

To list all projects stored on the server (not just in local memory):

```bash
falcli.py project list
```

---

## 2. Start a Scan

To initiate a scan for the current project:

```bash
falcli.py scan start --config scan_configs/default.yaml --targets-file hosts.txt
```

* `--config` is optional; if not set, `default.yaml` is used automatically.
* You can specify targets explicitly via `--targets-file`.

For available options:

```bash
falcli.py scan start --help
```

By specifying a config file with the `--config` parameter, you define how the scan will run — including Nmap options, service detection settings, and the import mode for results.

You can run multiple scans with different configs for different parts of the target list — all tasks will be queued and processed under the same project. This allows phased scanning, where each scan focuses on a specific protocol, range, or depth.

Scan configurations are YAML files. You can create your own, reuse existing ones, or share them across the team.

---

## 3. Check Scan Status

While the scan is running, check the real-time status interactively:

```bash
falcli.py scan status -i
```

Remove `-i` to get number of tasks in queue.

To stop the scan (removes all tasks in the queue for this project only):

```bash
falcli.py scan stop
```

---

## 4. Inspect Scan Results

### List IPs with open ports:

```bash
falcli.py project ips list
```

### View detailed results (Nmap-like output):

```bash
falcli.py project ips get
```

By default, only IPs with at least one open port are shown. To also retrieve hosts without open ports:

```bash
falcli.py project ips get --no-has-ports
```

---

## 5. Per-IP Operations

The same `get` and `delete` logic applies to a single IP:

```bash
falcli.py project ips get <ip_address>
falcli.py project ips delete <ip_address>
```

If you omit `<ip_address>`, the command applies to **all IPs** in the current project.

---

## 6. Download Results

To save the current project scan results to an XML file:

```bash
falcli.py project ips download
```

By default, the output will be saved to the `./scan_reports` directory.

---

## 7. Delete All Data

To delete **all IPs** from the project:

```bash
falcli.py project ips delete
```

To delete the entire project:

```bash
falcli.py project delete <project_uuid>
```

---

These operations represent the core workflow in Falcoria: create a project → launch a scan → check results → export or clean up.

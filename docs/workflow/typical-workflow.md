# Typical Workflow

This section demonstrates a step-by-step workflow in Falcoria, from creating a project to exporting results. Each phase includes example commands using `falcli`. Illustrations are included to show how data flows into the project canvas.

## Create a project

Before running scans, a project must be created. The project acts as a single dataset ("canvas") where results accumulate and where the team collaborates.

```bash
falcli project create test_project
```

![Canvas initialization: empty project where results will be stored](../images/workflow-canvas-init.png)

## 1. Initial scan (HTTP ports only)

Upload the initial list of targets and run a scan limited to HTTP ports.

```bash
falcli scan start --config http-only.yaml --targets-file hosts.txt
```

![Initial scan: targets resolved/deduplicated, first HTTP results added to the canvas](../images/workflow-initial-scan.png)

## 2. Adding new targets

If the target file is updated with additional hosts, Falcoria detects the difference:

- Already scanned or queued targets are skipped
- Only new entries are processed

```bash
# Example: file was updated from 2 to 3 entries
# old: host1, host2
# new: host1, host2, host3
# only host3 will be sent to scan

falcli scan start --config http-only.yaml --targets-file hosts.txt
```

![New targets: only new entries from the updated list are added to the canvas](../images/workflow-new-targets.png)

## 3. Full port scan (Append)

Expand the scan to the full port range. The **Append** mode extends the project canvas:

- Existing results remain untouched
- New scan data is added next to them
- Data from previously covered ports is not overwritten

```bash
falcli scan start --config full-range.yaml --mode append --targets-file hosts.txt
```

![Append scan: new ports appear next to existing results, previous data remains unchanged](../images/workflow-append.png)

→ See [Scan Management](../concepts/scan-management.md) for details on checking status, stopping, or resuming scans.

## 4. Rescan with Replace

Run a rescan on a specific range of ports (e.g., top-1000). The **Replace** mode updates only the selected range:

- Ports in scope are refreshed
- All other results stay unchanged
- Changes are highlighted and stored in history

```bash
falcli scan start --config top-1000.yaml --mode replace --targets-file hosts.txt
```

To get history of changes:

```bash
falcli project ips history
```

![Replace scan: only selected ports are updated, changes highlighted on the canvas](../images/workflow-replace.png)

## 5. Report download

At any time, results can be exported from the project.
Even after multiple updates, the canvas always represents a consistent, complete dataset.

```bash
falcli project ips download
```

---

👉 **Key takeaway**: In Falcoria, data from previous scans stays intact. Only the chosen targets or port ranges are updated, while the project is always available as a single, unified report.

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

If the target file is updated with additional hosts, Falcoria will skip already scanned or queued targets and process only the new ones.

```bash
falcli scan start --config http-only.yaml --targets-file hosts.txt
```

![New targets: only new entries from the updated list are added to the canvas](../images/workflow-new-targets.png)

## 3. Full port scan (Append)

Expand the scan to the full port range. The **Append** mode extends the project canvas: existing results stay untouched, new scan data is appended alongside them.

```bash
falcli scan start --config full-range.yaml --mode append --targets-file hosts.txt
```

![Append scan: new ports appear next to existing results, previous data remains unchanged](../images/workflow-append.png)

→ See [Scan Management](../concepts/scan-management.md) for details on checking status, stopping, or resuming scans.

## 4. Rescan with Replace

Run a rescan on a specific range of ports (e.g., top-1000). The **Replace** mode refreshes a chosen part of the canvas: ports in the selected range are updated, with changes highlighted and stored in history.

```bash
falcli scan start --config top-1000.yaml --mode replace --targets-file hosts.txt
```

![Replace scan: only selected ports are updated, changes highlighted on the canvas](../images/workflow-replace.png)

## 5. Report download

At any time, results can be exported from the project.

```bash
falcli project ips download
```

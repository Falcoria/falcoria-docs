# Import External Reports

Falcoria supports importing external scan results into your project scope using Nmap XML files. This allows you to use Falcoria as a centralized data store — even if you don't use workers or automated scanning.

This is handled by the **ScanLedger** component and does not require Falcoria's distributed scanning features. You can use it in offline mode, fully locally, or on a server — no RabbitMQ, Redis, or workers are needed.

## Use Case: Centralized Import System

Whether you're importing reports from your personal scans or consolidating results from teammates, ScanLedger can act as a public-facing, standalone report registry.

**ScanLedger Reference:**  
[https://github.com/your-org/scanledger](https://github.com/your-org/scanledger)

---

## How It Works

You can run:

```bash
falcli project ips import --file <report.xml> [--project-id <id>] [--mode <insert|replace|update|append>]
```

- `--file` (required): Path to your Nmap XML report.
- `--project-id` (optional): Defaults to the last used project.
- `--mode` (optional): Defaults to `insert`.

If the project is not found in memory, Falcoria will attempt to fetch it from the server and cache it locally.

---

## Import Modes Summary

A brief overview is shown below. For detailed behavior, see [Import Modes](../import-modes/index.md).

| Mode     | Description                                                                 |
|----------|-----------------------------------------------------------------------------|
| insert   | Adds new IPs and ports. Skips anything already present.                    |
| replace  | Clears all existing IPs and ports before adding new data. Destructive.     |
| update   | Updates data for already-known IPs and ports.                              |
| append   | Adds only new ports to known IPs. Skips existing ones.                     |

---

## Common Scenarios

### Insert a fresh scan

```bash
falcli project ips import --file nmap_report.xml --mode insert
```

Use this if your scan contains new IPs or ports that aren’t in the project yet.

### Replace everything with new results

```bash
falcli project ips import --file nmap_report.xml --mode replace
```

Use with caution. All existing IPs and ports in the project will be deleted before import.

### Update scan results for known IPs

```bash
falcli project ips import --file nmap_report.xml --mode update
```

This will refresh services or states (e.g., port 80 changing from closed to open).

---

## When to Use This

- You scanned something manually and want to bring the results into Falcoria.
- You're working in a restricted environment without workers or queueing.
- You’re collaborating and someone shared a scan report.
- You want to use Falcoria as a structured storage layer for IPs and ports.

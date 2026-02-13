# Getting Started

## Setup options

There are three ways to run Falcoria, depending on what you need:

**Single-node** — everything on one machine. [ScanLedger](architecture.md), [Tasker](https://github.com/Falcoria/tasker), [Worker](https://github.com/Falcoria/worker), Postgres, Redis, RabbitMQ — all via Docker Compose. Good for trying Falcoria out or running engagements from one host.

**Distributed** — components deployed on separate machines. Workers run from different network locations, each with its own IP. This is the setup for large scopes where scan speed matters.

**Data aggregation only** — just ScanLedger and [falcli](https://github.com/Falcoria/falcli). No scanning — you import reports from Nmap or other tools and use ScanLedger to merge and track them.

## Single-node setup

The quickest way to get everything running:

```bash
git clone https://github.com/Falcoria/falcoria.git
cd falcoria
./quickstart.sh
```

The script generates TLS certificates, creates credentials, starts all services via Docker Compose, and runs health checks. At the end it prints an admin token — save it, you'll need it for CLI configuration.

Ports exposed: `443` (ScanLedger API), `8443` (Tasker API).

## Installing falcli

[falcli](https://github.com/Falcoria/falcli) is the CLI client for interacting with Falcoria. After installing it, edit the profile at `./app/data/profiles/default.yaml`:

```yaml
backend_base_url: https://<scanledger_host>
tasker_base_url: https://<tasker_host>
token: <YOUR_ADMIN_TOKEN>
```

For single-node setup, both URLs point to `localhost` with the respective ports.

falcli remembers the active project, so you don't need to specify it every time. You can switch between projects with `falcli profile set-active-project`. Every command supports `--help` with detailed usage information.

## First scan

### 1. Create a project

```bash
falcli project create --name internal-net
```

A project is a persistent dataset. All scans within a project write into the same shared state.

### 2. Start a scan

```bash
falcli scan start --config scan_configs/http-only.yaml --targets-file hosts.txt
```

Targets are [deduplicated](concepts/deduplication.md) before scanning — duplicate entries, overlapping CIDRs, hostnames resolving to the same IP are all handled automatically.

### 3. Check status

```bash
falcli project scan status
```

### 4. View results

```bash
falcli project ips get
```

### 5. Export {#export}

```bash
falcli project ips download
```

Exports the current shared state as Nmap XML. This reflects everything across all scans in the project.

## Importing external reports

If you have existing Nmap XML output, you can import it into [ScanLedger](architecture.md) without running a scan:

```bash
falcli project ips import -f scan_report.xml --mode append
```

The import mode controls how incoming data merges with what's already stored. See [Import Modes](concepts/import-modes.md) for details.

This is how ScanLedger works as a standalone tool — you bring your own scan output, ScanLedger handles aggregation.

## Distributed setup

For distributed scanning, components are deployed separately. Each has its own repository:

| Component | Repository | Role |
|-----------|------------|------|
| ScanLedger | [Falcoria/scanledger](https://github.com/Falcoria/scanledger) | Shared state — stores and merges all scan data |
| Tasker | [Falcoria/tasker](https://github.com/Falcoria/tasker) | Target preparation and task distribution |
| Worker | [Falcoria/worker](https://github.com/Falcoria/worker) | Scan execution |
| falcli | [Falcoria/falcli](https://github.com/Falcoria/falcli) | Command-line interface |

ScanLedger and Tasker run centrally. Workers are deployed on separate machines — cloud VMs, VPSes, VPN endpoints — each connecting to the shared RabbitMQ and Redis. Adding workers scales scan throughput linearly.

See each repository for installation instructions.

## Next steps

- [Workflows](workflows.md) — common usage patterns across engagements
- [Concepts](concepts/index.md) — import modes, deduplication, change history, distribution

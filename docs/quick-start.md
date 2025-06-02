# Quick Start

This guide provides two streamlined ways to get started with Falcoria: a high-level automatic workflow using `fast-scan`, and a more manual, step-by-step process for full control.

> ⚙️ This guide uses [`falcli`](https://github.com/Falcoria/falcli) — Falcoria's command-line interface.  
> Make sure it’s installed and connected to a running backend before proceeding.

---

## Option 1: Fast Path with `fast-scan`

Use this when you want to scan quickly with minimal setup.

```bash
falcli fast-scan --config scan_configs/default.yaml --hosts example.com,scanme.nmap.org
```

The command above will:

* Create a new project with a random name
* Send a scan request to Tasker
* Track progress until completion
* Show scanned IPs and port summary
* Save report locally (XML by default)

You can also pass `--delete` if you want to remove the project after report download.

> Example config files can be found in the [`scan_configs`](https://github.com/Falcoria/falcli/tree/main/scan_configs) folder or created manually.

---

## Option 2: Manual Step-by-Step Control

Use this when you want explicit control over project creation, task sending, and data download.

### 1. Create Project

```bash
falcli project create --name internal-net
```

### 2. Start Scan

```bash
falcli project scan start --config scan_configs/custom.yaml --hosts example.com,scanme.nmap.org
```

### 3. Check Scan Status

```bash
falcli project scan status
```

### 4. Get Scanned IPs

```bash
falcli project ips list
```

### 5. Download Report

```bash
falcli project ips download
```

This manual workflow gives you full control over scope, mode, configuration, and report handling.

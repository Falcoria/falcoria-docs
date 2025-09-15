# Quick Start


This guide provides a manual, step-by-step process for full control when getting started with Falcoria.

> ⚙️ This guide uses [`falcli`](https://github.com/Falcoria/falcli) — Falcoria's command-line interface.  
> Make sure it’s installed and connected to a running backend before proceeding.

---

## Manual Step-by-Step Control

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
falcli project ips get
```

### 5. Download Report

```bash
falcli project ips download
```

This manual workflow gives you full control over scope, mode, configuration, and report handling.

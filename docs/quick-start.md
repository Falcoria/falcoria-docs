# Quick Start

This guide provides two streamlined ways to get started with Falcoria: a high-level automatic workflow using `fast-scan`, and a more manual, step-by-step process for full control.

---

## Option 1: Fast Path with `fast-scan`

Use this when you want to scan quickly with minimal setup.

```bash
falcli fast-scan --config scan_configs/default.yaml --hosts 192.168.1.1,192.168.1.2
```

This command will:

* Create a new project with a random name
* Send a scan request to Tasker
* Track progress until completion
* Show scanned IPs and port summary
* Save report locally (XML by default)

You can also pass `--delete` if you want to remove the project after report download.

---

## Option 2: Manual Step-by-Step Control

Use this when you want explicit control over project creation, task sending, and data download.

### 1. Create Project

```bash
falcli project create --name internal-net
```

### 2. Start Scan

```bash
falcli project scan start --config scan_configs/custom.yaml --hosts 192.168.1.1,192.168.1.2
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

---

You can switch between both approaches depending on your use case — speed and simplicity vs. precision and flexibility.

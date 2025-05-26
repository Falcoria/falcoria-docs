# Falcoria Use Cases

Falcoria supports a wide range of real-world workflows through two primary categories:

* **Scan Strategies** – how scans are executed
* **Report Handling** – how scan results are imported, enriched, or merged

This document outlines the **most essential use cases** for the MVP release.

---

## 1. Scan Strategies

### Port Sharding Across Workers

Distribute port ranges across multiple workers to parallelize scans and reduce detection by IDS/IPS.

```bash
falcli fast-scan --config ports_0-10000.yaml --hosts targets.txt
falcli fast-scan --config ports_10001-65535.yaml --hosts targets.txt
```

**Import Mode:** `append`

> ⚠️ To ensure optimal task distribution, launch the scans one by one with short delays between commands. This gives workers time to claim tasks without conflicts.

---

### Fast Scan Only (No Service Detection)

Run a lightweight scan to detect open ports quickly, skipping service detection entirely.

**Why This Matters:**

* Speeds up scanning time, especially for large scopes
* Minimizes noise to avoid detection by firewalls, IDS, and honeypots
* Allows chaining with external tools for post-processing

```bash
falcli fast-scan --config fast_ports.yaml --hosts targets.txt
```

---

### Service Detection Behavior (Default and Optional)

By default, Falcoria first discovers open ports and then performs service detection for those ports.

* You can disable service detection in the configuration file to run only the discovery phase.
* Falcoria saves open ports found during the first phase.
* If some ports are later closed (e.g., by firewall rules) during service detection, they will still be retained in the project.

---

### Offline Project Imports

Useful for air-gapped or internal environments where scan results are collected manually.

**Why This Matters:**

* Supports internal pentests or red team ops without internet access
* Integrates legacy tool output (e.g., Nmap XML)
* Still benefits from Falcoria’s deduplication and import logic

```bash
falcli project ips import --file scan.xml --mode insert
```

---

## 2. Report Handling

### Enrich Partial Results

First import open ports only, then later import banners or services to update only changed fields.

```bash
falcli project ips import --file service_scan.xml --mode update
```

**Import Mode:** `update`

---

### Replace Changed Hosts

If a rescan reveals different open ports, fully replace the corresponding host’s data.

**Why This Matters:**

* During long engagements, the network state may change frequently
* Ensures the scan data stays fresh and relevant
* Eliminates outdated results without manual cleanup


```bash
falcli project ips import --file latest_scan.xml --mode replace
```

**Import Mode:** `replace`

---

### Initial Import and Deduplication

Safely load scan results into a project. Whether importing manually or via workers, the backend ensures that no duplicate IP-port pairs are stored. This avoids redundancy when multiple team members scan the same targets.

**Why This Matters:**

* Reduces storage overhead
* Ensures clean project history
* Prevents conflicts in collaborative workflows

```bash
falcli fast-scan --hosts team1.txt --mode insert
falcli project ips import --file external_team_scan.xml --mode insert
```

**Import Mode:** `insert` or `update`

---

These core use cases define the MVP-level capabilities of Falcoria. They ensure efficient scanning, parallel execution, clean data management, and reliable collaboration.

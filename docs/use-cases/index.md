# Falcoria Use Cases

Falcoria supports structured workflows for scanning, importing, filtering, and managing scan results.  
This section documents common usage patterns and provides real-world CLI sequences for each.

Each use case reflects actual red team and recon workflows — from fast scans to controlled project management.

---

## CLI Patterns

These commands form the base of interaction:

- `create` — create new projects or scan jobs
- `list` — list projects, IPs, ports, or results
- `get` — retrieve detailed data per asset or scan
- `delete` — remove data cleanly from the system
- `help` — introspect available commands and options

---

## Scan Behavior Note

By default, Falcoria performs **open port detection first**, and then automatically **runs service scan** only on ports that are confirmed open.

- You can disable service scanning entirely if you only want to detect open ports.
- You cannot currently run only service scans on pre-specified ports without first performing port discovery.

This approach optimizes performance and minimizes noise while preserving accurate state information for import and merge operations.

---

## Scan Configs Reference

Falcoria uses YAML-based configuration files to control scan behavior.

- Use predefined configs from [`scan_configs/`](https://github.com/Falcoria/falcli/tree/main/scan_configs)
- See full option list in [`all_options.yaml`](https://github.com/Falcoria/falcli/blob/main/scan_configs/all_options.yaml)
- Short configs like `light.yaml` or `web.yaml` are available for quick targeting
- Configs can be shared, versioned, or chained across scan phases

---

## Use Cases Covered

- [Common Operations](common-operations.md)  
  Typical create/list/get/delete commands for working with projects, IPs, and ports.

- [Import External Reports](import-external-reports.md)  
  Add Nmap XML results to your project scope — no workers needed.

- [Rescan](rescan.md)  
  Trigger new scans on previously discovered IPs or ports.

- [Update Enrichment](update-enrichment.md)  
  Enrich or reclassify services with newer metadata (e.g., updated banners).

- [Port Sharding (Evasion)](port-sharding.md)  
  Use parallelized port scan ranges to bypass WAFs and reduce detection.

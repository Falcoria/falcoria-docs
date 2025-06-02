# Full Rescan

This use case demonstrates how to perform a complete rescan of the current project using **replace** mode.

Replace mode wipes all existing IPs and ports in the project and imports only the results from the new scan. This is useful when you want to fully refresh the scan results with updated data.

---

## Configuration File

Use the following configuration file to run a full scan:

```yaml
open_ports_opts:
  skip_host_discovery: true
  dns_resolution: false
  transport_protocol: tcp
  max_retries: 3
  min_rate: 1000
  ports:
    - "1-65000"

service_opts:
  aggressive_scan: true
  default_scripts: true
  os_detection: true
  traceroute: false

timeout: 1800
mode: replace
include_services: true
```

---

## How to Use

Run the scan with:

```bash
falcli scan start --config scan_configs/rescan.yaml --from-config
```

---

## Notes

This use case assumes that the current project already has some previously scanned data, such as APIs and port banners. Only in such cases will **replace** mode be used as intended — to cleanly override the existing data with new results.

⚠️ **Be careful** when using `replace` mode. It deletes all data for the project, including IPs. If an IP that previously had ports now returns no results, the old data will be completely overwritten by an empty set.

Use this mode only when you're sure you want a full reset of your scan results.

# Configurable Scans and Preset Profiles

Falcoria supports both quick one-liner scans and fully configurable scan definitions. This makes it suitable for fast on-the-fly usage as well as highly controlled, team-wide scanning workflows.

---

## Launch a Scan in One Command

If you want to start scanning immediately, use the `fast-scan` command with a default configuration:

```bash
./falcli.py fast-scan --config ./scan_configs/default.yaml
```

This launches a scan with balanced parameters that cover typical infrastructure setups.

---

## Use Predefined Scan Configurations

Falcoria includes a set of ready-to-use configuration files that you can use as-is or modify:

- `default.yaml` – general-purpose scan profile
- `web.yaml` – focuses on web-related ports
- `only_open_ports.yaml` – hides closed/filtered ports in results
- `port_sharding_1.yaml` / `port_sharding_2.yaml` – optimized for distributed scan workers
- `rescan.yaml` – forces re-scan of previously scanned targets
- `udp.yaml` – enables UDP scanning
- `update_enrichment.yaml` – used for scan enrichment or patching

Browse the full list here:  
[scan_configs](https://github.com/Falcoria/falcli/tree/main/scan_configs)

---

## Create Your Own Configuration File

You can also define your own scan parameters using a `.yaml` file. All supported parameters are demonstrated in:

- `scan_configs/all_options_example.yaml`

Example:

```yaml
min_rate: 1000
ports: "22,80,443,3306"
scan_type: "tcp"
max_retries: 1
```

Run with:

```bash
./falcli.py fast-scan --config my_scan.yaml
```

This allows you to fine-tune each scan to your project needs or infrastructure quirks.

---

## Team Usage and Preset Sharing

Configuration files can be versioned and shared across teams to ensure consistent scanning policies. This improves:

- Repeatability across environments
- Auditability of scan logic
- Team alignment on port selection, rate limits, and strategy
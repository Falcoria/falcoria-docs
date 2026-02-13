# Scan Configs

A scan config is a YAML file that defines how a scan is executed — which ports to scan, which protocols to use, and how results are processed.

## Separation of concerns

Targets define _what_ is scanned. Configs define _how_ it is scanned. This separation allows the same target list to be scanned with different configurations across phases — HTTP-only first, then full range, then service detection — without duplicating target management.

## Two-phase scanning

Each scan has up to two phases:

1. **Port discovery** (`open_ports_opts`) — finds which ports are open. Configurable: port range, protocol (TCP/UDP), rate limits, retries, timeouts.

2. **Service detection** (`service_opts`) — runs against discovered open ports only, if `include_services: true`. Configurable: aggressive scan, default scripts, OS detection.

This avoids probing closed ports for service information. Both phases are configured independently within the same YAML file.

## Config reference

A complete example with all available options and their descriptions is available at [`all_options_example.yaml`](https://github.com/Falcoria/falcli/blob/main/app/data/scan_configs/all_options_example.yaml).

## Built-in profiles

Falcoria ships with predefined configs for common scan types. Available profiles are in the [`scan_configs`](https://github.com/Falcoria/falcli/tree/main/app/data/scan_configs) directory. You can modify existing profiles or create new ones — they are plain YAML files, portable and reusable across projects and team members.

## Staged scanning

Configs enable a phased approach — start with HTTP ports, expand to full range, then run service detection. Each phase uses a different config against the same targets. See [Workflows](../workflows.md#expanding-scan-coverage) for a practical example.

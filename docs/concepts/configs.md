# Configs

In Falcoria, a *config* defines how a scan is executed.
It is a YAML file that describes scan parameters such as:

- which port ranges to scan,
- which protocols or services to target,
- which scan mode to use (append, replace, etc.),
- additional tool options.

Configs separate scan logic from target lists:

- The *targets file* tells *what to scan*.
- The *config file* tells *how to scan*.

## Examples

- `web.yaml` → scan only HTTP ports  
- `full-range.yaml` → scan the entire port range  
- `udp.yaml` → scan UDP ports

## Why configs matter

By combining different configs with the same project, teams can:

- start with lightweight scans (e.g. web ports),
- expand to deeper scans later (full range),
- rescan selected ranges to refresh data.

This separation makes scans flexible and repeatable: targets stay the same, while configs define the scanning strategy.

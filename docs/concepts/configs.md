# Configs

In Falcoria, a config defines how a scan is executed.

A config is a YAML file that describes scan behavior, including:

- which ports are scanned,
- which protocols or services are included,
- how scan results are processed.

Targets and scan behavior are defined separately:

- the targets define *what* is scanned,
- the config defines *how* it is scanned.

---

## Built-in Scan Profiles

Falcoria provides a set of predefined configs for common scan tasks.

Typical examples include:

- HTTP-only scans,
- full port range scans,
- UDP scans,
- scans that detect only open ports,
- scans that include service and banner detection.

These configs allow scans to be started without manual parameter tuning.

---

## Sharing and Reuse

Configs are designed to be reusable.

A config can be:

- reused across multiple projects,
- shared between team members,
- stored as part of a project setup.

This allows teams to standardize scan behavior and avoid reconfiguring tools for each scan.

---

## Embedded Experience

Configs in Falcoria are not just presets.

They are based on tested scan setups and practical experience gathered from repeated scan comparisons and real-world usage.
The selected parameters reflect trade-offs between speed, coverage, and reliability.

Using a config applies these tested settings directly, without requiring users to fine-tune scanner options.

---

## Practical Usage

Configs make it easy to run scans in stages.

A common workflow includes:

- starting with a lightweight scan (for example, HTTP ports),
- expanding to broader scans (full port range),
- refreshing specific parts of the scope when needed.

Targets remain the same, while configs control scan depth and behavior.

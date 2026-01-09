# Configs

In Falcoria, a config defines how a scan is executed.

A config is a YAML file that describes scan behavior, such as:

- which ports are scanned,
- which protocols or services are included,
- how scan results are processed.

Targets and scan behavior are defined separately:

- targets define *what* is scanned,
- configs define *how* it is scanned.

---

## Built-in Scan Profiles

Falcoria provides predefined configs for common scan tasks.

Examples include:

- HTTP-only scans,
- full port range scans,
- UDP scans,
- scans that detect only open ports,
- scans that include service and banner detection.

These configs allow scans to be started without manual parameter selection.

---

## Sharing and Reuse

Configs are reusable and portable.

A config can be:

- reused across multiple projects,
- shared between team members,
- stored as part of a project setup.

This helps teams keep scan behavior consistent and reduces repeated configuration work.

---

## Embedded Experience

Configs are based on tested scan setups and practical usage.

They reflect known trade-offs between speed, coverage, and reliability.
Using a config applies these settings directly, without manual tuning.

---

## Practical Usage

Configs support staged scanning.

A typical workflow includes:

- starting with a lightweight scan,
- expanding to broader scans,
- refreshing selected parts of the scope.

Targets remain the same, while configs control scan depth and behavior.

# What is Falcoria

**Falcoria** is a collaborative platform for storing and managing port scanning data, providing a single shared view of hosts, ports, and services for the entire team.
It maintains a structured dataset of discovered hosts, ports, and services, accessible to all team members.

---

## Why Falcoria

During assessments teams face challenges:

- scope targets (hostnames, IPs, CIDRs) change during the engagement
- ports open or close, services update banners or versions
- results are split across separate reports — top ports, HTTP-only, subsets of hosts — and need to be merged
- the same host may be scanned multiple times under IP, CIDR, or hostname
- difficult to track changes between scans and maintain history
- scan speed limitations — scanners hit bandwidth or rate limits, so teams adjust accuracy for speed

These issues lead to repeated work, inconsistent data, and missed hosts or ports.

### Key Features

✅ **Deduplication** — IPs, hostnames, and ports are not scanned unintentionally more than once. If two hostnames resolve to the same IP, it is scanned only once.

✅ **Single source of truth** — Each IP, hostname, and port exists as a unique entry in one dataset, available to the whole team.

✅ **Flexible updates** — Any entry can be updated or extended without affecting others. For example, you can start with HTTP ports, then add all remaining ports, or rescan the top-1000 — only selected entries change.

✅ **Change tracking** — New hosts, port state changes, and service banner updates are recorded in history.

✅ **Distributed scans** — During the scanning phase, hosts are divided between workers, and each worker scans one host at a time. This reduces bandwidth bottlenecks, avoids rate limits, and results arrive host by host.

## Who It's For

- Penetration testers working with changing scopes
- Red team operators running large-scale reconnaissance
- Security engineers maintaining an up-to-date view of exposed services

---

## Get Started

Want to see how Falcoria works in practice? Start here:  
[Common Workflow — Step-by-Step Example](use-cases/common-workflow.md)

- [Installation Guide](installation.md)  
- [Import Modes](import-modes/index.md)  
- [Architecture Overview](architecture.md)  

---

## Watch Falcoria in Action

<video width="800" controls>
  <source src="videos/falcoria_common_workflow.mp4" type="video/mp4">
  Your browser does not support the video tag. [Download Video](videos/falcoria_common_workflow.mp4)
</video>

---

## Get Early Access

If this matches your workflow, sign up here: [Early Access Form](https://forms.gle/wo2619ZKrW6irRX19)
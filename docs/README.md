# What is Falcoria

**Falcoria** is a tool for maintaining the current state of the perimeter.  
It tracks exposed ports and services as a single source of truth, no matter if the scope changes or you update it in any way.

---

## Why Falcoria

During assessments teams face challenges:

- scope targets (hostnames, IPs) change — OSINT finds new, or client changes the scope  
- ports change (open/close), services update (banner, version)  
- separate reports — one for top 1000 ports, another for HTTP only, others for small groups of hosts, with the need to merge and diff
- repeated rescans or manual checks — the same hosts get scanned more than once under IP, CIDR, or different hostnames
- scan speed limitations — scanners hit bandwidth or rate limits, so teams often sacrifice accuracy for speed

This leads to repeated scans, manual double checks, longer scan times, and missed hosts or ports.

### Key Features

✅ **Deduplication** — IPs, hostnames, and ports are not scanned unintentionally more than once. If two hostnames resolve to the same IP, it is scanned only once.

✅ **Single source of truth** — Each IP, hostname, and port exists as a single unique entry in one report, available to the whole team.

✅ **Flexible updates** — Each IP and port entry can be extended, updated, or replaced without affecting others. For example, you can start with HTTP ports, then add all remaining ports, and later rescan the top-1000 — only selected entries change, others remain the same.

✅ **Change tracking** — New hosts, port state changes, and service banner updates are stored in history.

✅ **Distributed scans** — During the scanning phase, hosts are divided between workers, and each worker scans one host at a time. This reduces bandwidth bottlenecks, avoids rate limits, and results arrive host by host.

## Who It's For

- Penetration testers working with dynamic scopes  
- Red team operators running large-scale reconnaissance  
- Security engineers maintaining a current view of exposed services for their team  

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
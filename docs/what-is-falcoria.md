# Introduction to Falcoria

**Falcoria** is a distributed scanning and coordination platform built for penetration testers and red teams. It automates host discovery, port scanning, and result collection across multiple machines, enabling efficient recon at scale while avoiding duplicated effort.

---

## Core Advantages

### Speed Through Distributed Scanning

Falcoria distributes scans across unlimited workers. Add 10 workers — it runs \~10× faster. Scaling is horizontal, not capped.

### High Accuracy by Design

Falcoria performs full scans with full output — no missed ports, no lost banners. Unlike superficial scanners, it never sacrifices detail for speed.

### No Duplication — Runtime and Storage-Level

Falcoria prevents accidental rescans and duplicate results through Redis locks and import modes. You won’t scan the same IP twice — or store it twice.

### Evasion Capabilities — Port Sharding

Falcoria supports port sharding, allowing you to split port scans across workers. This reduces noise and helps evade detection in monitored environments.

### CLI-First & Declarative Scanning

Falcoria is built around a CLI-first workflow. Scan configurations are defined in clean YAML files — easy to version, reuse, and share. This brings clarity and control to your recon — without relying on GUIs or brittle shell scripts.

### API-Native by Design

Everything in Falcoria is powered by documented APIs. You can automate every step — from project creation to scan execution and result download — or seamlessly integrate Falcoria into your own systems.

---

## Why Falcoria Exists

Falcoria was built to fix the broken state of recon workflows: untracked scans, duplicated effort, and incomplete results. We wanted a scanner that’s fast, reliable, automatable — and actually scales.

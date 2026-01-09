# What is Falcoria

Falcoria is a system for team-based network scanning for large and dynamic scopes.
Each scan run updates a shared map of hosts, ports, and services used by the entire team.

---

Falcoria centralizes network scanning work and treats scans as state updates rather than standalone outputs.
It solves two core problems: the speed of data collection and the consistency in how scan data is stored and shared.

This is achieved through two core parts:

- **Scan execution** — responsible for collecting scan data for large and dynamic scopes  
- **Data aggregation** — responsible for merging fragmented scan runs into one consistent network state  

---

## Scan Execution

This module handles scan execution for large and dynamic scopes, addressing two core constraints: execution speed and network load.

---

### Core mechanisms

- **[Distributed scanning](concepts/distribution)**  
  Tasks are executed across multiple workers, reducing total scan time proportionally to the number of active workers.

- **[Target deduplication](concepts/deduplication)**  
  Four built-in deduplication mechanisms prevent duplicate targets and redundant network requests before execution starts.

- **[Optimized scan configurations](concepts/configs)**  
  Pre-tuned scanning profiles, selected through 5000+ empirical tests, provide a reliable baseline for speed and accuracy.

---

### Results

- **Speed**: Scan execution completes **10×–100× faster** compared to single-node scanning.
- **Lower network impact**: Eliminating redundant requests reduces overall traffic and makes large scans less disruptive for the target network.
- **Reduced blocking risk**: Lower request volume and reduced scan noise decrease the likelihood of triggering rate limits or security controls.

Detailed performance data and test methodology are documented separately.

→ **Benchmarks**

---

## Data Aggregation

This module addresses the problem of fragmented scan data and loss of context in team-based workflows.  
Scan results are applied incrementally to a shared network state.

---

### Core mechanisms

- **State-based data model**  
  Scan data is stored as a single shared network state composed of unique records.  
  Duplicate entries across reports (hosts, ports, services) are merged automatically, keeping one current view of the network available to the entire team.

- **[Order-independent updates](concepts/import-modes)**  
  Scan results can be applied in any order.  
  Four import modes define how new scan data is merged into the existing state.  
  For example, extending a scan from 80 ports to 1,000 adds only newly discovered ports.

- **[Change tracking](concepts/track-history)**  
  Changes to ports and services are recorded whenever new data is applied.  
  The history logs what changed and when, including updates to port state, service, and service banner data.

- **API and export access**  
  Aggregated scan data is available via an API and standardized export formats, including Nmap XML and JSON.  
  This allows teams to retrieve a unified network view and integrate it into existing tools, automation, and reporting pipelines.

- **CLI-based data exploration**  
  Scan data can be explored using a dedicated CLI, providing structured output and controlled navigation through large result sets.

---

### Results

- **Single shared dataset**  
  Scan results are kept in one place, removing the need to manually merge reports or exchange files.  
  The current state can still be exported as Nmap XML or accessed via API for use in existing tools.

- **Continuity over time**  
  Data remains usable across repeated scans and scope changes, supporting both long-running engagements and rapidly changing environments.

- **Focused change tracking**  
  Users can quickly see what changed since the last scan and focus only on new or modified ports and services instead of rechecking the entire dataset.

- **Shared team context**  
  Everyone on the team works with the same up-to-date network view, eliminating confusion about which results are current.

## Who It's For

- Penetration testers working with large or frequently changing scopes
- Red team operators performing repeated network discovery
- Security engineers maintaining a current view of exposed hosts, ports, and services

---

## Get Started

To understand how Falcoria is used in practice, start here:  
[Common Workflow — Step-by-Step Example](workflow/typical-workflow)

- [Installation Guide](installation)  
- [Import Modes](concepts/import-modes)
- [Architecture Overview](architecture)  

---

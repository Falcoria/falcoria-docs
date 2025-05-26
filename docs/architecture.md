# Architecture Overview

Falcoria is a distributed scanning platform composed of modular services. Each part plays a specific role, ensuring scalable and consistent scanning across large infrastructure.

---

## Core Components

* **CLI (falcli)**  
  Command-line tool used to launch scans and retrieve results via API.

* **Tasker (API)**  
  Coordinates scan requests. Validates input, deduplicates targets, associates scans with a project, and queues scan tasks.

* **Worker**  
  Executes scan jobs using Nmap. Supports parallel execution and horizontal scaling.

* **Scanledger (API)**  
  Stores scan results per project. Provides endpoints for result retrieval, metadata access, and importing external scan data.

* **Redis**  
  Tracks runtime scan state and enforces deduplication during task preparation and execution.

* **RabbitMQ**  
  Message queue used to distribute scan tasks from Tasker to Workers.

---

## System Diagram

```text
+--------+       +---------------+        +------------+        +-----------+
| falcli | ────► |  Tasker (API) | ─────► | RabbitMQ   | ─────► |  Worker   |
+--------+       +---------------+        +------------+        +-----------+
      ▲                                                                |
      │                                                                |
      │                                                                ▼
      └───────────────────────────────────────────────────►+-------------------+
                                                           | Scanledger (API)  |
                                                           +-------------------+
```

---

## Scan Workflow

1. User runs `falcli` with a list of targets and optional scan configuration.
2. CLI sends the request to Tasker via API.
3. Tasker validates input, assigns or uses an existing project ID, applies deduplication, and prepares the scan job.
4. Tasker sends the job to the RabbitMQ queue.
5. A Worker receives the task and executes the scan using Nmap.
6. Worker sends scan results to Scanledger.
7. User retrieves results from Scanledger using `falcli`.

---

## Scalability

* Workers can be added or removed independently.
* Each Worker processes tasks in parallel.
* There is no hard limit on the number of Workers in the system.

---

## Extensibility

Falcoria is designed with modularity and chaining in mind. Future extensions may include:

* Tool chaining (e.g., Nmap → Nuclei)
* Customizable workflows and conditional task execution
* Configurable scan templates with predefined logic

# Architecture

Falcoria separates **scan execution** from **data aggregation**.

Scan execution and data aggregation are implemented as independent API services.
All interaction with core components is performed through their APIs.
Internal state and storage are not accessed directly.

<!-- Architecture diagram -->
![Architecture overview](images/architecture.png)

---

## Core Domains

### ScanExecution

ScanExecution is responsible for running scans.

It consists of:

- **Tasker**
- **Queue**
- **Workers**

Tasker schedules scan execution.
It accepts scan requests, splits them into execution tasks, and publishes them to the queue.

Each task targets a single host or IP with a defined port set.

Workers consume tasks from the queue and execute scans independently.
Workers do not share state.

ScanExecution scales horizontally by adding workers.

---

### DataAggregation

DataAggregation is responsible for aggregating scan results and maintaining shared scan state.

It consists of:

- **ScanLedger**

ScanLedger collects results produced by workers and merges them into a single network view.
It encapsulates its internal storage and exposes aggregated data through its API.

ScanLedger is the single source of truth for:

- hosts
- IP addresses
- ports
- services
- scan state and history

---

## Data Flow

### Scan execution

1. A scan is started via **falcli**.
2. The request is sent to **Tasker**.
3. Tasker creates execution tasks.
4. Tasks are published to the queue.
5. Workers execute tasks.
6. Results are submitted to **ScanLedger**.

### Result access

- **falcli** retrieves aggregated scan data from **ScanLedger**.

---

## Execution Model

- Execution is task-based.
- Tasks are independent.
- Scanning is performed against IP addresses.

If a hostname is provided, it is resolved before execution.
Scanning always targets IP addresses, while hostnames are preserved as metadata and associated during aggregation.

---

## Key Properties

- Scan execution and data aggregation are decoupled.
- Execution scales without changing data semantics.
- Aggregation is centralized and deterministic.

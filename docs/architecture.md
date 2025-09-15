# Architecture

Falcoria is built as a set of components that work together to manage and update port scanning data.

![System Diagram](images/architecture.png)

---

## Components by Layer

### Storage — ScanLedger

The central database. Stores projects, IPs, hosts, ports, and results.  
Implements deduplication and history tracking when new data is added or updated.

### Coordination — Tasker

The service that creates scan tasks and places them into queues.  
Handles distribution logic so multiple workers can process tasks in parallel.

### Execution — Workers

Workers perform scans. Each worker picks tasks from the queue, runs the scan, and sends results back to ScanLedger.

### Access — CLI (falcli)

The interface for users. Provides commands to create projects, run scans, import results, and view data.

---

## Notes

- All results are consolidated in ScanLedger.  
- Distribution is achieved through Tasker and Workers.  
- Deduplication and history tracking are applied automatically during updates.  

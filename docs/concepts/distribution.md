# Distribution

Distributed scanning in Falcoria is designed to increase scan speed on large scopes by splitting tasks across multiple workers.  
The key limitation in large-scale scanning is **network bandwidth**. Distribution bypasses this limitation by scaling horizontally.

---

## Why Distribution Matters

- A single machine is limited by bandwidth and latency.  
- Faster scans often reduce accuracy when done on one system.  
- Distribution allows multiple workers to scan in parallel, keeping accuracy while reducing time.  
- More workers = faster scans.  

---

## How It Works

1. The project scope is split into individual tasks (one host, one IP).  
2. Tasks are placed into a queue.  
3. Workers pick tasks from the queue and run scans in parallel.  
4. Results are collected in **ScanLedger**.  
5. The CLI retrieves consolidated results from ScanLedger.  

[IMAGE PLACEHOLDER: Insert diagram here showing scope split into tasks, queue, and workers consuming tasks]

---

## Notes

- Distributed scanning keeps results identical to local scans — only speed changes.  
- It can be combined with [Deduplication](deduplication.md) to avoid rescanning targets.  
- With import modes, distribution can also help bypass rate limits by splitting large port ranges across workers when needed.  

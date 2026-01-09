# Distribution

Distribution is the execution of scan tasks across multiple parallel workers in Falcoria.

Its purpose is to increase available throughput and reduce total scan time.

---

## Why It Is Used

Faster scans are important in two cases:

- **Large scopes**  
  Faster execution allows teams to start analysis and follow-up tasks earlier.

- **Dynamic scopes**  
  When a scope changes frequently, faster scans make it possible to rescan the entire scope often enough to track changes.

Measured behavior and detailed analysis are described in the performance article.  
[Link to article]

---

## Behavior

- Scan tasks are distributed across available workers.
- Adding workers can reduce total scan time.
- Throughput increases until limited by network bottlenecks or target capacity.

Observed scaling behavior is discussed in the performance article.  
[Link to article]

---

## Related Mechanisms

Distribution is used by other execution mechanisms:

- **Port Sharding**
- **Deduplication**
- **Import Modes**

These mechanisms are described in their own sections.

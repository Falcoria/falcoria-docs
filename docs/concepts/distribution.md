# Distribution

Distribution is the execution of scan tasks across multiple parallel workers in Falcoria.  
It increases available throughput and reduces total scan time.

---

## When Distribution Is Needed

Faster scans are important in two cases:

- **Large scopes**  
  Faster execution allows teams to start analysis and follow-up tasks earlier.

- **Dynamic scopes**  
  When a scope changes frequently, faster scans make it possible to rescan the entire scope often enough to track changes.

Measured behavior and scaling limits are described in the performance article.  
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

These mechanisms are described in their own sections.

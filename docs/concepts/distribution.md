# Distribution

Distribution is how Falcoria runs scans using multiple workers.

It allows scans to complete faster without losing accuracy when scope size grows or changes frequently.

---

## Why Distribution Matters

When scanning from a single machine, there are only two options:

- scan slowly and keep accuracy,
- scan faster and miss data.

For large scopes, this becomes a problem.
For scopes that change frequently, slow scans make it impossible to track changes in time.

Distribution solves this by spreading the work across multiple workers.
Each worker scans a smaller part of the scope at a safe speed.

---

## Why This Is Important

Distribution is useful in two common cases.

**Large scopes**  
When the scope contains many hosts or ports, a single worker takes too long to finish.
Distribution reduces total scan time by running parts of the scan in parallel.

**Dynamic scopes**  
When the scope changes often, slow scans mean changes are detected too late.
Distribution allows scans to run frequently enough to keep the network state up to date.

---

## How It Works in Falcoria

Distribution follows the standard Falcoria execution flow:

1. A scan is started via `falcli` or the API.
2. **Tasker** splits the scope into execution tasks.
3. Tasks are assigned to available **Workers**.
4. Each **Worker** runs a normal scan for its assigned tasks.
5. Results are sent to **ScanLedger** and merged into the shared state.

Execution runs in parallel.
Aggregation remains centralized.

---

## What It Enables

- Less time to complete scans for large scopes.
- Ability to rescan large and dynamic scopes frequently and detect changes early.
- Full coverage without missing hosts or ports.

Each worker behaves the same way as a single-worker scan.
Distribution only changes how many workers are used.

---

## Practical Notes

- Adding workers helps until a shared limit is reached (for example, the target’s network capacity).
- Using a single worker is a valid setup and works like a traditional scanner.
- Worker placement affects speed. Workers closer to targets usually perform better.

---

## Related Mechanisms

Distribution is used by other Falcoria features:

- **Port Sharding:** Split port ranges across workers.
- **Deduplication:** Avoid scanning targets that already exist in the state.
- **Import Modes:** Control how new results are merged with existing data.

These are described in their own sections.

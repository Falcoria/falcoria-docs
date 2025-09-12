
# Distributed Scanning
# Distributed Scanning
---

## Why Distributed Scanning Matters

Traditional perimeter scans are limited by:

- The number of machines the team can use, and the manual effort needed to merge results.
- Network bandwidth and latency limits — or losing accuracy when trying to scan too fast.

Distributed scanning helps overcome these limits by increasing effective network bandwidth while keeping full scan accuracy.

---

## When to Use Distributed Scanning

Use distributed scanning when:

- You are scanning a large perimeter (hundreds or thousands of IPs).
- You want to reduce total scan time by a factor of 10 or more — from days to hours or minutes.
- You want to collect all scan results in one place, fully consolidated.
- You want to run scans from machines closer to specific targets to reduce latency and improve efficiency.

---

## Behavior Summary

The process of a distributed scan in Falcoria looks like this:

- The project scope is split into individual scan tasks.
- Each scan task represents one Nmap scan of one IP with specific scan parameters.
- Scan tasks are distributed to available scanner workers.
- Each worker performs its assigned scans and pushes results to ScanLedger.
- The CLI retrieves consolidated results from ScanLedger when requested.

---

## Notes

- Distributed scanning is safe — each scan task runs exactly as it would locally on a single machine.
- Scan accuracy is preserved — results are identical to standard Nmap output.
- Speed gains depend on the number of workers and the size of the target perimeter.

---

## Example

Starting a distributed scan:

```bash
./falcli.py scan start --targets-file targets.txt
```

Output:

```
Scan initiated: 200 targets, 8 workers active. Processing started.
```

Retrieving scan results:

```bash
./falcli.py project ips list
```

---

## Try It Yourself

Step-by-step distributed scan example on GitHub.

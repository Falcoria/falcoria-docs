# Benchmarks

This page summarizes measured scan performance results used by Falcoria.

Detailed methodology, raw data, and test scripts are documented separately in the research article:
→ *Nmap vs Masscan vs Rustscan: Myths and Facts* (Medium)

---

## Summary

The tests focus on open port discovery under realistic conditions:

- hundreds to thousands of targets
- stable and unstable networks
- accuracy ≥ 99%

The key finding is that architecture and network placement matter more than the scanner itself.

---

## Time to Scan 1,000 Targets

Estimated scan time for 1,000 hosts using stable configurations:

| Setup | Time |
|------|------|
| Nmap (home, default) | 32h 16m |
| Nmap (home, tuned) | 4h 56m |
| Masscan (home) | 5h 57m |
| Rustscan (home) | 54h 42m |
| Nmap (cloud → cloud) | 1h 12m |
| Masscan (cloud → cloud) | 1h 15m |
| Rustscan (cloud → cloud) | 1h 08m |
| Distributed (4 nodes) | 22m 25s |
| Distributed (10 nodes) | 8m 58s |

---

## Key Observations

- Single-host scans hit network limits quickly.
- Parallel scans on one machine do not provide meaningful gains.
- Placing scanners in the same cloud as targets improves speed by ~30%.
- Distributed scanning scales close to linearly until target-side limits are reached.

---

## Why This Matters for Falcoria

Falcoria is designed around these constraints:

- Distributed execution across independent network paths.
- Reliable scan configurations instead of aggressive rates.
- Central aggregation of results into a single shared state.

Benchmarks are used to validate these design decisions, not to compare tools in isolation.

---

## References

- Full research article (methodology and raw data)
- Cloud-to-cloud benchmarks
- Home-to-cloud benchmarks
- Distributed scan benchmarks
- Extrapolation scripts

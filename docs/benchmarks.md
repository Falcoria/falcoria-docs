# Benchmarks

Performance data for open port discovery across different scanning setups. The key finding: architecture and network placement matter more than the scanner itself.

Detailed methodology, raw data, and test scripts are in the research article:
[Nmap vs Masscan vs Rustscan: Myths and Facts](https://medium.com/@2s1one/nmap-vs-masscan-vs-rustscan-myths-and-facts-62a9b462241e)

## Time to scan 1,000 targets

| Setup | Duration |
|---|---|
| Nmap (home network, default settings) | 32h 16m |
| Nmap (home network, tuned settings) | 4h 56m |
| Nmap (cloud → cloud) | 1h 12m |
| Distributed, 4 workers | 22m 25s |
| Distributed, 10 workers | 8m 58s |

## Observations

**Single-host limits.** A single scanner hits network constraints quickly. Running multiple scans on one machine provides negligible gains — the bottleneck is the network path, not CPU or memory.

**Network placement.** Cloud-to-cloud scanning is roughly 30% faster than scanning from a home connection to cloud targets. The difference comes from lower latency and higher bandwidth between cloud networks.

**Distributed scaling.** Distributing across workers scales nearly linearly. 4 workers are roughly 4x faster than one; 10 workers roughly 10x. The limit is reached when target-side rate limiting or network saturation becomes the bottleneck.

**Scanner choice.** With proper configuration, differences between Nmap, Masscan, and RustScan are marginal for most pentest setups. Configuration and architecture account for the meaningful differences.

## How this shaped Falcoria

These results drove the architecture:

- Distributed execution across independent network paths — adding machines helps, tuning a single scanner has diminishing returns
- Predefined scan configs that balance speed and accuracy based on tested conditions
- Central aggregation into one shared state — results from all workers merge automatically

## References

- [Full research article](https://medium.com/@2s1one/nmap-vs-masscan-vs-rustscan-myths-and-facts-62a9b462241e) — methodology and raw data
- [Cloud-to-cloud benchmarks](https://github.com/2S1one/netscan-benchmarks/tree/main/cloud-to-cloud)
- [Home-to-cloud benchmarks](https://github.com/2S1one/netscan-benchmarks/tree/main/home-to-cloud)
- [Distributed scan benchmarks](https://github.com/2S1one/netscan-benchmarks/tree/main/distributed-scan)
- [Extrapolation scripts](https://github.com/2S1one/netscan-benchmarks/tree/main/extrapolation)

# Evasion: Port Sharding

Port sharding is a technique used to evade detection systems and increase scan throughput by splitting the full port range across multiple scan tasks.

This is especially effective when the scanning platform distributes tasks to different workers — each scanning a distinct range of ports.

---

## Sharding Setup

Two config files are used to implement sharding:

* `port_shard_1.yaml` — contains ports from 1 to 10,000
* `port_shard_2.yaml` — contains ports from 10,001 to 65,535

Example usage:

```bash
falcli scan start --config scan_configs/port_sharding_1.yaml
falcli scan start --config scan_configs/port_sharding_2.yaml
```

Run both commands in quick succession to distribute scanning load across different workers.

---

## Notes

* These configs use **append** mode to preserve existing data.
* Avoid using `replace` mode unless you intend to fully wipe and reimport.
* **Be careful with `min_rate`** — overly high values (like 10,000) can flood networks or trigger defenses.
* This tactic is best suited for red team or stealth scanning scenarios.

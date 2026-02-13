# Change History

Change history tracks modifications to port state, service, and banner information between scan runs.

## What is recorded

A history entry is created when a rescanned port's attributes change:

- **Port state** — e.g., open → closed
- **Service** — detected service changed
- **Banner** — application version or banner string updated

Only attributes that were actively rescanned and changed are logged. Ports not included in a scan retain their previous values — no history entry is created for them.

## How it works

When scan results are imported into [ScanLedger](../architecture.md), incoming data is compared against the existing shared state for the project. For each rescanned target, any detected change is recorded with a timestamp.

Unscanned ports and services remain static.

![Change history](../images/history.png){ width="700" align=center }

## Why it matters

On a large scope scanned repeatedly, most data stays the same between runs. Reviewing full scan output to find what changed is not practical at scale.

History surfaces the differences: a new port appeared, a service switched, a banner updated — without reviewing full scan output.

## Disabling history

History tracking can be disabled per scan or import. This is useful when a scan is expected to produce redundant changes — for example, rescanning with a broader port range where previously found ports will appear again without meaningful differences.

## Viewing history

```bash
falcli project ips history
```

History entries show what changed, when, and on which host/port.

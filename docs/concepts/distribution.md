# Distribution

Distribution splits scan tasks across multiple workers running on separate machines.

## When it helps

**Large scopes** — scanning hundreds or thousands of targets on a single machine takes hours or days. Distributing across workers reduces total scan time proportionally.

**Dynamic scopes** — when the scope changes regularly, faster scanning allows frequent rescans to track changes.

## How it works

Workers consume tasks from a shared queue independently. Each worker runs on its own machine with its own network path and IP address. See [Architecture](../architecture.md) for how the components fit together.

![Distribution](../images/distribution.png){ width="700" align=center }

## Why it's effective

The bottleneck in scanning is the network path, not the scanner itself. A single machine is limited by its bandwidth and rate limits imposed by the target network.

Multiple workers bypass this by scanning from independent network paths. Each worker stays within rate limits individually; combined, they cover the scope faster.

Throughput scales roughly linearly: 4 workers are roughly 4x faster, 10 workers roughly 10x. The limit is reached when target-side rate limiting or network saturation becomes the bottleneck.

See [Benchmarks](../benchmarks.md) for measured performance data.

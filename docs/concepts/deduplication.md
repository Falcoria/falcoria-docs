# Deduplication

Deduplication ensures each target is scanned only once. It operates at multiple stages across [Tasker](../architecture.md) and [ScanLedger](../architecture.md).

## Why it matters

Target lists often contain duplicates — the same host under different names, CIDRs overlapping with individual IPs, overlapping scopes from different team members. Without deduplication, the same target gets scanned multiple times, wasting time and adding load on the target network.

## Target deduplication

### 1. String duplicates

Identical entries in the target list are removed. Each entry is normalized for comparison: CIDRs are expanded to their first host address, IPs are canonicalized (leading zeros removed), hostnames are compared as-is.

### 2. Resolution and IP-level unification

After string deduplication, all entries are resolved into IP addresses:

- CIDRs are expanded into individual host IPs
- Hostnames are resolved via DNS (IPv4, with retries on failure)
- When multiple hostnames resolve to the same IP, they are collapsed into a single target. The resolved IP becomes the key, all originating hostnames are kept as metadata.

If `single_resolve` is enabled, only the first resolved IP per hostname is used — useful for CDN cases where one hostname resolves to many IPs.

![Deduplication](../images/deduplication_1.png){ width="700" align=center }

## System-level deduplication

### 3. Skipping already stored targets

Targets already present in ScanLedger for the current project are excluded from scanning. This includes hostnames that resolve to an already known IP. If an excluded target carried new hostnames, those hostnames are still merged into the existing record without triggering a new scan.

This applies when using [Insert](import-modes.md#insert) mode. Other modes rescan existing targets to update their data.

### 4. Queue deduplication

Targets already queued for the current project are skipped. This is checked both before dispatching and immediately before sending each task, to handle race conditions between concurrent scan requests.

## Effect

The result: raw target lists with duplicates, overlapping ranges, and mixed hostnames are reduced to a set of unique targets that haven't been scanned yet. Team members can submit overlapping scopes without coordination — duplicates are filtered automatically.

In practice, host deduplication alone provided ~20% reduction in one scenario and nearly 50% in another. See [Scan Less, Find More: DNS Deduplication for Large Scopes](https://medium.com/@2s1one/scan-less-find-more-dns-deduplication-for-large-scopes-efbe1cdf57e9) for measured examples.

# Track History

Falcoria supports update enrichment to keep scan results current and accurate. The update mode allows you to enrich existing scan data with new ports, updated banners, or improved service information, without deleting previous results.

---

## Update Enrichment

Use this mode when you want to enrich existing scan results with new data, such as additional ports, updated banners, or service info. The `update` mode does not delete existing data — it only adds or refreshes what’s newly discovered.

### Behavior

- Keeps existing IPs and ports.
- Updates services, banners, and metadata if improved information is discovered.
- Adds new open ports that weren’t previously present.
- Does not remove or overwrite existing data unless newer values are found.

### Use Case

You’ve already scanned an infrastructure and now want to:

- Improve service detection with more aggressive settings
- Refresh outdated banner info
- Update open port set with additional targets or new exposure

This is a safe mode to run multiple times without losing data.

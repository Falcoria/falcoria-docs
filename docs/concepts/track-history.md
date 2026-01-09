# History Tracking

Falcoria records changes to port state, service, and banner data when new scan results update the shared network state.

---

## What Is Recorded

A history entry is created for a port when one of its attributes changes:

- **Port State** — for example, from `open` to `closed`.
- **Service** — the detected service on the port.
- **Banner** — application banner or version string.

History is generated only for attributes that were re-scanned and changed.
Ports that were not included in a scan retain their previous state.

---

## How It Works

When scan results are imported, the system compares the new data against the existing network state stored in **ScanLedger**.

For scanned targets, detected differences are written to the history log with a timestamp.
Ports and services that were not part of the scan remain unchanged.

The history log is available through the API and the `falcli` command-line client.

---

## Why This Matters

- On large scopes with hundreds of IPs and many ports, rescans can produce large result sets.
- History highlights only what changed, so teams know where to focus attention.
- This makes follow-up checks faster and reduces the risk of missing important changes.

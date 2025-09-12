# History Tracking

Falcoria keeps track of changes between scans.  
This is useful when working with large scopes, where manually spotting differences is nearly impossible.

---

## What Is Recorded

For each port, history is written only when existing data changes:

- **State** — e.g., from `open` to `closed`.  
- **Service** — detected service on the port.  
- **Banner** — application banner or version string.  

---

## Why This Matters

- On large scopes with hundreds of IPs and many ports, rescans can produce huge result sets.  
- History highlights only what changed, so teams know exactly where to focus attention.  
- This makes follow‑up checks faster and ensures important changes are not missed.

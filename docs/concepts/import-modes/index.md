# Import Modes in Falcoria

Import modes are the **heart of Falcoria’s scan management system** — giving you full control over how scan data is ingested, updated, and preserved.  
They apply equally to **automated scan results** (e.g. scans) and to **manual imports** (e.g. from Nmap XML reports).  
They ensure consistency, eliminate duplicates, and support workflows like incremental enrichment or authoritative replacement.

---

## Quick Access

- [`insert` Mode](insert.md) – [Example](https://github.com/Falcoria/falcoria-use-cases/tree/main/import-mode-insert)
- [`replace` Mode](replace.md) – [Example](https://github.com/Falcoria/falcoria-use-cases/tree/main/import-mode-replace)
- [`append` Mode](append.md)
- [`update` Mode](update.md)

---

## Summary Table

| Mode      | What it Does                                                  | Primary Use Case                                           |
| --------- | ------------------------------------------------------------- | ---------------------------------------------------------- |
| `insert`  | Adds new IPs only; skips if they exist                        | Importing multiple partial scans safely without risk of duplication |
| `replace` | Deletes and replaces all matching IPs and ports               | Overwriting outdated scan results with fresh authoritative data     |
| `append`  | Adds new ports to existing IPs; does not update existing ones | Combining distributed or parallel scans into one dataset            |
| `update`  | Updates only matching ports; preserves everything else        | Enriching scan data incrementally (e.g. banners, versions)          |

---

## When to Use Each Mode

Each import mode exists to support a specific type of workflow. Here’s how to decide:

- **Insert** → _“I don’t want to mess up what’s there; just add new stuff.”_  
  Useful when importing scan chunks safely without affecting existing results.

- **Replace** → _“I want to start over for this host.”_  
  Clears out stale or incorrect data and replaces it completely.

- **Append** → _“This is more data for the same host — don’t touch what’s already known.”_  
  Designed for phased scanning or port sharding across teams or tools.

  ```{toctree}
  :maxdepth: 1

  insert.md
  replace.md
  append.md
  update.md
  ```

- **Update** → _“Let’s improve the quality of the scan details, not the structure.”_  
  Keeps the structure intact but adds more detail where available.
---

**Note:** All import modes will add new IP addresses that don’t already exist in the project — this behavior is consistent across `insert`, `replace`, `append`, and `update`.

---


Use these modes to control how data enters Falcoria and to design scanning workflows that match your infrastructure and goals.

# Import Modes

Import modes define how new scan results are merged with existing data in ScanLedger.  

---

## Insert

- **Insert** — Adds only new IP addresses.  
  Existing IPs and their ports are never modified.

---

## Port Update Modes

All other modes add new IPs and all new ports they provide.  
The difference is only in how they handle ports that already exist for the same IP.

- **Append** — Leaves existing ports untouched. Only new ports are added.  
- **Update** — Updates data for existing ports (state, banner, service) but never deletes them.  
- **Replace** — Updates existing ports and may also remove them (for example, if a port was open and is now closed).  

---

## Available Import Modes

- [`insert` Mode](insert.md) – [Example](https://github.com/Falcoria/falcoria-use-cases/tree/main/import-mode-insert)  
- [`replace` Mode](replace.md) – [Example](https://github.com/Falcoria/falcoria-use-cases/tree/main/import-mode-replace)  
- [`append` Mode](append.md)  
- [`update` Mode](update.md)  

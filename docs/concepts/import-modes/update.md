# Update Mode

The **Update** mode adds new IPs and ports, and updates existing ones when their state, banner, or service changes.  
Existing data is never removed.

---

## Behavior

- If an IP does not exist in the project → it will be added with its ports.  
- If an IP exists →  
  - new ports are added,  
  - existing ports are updated if state, banner, or service differs,  
  - no ports are deleted.  

**Image placeholder:** canvas showing dataset before and after → existing ports keep their place, only fields updated.

---

## When to Use

Use Update when you want to refine or enrich results without losing data, for example:  

- Adding results from a scan with version or banner detection.  
- Combining results from different tools for the same targets.  
- Keeping track of changes while preserving all existing data.  

---

## Example

```bash
falcli project ips import --file report_update1.xml --mode update
```

---

## Reference

- [Practical Example on GitHub](https://github.com/Falcoria/falcoria-use-cases/tree/main/import-mode-update)

# Append Mode

The **Append** mode adds new ports to existing IPs without modifying existing ones.  
It is useful when combining results from multiple scans or phases.

---

## Behavior

- If an IP does not exist in the project → it will be added with its ports.  
- If an IP exists → new ports are added, existing ports stay unchanged.  
- Existing fields (state, banner, service) are never updated or removed.  

**Image placeholder:** canvas showing dataset with IP and ports → new ports added while existing remain unchanged.

---

## When to Use

Use Append when you want to extend data without affecting existing results, for example:  

- Combining partial results from different port ranges.  
- Running parallel workers to cover large scopes faster.  
- Adding data from additional scan phases (e.g. UDP, slow services).

---

## Example

```bash
falcli project ips import --file report_append1.xml --mode append
```

---

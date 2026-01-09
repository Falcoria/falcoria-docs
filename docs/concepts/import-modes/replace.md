# Replace Mode

The **Replace** mode imports new results and overwrites existing ports for matching IPs.  
Ports not included in the new scan remain unchanged.

---

## Behavior

- If an IP does not exist in the project → it will be added with its ports.  
- If an IP exists → ports from the new report replace existing ones for that IP.  
- Ports not present in the new report are removed only if they were explicitly included and marked as closed.  

**Image placeholder:** canvas showing dataset before and after → updated ports overwrite old ones.

---

## When to Use

Use Replace when you want to refresh data for specific IPs and overwrite outdated port states, for example:  

- Rescanning an IP with a different port range.  
- Correcting results after a failed or partial scan.  
- Ensuring only the latest scan data is kept for those IPs.  

---

## Example

```bash
falcli project ips import --file report_replace1.xml --mode replace
```

---

## Reference

- [Practical Example on GitHub](https://github.com/Falcoria/falcoria-use-cases/tree/main/import-mode-replace)

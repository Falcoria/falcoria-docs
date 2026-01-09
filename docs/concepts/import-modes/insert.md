# Insert Mode

The **Insert** mode adds only new IP addresses to a project.  
Existing IPs and their ports are never modified.

---

## Behavior

- If an IP does not exist in the project → it will be added with its ports.  
- If an IP already exists → it is skipped completely.  
- Ports are only added for new IPs; existing IPs and their ports remain untouched.  

**Image placeholder:** canvas showing input list with duplicates → only new IPs added to the dataset.

---

## When to Use

Use Insert when you want to import results without touching existing data, for example:  

- Importing results from segmented or partial scans.  
- Loading results from offline sources or external tools.  
- Combining data from multiple discovery steps without risk of overwriting.  

---

## Example

```bash
falcli project ips import --file report_insert1.xml --mode insert
```

Output:

```text
Imported IPs report into project 'example-project-id'. Result: 2 IPs.
```

If you run it again with the same file, duplicates are skipped:

```text
No new IPs added in project
```

---

## Reference

- [Practical Example on GitHub](https://github.com/Falcoria/falcoria-use-cases/tree/main/import-mode-insert)

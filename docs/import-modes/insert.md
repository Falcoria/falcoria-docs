# `insert` Mode

The `insert` mode is the safest way to import scan results into a Falcoria project.  
It **adds new IPs** and their data only if they do not already exist — and **skips duplicates silently**.

This makes it ideal for importing results from passive scans, segmented scopes, or slow asset discovery — where you don’t want to accidentally overwrite or duplicate anything already collected.

---

## ✅ When to Use `insert`

Use this mode when:

- You're importing scan data from multiple small or partial scans
- You want to avoid modifying any existing project data
- You’re loading results from distributed scanning agents or external sources
- You’re transferring scans from an isolated or offline network environment where direct integration isn’t possible

---

## 🧠 Behavior Summary

- If an IP does **not** exist in the project → it will be added
- If an IP **already exists** → it will be skipped without error
- Ports are only added for new IPs; existing IPs and their ports remain untouched

---

## 💡 Example

```bash
python3 falcli.py project ips import --file report_insert1.xml --mode insert
```

Output:

```text
Imported IPs report into project 'example-project-id'. Result: 2 IPs.
```

If you run it again with the same file, it will detect duplicates and skip them:

```text
No new IPs added in project 
```

---

## 🔗 Try It Yourself

- [Step-by-Step Example on GitHub](https://github.com/Falcoria/falcoria-use-cases/tree/main/import-mode-insert)

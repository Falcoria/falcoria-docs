# `replace` Mode

The `replace` mode is a **destructive import mode** — it fully **removes and replaces** existing data for matching IPs.  
If an IP already exists in the project, it will be **wiped clean** (including all ports and metadata) and replaced with the data from the new report.

Use this mode when you want to overwrite outdated or incorrect scan results with fresh, authoritative data.

---

## ✅ When to Use `replace`

Use this mode when:

- You're resyncing results from a more complete or trusted scan
- You need to clean up bad or partial scan data
- You’re running a re-scan and want to discard old port states
- You’re enforcing source-of-truth data from a central scan server

---

## 🧠 Behavior Summary

- If an IP does **not** exist in the project → it will be added normally
- If an IP **already exists** → its entire record will be deleted and replaced
- Port and metadata fields are wiped and re-imported in full

---

## ⚠️ Warning

`replace` is **not reversible**. Once imported, previous data is lost unless you have a backup.  
Use with care, especially in collaborative environments.

---

## 💡 Example

```bash
python3 falcli.py project ips import --file report_replace1.xml --mode replace
```

Output:

```text
Imported IPs report into project 'example-project-id'. Result: 1 IP.
```

---

## 🔗 Try It Yourself

- [Step-by-Step Example on GitHub](https://github.com/Falcoria/falcoria-use-cases/tree/main/import-mode-replace)

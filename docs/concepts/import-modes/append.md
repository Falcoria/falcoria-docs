# `append` Mode

The `append` mode lets you **add new ports** to existing IPs without touching or modifying existing data.  
It’s designed for **parallel scans**, **port sharding**, and **multi-phase collection** — where multiple scan outputs need to be combined into one project.

This mode avoids any destructive behavior and is ideal when you want to gather more data over time.

---

## ✅ When to Use `append`

Use this mode when:

- You're combining partial results from multiple scan agents
- You're scanning different port ranges in separate phases
- You're running parallel workers to cover large IP scopes faster
- You're layering additional scan data (e.g. slow services or UDP) without disturbing existing results

---

## 🧠 Behavior Summary

- If an IP does **not** exist in the project → it will be added
- If an IP **exists** → new ports will be added, but existing ports stay unchanged
- Fields like `banner`, `service`, and metadata remain untouched for existing ports

---

## 🛡 Safe by Design

No existing data is modified or removed.  
`append` is fully additive — making it the best choice for distributed scan merging.

---

## 💡 Example

```bash
python3 falcli.py project ips import --file report_append1.xml --mode append
```

Output:

```text
Imported IPs report into project 'example-project-id'. Result: 1 IP.
```

After importing `report_append2.xml`, new ports will appear — without altering previously added ones.

---

## 🔗 Try It Yourself

- [Step-by-Step Example on GitHub](https://github.com/Falcoria/falcoria-use-cases/tree/main/import-mode-append)

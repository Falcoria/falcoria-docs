# `update` Mode

The `update` mode allows you to **enrich or refine** existing scan data without overwriting the entire IP record.  
It performs a **smart field-level merge** — updating only the values that are explicitly present in the new report.

This is perfect for progressive scanning, banner grabbing, or incrementally improving service detection.

---

## ✅ When to Use `update`

Use this mode when:

- You're enriching data with additional scan phases (e.g. version detection)
- You're merging passive and active results for the same IPs
- You're updating banners, services, or OS details from more specialized tools
- You want to preserve existing port data while refining metadata

---

## 🧠 Behavior Summary

- If an IP does **not** exist in the project → it will be added
- If an IP **exists** → its ports stay intact; only fields explicitly present in the import are updated
- Fields that are missing in the import report will not erase or overwrite existing data

---

## 🧠 Smart Merge Logic

Unlike `replace`, which wipes everything, `update` is non-destructive and selective.  
It’s ideal for long-term scan enrichment, especially when combining different tools or scan passes.

---

## 💡 Example

```bash
python3 falcli.py project ips import --file report_update1.xml --mode update
```

Output:

```text
Imported IPs report into project 'example-project-id'. Result: 1 IP.
```

Existing port data will remain, but service names or banners may be updated.

---

## 🔗 Try It Yourself

- [Step-by-Step Example on GitHub](https://github.com/Falcoria/falcoria-use-cases/tree/main/import-mode-update)

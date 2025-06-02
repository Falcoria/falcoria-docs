# Installation

Falcoria is built as a modular system. Each component serves a specific role, and you only need to install what fits your use case.

At this stage, two public modules are available:

---

## ScanLedger

**ScanLedger** is the backend responsible for storing, organizing, and querying scan results.  
It does not execute scans — but gives you full access to reports, project data, and import functionality.

→ [ScanLedger Installation Guide](installation/scanledger.md)

---

## falcli (CLI Client)

**`falcli`** is the command-line interface to manage projects, import data, and interact with ScanLedger.  
Use it to test workflows, automate project setup, or simulate scans manually.

→ [CLI Installation Guide](installation/falcli.md)

---

> ⚠️ Other modules such as `Tasker` and `Worker` (used for actual scanning and distribution) are not yet publicly released.

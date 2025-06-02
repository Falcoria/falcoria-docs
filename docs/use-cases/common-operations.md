# Common CLI Operations

This section demonstrates a standard workflow with Falcoria CLI — from project creation to scanning and result retrieval. Each command includes a brief description to make the process intuitive.

All operations are performed in the **currently selected project**. Results, scan statuses, and IP listings are scoped to this project by default.

To switch the current project:

```bash
python3 falcli.py memory list
```

Displays all saved projects and the last used project.

```bash
python3 falcli.py memory set-default <project_id>
```

Switches the active project used for all further commands.

---

## 1. Create a Project

```bash
python3 falcli.py project create pentest_example
```

Creates a new project for the scan. If a project is already in memory, you’ll be asked whether to replace it.

---

## 2. View Active Project

```bash
python3 falcli.py project get
```

Displays details of the currently selected project.

---

## 3. Start a Scan

```bash
python3 falcli.py scan start --config scan_configs/default.yaml --targets-file ../hosts.txt
```

Launches a scan using a specific configuration and a list of target hosts. `--config` is optional. By default, `default.yaml.` will be used. You can use other config files like `web.yaml`, `udp.yaml` to perform specified scans.

---

## 4. Check Scan Status

```bash
python3 falcli.py scan status -i
```

Shows real-time scan status with a progress bar.

---

## 5. List All Projects

```bash
python3 falcli.py project list
```

Displays all available projects with their names, IDs, and users.

---

## 6. Get Project by ID

```bash
python3 falcli.py project get <project_id>
```

Retrieves project metadata by its UUID.

---

## 7. List Scanned IPs

```bash
python3 falcli.py project ips list
```

Displays all scanned IPs and how many ports were found for each.

---

## 8. View Detailed IP Results

```bash
python3 falcli.py project ips get
```

Shows host status and service information for each scanned IP.

---

## 9. Download Scan Results

```bash
python3 falcli.py project ips download
```

Downloads the scan report for the current project as an XML file.

---

## 10. Delete All IPs from Project

```bash
python3 falcli.py project ips delete
```

Removes all IPs from the selected project.

---

## 11. Delete project and all its data

```bash
python3 falcli.py project delete <project_uuid>
```

These operations represent the basic usage pattern of Falcoria CLI — define project → scan targets → track progress → inspect or delete results.

# Real-Time Access and Collaboration on Scan Results

Falcoria enables real-time collaboration between multiple team members working on the same project. Once data is imported or a scan is launched, results become immediately available to all users connected to the shared backend — without needing to sync files, wait for exports, or coordinate tasks manually.

---

## Shared Workflow Example: External Scan Results

The following workflow demonstrates how one team member can import results from an external scan, and others can instantly explore, query, and export that data.

### Step 1 — One teammate runs an external scan

```bash
nmap 134.209.203.62 -Pn -n -oX report.xml
```

Example scan output:
```
PORT      STATE SERVICE
22/tcp    open  ssh
2222/tcp  open  EtherNetIP-1
5432/tcp  open  postgresql
50500/tcp open  unknown
```

Or start a scan with falcli. In this case you don't need to import results manually:
```bash
./falcli.py scan start --hosts 134.209.203.62
```


### Step 2 — Import results into a shared project

```bash
$ ./falcli.py project ips import -f report.xml
Imported IPs report into project '4e0d5a24-791d-4abb-a1fd-212f738b48b8'. Result: 1 IP.
```

### Step 3 — Other users access results immediately

List all scanned IPs:
```bash
$ ./falcli.py project ips list
IP              PORT_COUNT
134.209.203.62  4
```

Get full details for the host:
```bash
$ ./falcli.py project ips get
IP: 134.209.203.62
Status   : up
OS       : -
Hostnames: -

PORT   PROTO  STATE  SERVICE       BANNER
22     tcp    open   ssh           -     
2222   tcp    open   EtherNetIP-1  -     
5432   tcp    open   postgresql    -     
50500  tcp    open   -             -     
```

Download results as a report:
```bash
$ ./falcli.py project ips download
[+] Downloaded IPs report for project '4e0d5a24-791d-4abb-a1fd-212f738b48b8'.
```

### Step 4 — Or access data programmatically via API

Falcoria exposes a REST API to support integration into automation pipelines or external tools.

```bash
$ curl -s 'https://161.35.155.132/projects/4e0d5a24-791d-4abb-a1fd-212f738b48b8/ips' \
    -H 'Authorization: Bearer <YOUR_AUTH_TOKEN>' -k | jq
```

Example output:
```json
[
  {
    "ip": "134.209.203.62",
    "status": "up",
    "ports": [
      { "number": 22, "protocol": "tcp", "state": "open", "service": "ssh" },
      { "number": 2222, "protocol": "tcp", "state": "open", "service": "EtherNetIP-1" },
      { "number": 5432, "protocol": "tcp", "state": "open", "service": "postgresql" },
      { "number": 50500, "protocol": "tcp", "state": "open", "service": "" }
    ]
  }
]
```

---

## Summary

- One team member imports or launches a scan
- Others can immediately query results via CLI or API
- All data is centralized and synchronized via ScanLedger

This real-time access eliminates delays, file syncing, and duplicated effort — enabling fast, coordinated recon and analysis across any size team.
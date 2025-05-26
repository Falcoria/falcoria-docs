# Import Modes in Falcoria

Falcoria supports four import modes to give you full control over how scan results are added and updated within a project. These modes help prevent duplication, ensure consistency, and support workflows like incremental enrichment or full rescan replacement.

---

## Summary Table

| Mode    | Behavior                                           | Primary Use Case                                          |
| ------- | -------------------------------------------------- | --------------------------------------------------------- |
| insert  | Adds new entries; skips duplicates                 | Safe initial loads and clean data imports                 |
| replace | Replaces all existing records entirely             | Full target rescan or authoritative result refresh        |
| append  | Adds new data without touching existing records    | Port sharding, parallel scans, multi-phase collection     |
| update  | Updates only specific fields, preserves all others | Incremental enrichment, banner or service info refinement |

---

## `insert` Mode

Adds new data **only if the IP does not already exist** in the project. If the IP is already present, it will be **skipped silently**.

**Best for:**

* Initial imports
* Non-destructive runs
* Loading many partial reports

**Example:**

```bash
$ python3 falcli.py project ips import --file report_insert1.xml --mode insert
Imported IPs report into project '5a2e5a0d-a36f-456f-822d-4769c4e0fd4f'. Result: 2 IPs.

$ python3 falcli.py project ips list
IP              PORT_COUNT
134.209.203.62  6         
159.223.15.22   6         

$ python3 falcli.py project ips import --file report_insert2.xml --mode insert
Imported IPs report into project '5a2e5a0d-a36f-456f-822d-4769c4e0fd4f'. Result: 1 IP.

$ python3 falcli.py project ips list
IP               PORT_COUNT
134.209.203.62   6         
159.223.15.22    6         
188.166.121.245  8         
```

---

## `append` Mode

Adds new data **regardless of duplicates**. Existing records are **not touched or merged**.

**Best for:**

* Combining multiple scans
* Port sharding
* Merging safe/partial and extended scans

**Example:**

```bash
$ python3 falcli.py project ips import --file report_append1.xml 
Imported IPs report into project '5a2e5a0d-a36f-456f-822d-4769c4e0fd4f'. Result: 1 IP.

$ python3 falcli.py project ips get
IP: 134.209.203.62
Status   : up
OS       : -
Hostnames: -

PORT  PROTO  STATE  SERVICE       BANNER
22    tcp    open   ssh           -     
2222  tcp    open   EtherNetIP-1  -     
5432  tcp    open   postgresql    -     

$ python3 falcli.py project ips import --file report_append2.xml --mode append
Imported IPs report into project '5a2e5a0d-a36f-456f-822d-4769c4e0fd4f'. Result: 1 IP.

$ python3 falcli.py project ips get
IP: 134.209.203.62
Status   : up
OS       : -
Hostnames: -

PORT   PROTO  STATE  SERVICE       BANNER                                                                     
22     tcp    open   ssh           -                                                                          
2222   tcp    open   EtherNetIP-1  -                                                                          
5432   tcp    open   postgresql    -                                                                          
6379   tcp    open   redis         product: Redis key-value store                                             
50500  tcp    open   http          product: Golang net/http server extrainfo: Go-IPFS json-rpc or InfluxDB API
```

---

## `replace` Mode

Completely **overwrites** all existing data for an IP, including all ports. Even matching ports are replaced.

**Best for:**

* Retesting
* Overwriting old scan results

**Example:**

```bash
$ python3 falcli.py project ips import --file report_replace1.xml
Imported IPs report into project '5a2e5a0d-a36f-456f-822d-4769c4e0fd4f'. Result: 1 IP.

$ python3 falcli.py project ips get
IP: 134.209.203.62
Status   : up
OS       : -
Hostnames: -

PORT  PROTO  STATE  SERVICE  BANNER                                                                                                 
22    tcp    open   ssh      product: OpenSSH version: 8.9p1 Ubuntu 3ubuntu0.13 extrainfo: Ubuntu Linux; protocol 2.0 ostype: Linux

$ python3 falcli.py project ips import --file report_replace2.xml --mode replace
Imported IPs report into project '5a2e5a0d-a36f-456f-822d-4769c4e0fd4f'. Result: 1 IP.

$ python3 falcli.py project ips get
IP: 134.209.203.62
Status   : up
OS       : -
Hostnames: -

PORT  PROTO  STATE  SERVICE     BANNER
22    tcp    open   ssh         -     
5432  tcp    open   postgresql  -     
```

---

## `update` Mode

Performs a **smart merge**. Keeps existing ports and only updates fields that are explicitly present in the new report. Values like `banner` or `service` are preserved unless overwritten.

**Best for:**

* Incremental enrichment
* Deepening banner/service info

**Example:**

```bash
$ python3 falcli.py project ips import --file report_update1.xml
Imported IPs report into project '5a2e5a0d-a36f-456f-822d-4769c4e0fd4f'. Result: 1 IP.

$ python3 falcli.py project ips get
IP: 134.209.203.62
Status   : up
OS       : -
Hostnames: -

PORT  PROTO  STATE  SERVICE       BANNER
22    tcp    open   ssh           -     
2222  tcp    open   EtherNetIP-1  -     
5432  tcp    open   postgresql    -     

$ python3 falcli.py project ips import --file report_update2.xml --mode update
Imported IPs report into project '5a2e5a0d-a36f-456f-822d-4769c4e0fd4f'. Result: 1 IP.

$ python3 falcli.py project ips get
IP: 134.209.203.62
Status   : up
OS       : -
Hostnames: -

PORT   PROTO  STATE  SERVICE     BANNER                                                                                                 
22     tcp    open   ssh         product: OpenSSH version: 8.9p1 Ubuntu 3ubuntu0.13 extrainfo: Ubuntu Linux; protocol 2.0 ostype: Linux
2222   tcp    open   ssh         product: OpenSSH version: 9.9 extrainfo: protocol 2.0                                                 
5432   tcp    open   postgresql  product: PostgreSQL DB version: 9.6.0 or later                                                        
6379   tcp    open   redis       product: Redis key-value store                                                                        
50500  tcp    open   http        product: Golang net/http server extrainfo: Go-IPFS json-rpc or InfluxDB API                           
```
---
**Note:** All modes will add new IP addresses that don't already exist in the project. For scans **insert** mode is default.

## Field-Level Behavior

| Mode    | IP Address     | Ports               | Service Info                    | Summary Use Case                               |
| ------- | -------------- | ------------------- | ------------------------------- | ---------------------------------------------- |
| insert  | Creates new    | Creates new         | Creates new                     | First-time scan, safe inserts only             |
| replace | Overwrites     | Fully replaces      | Fully replaces                  | Rescan or full refresh                         |
| append  | Adds if new    | Adds only new ports | Does not change existing fields | Port sharding, safe parallel merge             |
| update  | Keeps existing | Keeps existing      | Updates provided fields only    | Service enrichment, field-by-field enhancement |

---

Use these modes to control how data enters Falcoria and to design scanning workflows that match your infrastructure and goals.

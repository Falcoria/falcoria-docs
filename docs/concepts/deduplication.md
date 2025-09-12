# Deduplication Behavior

Falcoria applies deduplication at several stages of the workflow.  
This prevents duplicate work, reduces scan time, avoids creating unnecessary tasks, and helps lower the probability of hitting rate limits.

**Deduplication:**  

- [String duplicates in input files](#string-duplicates-in-input-files)  
- [Unification of subnets and hostnames](#unification-of-subnets-and-hostnames)  
- [Skipping already stored targets (ScanLedger)](#skipping-already-stored-targets-scanledger)  
- [Skipping duplicate tasks in the queue](#skipping-duplicate-tasks-in-the-queue)

---

## String duplicates in input files

When a user provides a list of targets, duplicate string entries are removed.  
For example, if the same hostname or IP address appears multiple times, only one copy is kept.  

**Image placeholder:** show a list with duplicate entries → deduplicated list with unique targets.  

---

## Unification of subnets and hostnames

Falcoria normalizes mixed input before creating scan tasks:  

- Subnets (CIDR) are expanded into full lists of IP addresses.  
- Hostnames are resolved to IP addresses.  
- The final dataset contains only unique IPs and the hostnames associated with them.  

This ensures the same address is never scanned twice. It also shortens scan time and lowers the chance of triggering blocking mechanisms.  

**Image placeholder:** show subnet expansion and hostname resolution → resulting unique IP/hostname map.  

---

## Skipping already stored targets (ScanLedger)

If a target has already been scanned and exists in **ScanLedger**, it will not be scanned again.  
This applies both to new scans and to report imports.  

By default, this behavior is active in **Insert mode**.  
For details about other modes, see [Import Modes](../import-modes/index.md).  

**Image placeholder:** show ScanLedger with already stored IPs → new incoming data skipped.  

---

## Skipping duplicate tasks in the queue

If an identical target is already queued for scanning, a new task will not be created.  
This prevents multiple team members or processes from scanning the same target at the same time.  

**Image placeholder:** show queue with existing tasks → duplicate request rejected.  

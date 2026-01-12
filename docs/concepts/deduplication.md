# Deduplication Behavior

Falcoria applies deduplication at several stages of the workflow.  
This prevents redundant work, reduces scan time, avoids unnecessary tasks, and lowers the likelihood of hitting rate limits.

**Deduplication:**  

- [String duplicates in input files](#string-duplicates-in-input-files)  
- [Unification of subnets and hostnames](#unification-of-subnets-and-hostnames)  
- [Skipping already stored targets (ScanLedger)](#skipping-already-stored-targets-scanledger)  
- [Skipping duplicate tasks in the queue](#skipping-duplicate-tasks-in-the-queue)

---

## String duplicates in input files

![Deduplication of string duplicates](../images/deduplication_1.png){ align=center }

When a user provides a list of targets, duplicate string entries are removed.  
If the same hostname or IP address appears multiple times, only one entry is kept.

---

## Unification of subnets and hostnames

Falcoria normalizes mixed input before creating scan tasks:  

- Subnets (CIDR) are expanded into full lists of IP addresses.  
- Hostnames are resolved to IP addresses.  
- The final dataset contains only unique IPs and the hostnames associated with them.  

This ensures each address is scanned only once. It also shortens scan time and lowers the chance of triggering blocking mechanisms.  

**Image placeholder:** show subnet expansion and hostname resolution → resulting unique IP/hostname map.  

---

## Skipping already stored targets (ScanLedger)

If a target already exists in **ScanLedger**, it is not scanned again.

This applies to:

- new scan launches,
- imported scan results.

By default, this behavior is active in **Insert mode**.  
For details about other modes, see [Import Modes](../import-modes/index.md).  

**Image placeholder:** show ScanLedger with already stored IPs → new incoming data skipped.  

---

## Skipping duplicate tasks in the queue

If an identical scan task is already queued, a new task is not created.
This prevents multiple users or processes from scanning the same target at the same time.

**Image placeholder:** show queue with existing tasks → duplicate request rejected.  

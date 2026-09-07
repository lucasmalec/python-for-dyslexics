# Module 5: Subprocess & Shell Automation

[🇬🇧 English](README.md) | [🇵🇱 Polski](README.pl.md)

---

## 🎯 About This Module
Execute shell commands, capture stdout/stderr, handle process timeouts, and inspect return codes safely.

- **Target Focus:** Real-world sysadmin & cloud automation practices.
- **Visual Standard:** Clean layout, predictable structure, max 88 columns.

---

## 📝 Hands-on Practical Tasks (15 tasks)

### Task 01: Directory Listing Subprocess
- **Requirement (EN):** Execute `ls -la` via Python `subprocess.run()` and print captured stdout.
- **PL:** Uruchom `ls -la` z Pythona i wypisz wynik.
### Task 02: Capture Working Directory
- **Requirement (EN):** Execute `pwd` and capture clean directory string in a variable.
- **PL:** Uruchom `pwd` i zapisz wynik do zmiennej.
### Task 03: Ping Return Code Assertion
- **Requirement (EN):** Verify network reachability by checking if `ping -c 1 8.8.8.8` returns code 0.
- **PL:** Sprawdź, czy komenda `ping -c 1 google.com` się powiodła (returncode == 0).
### Task 04: Filtered Disk Space Query
- **Requirement (EN):** Execute `df -h` and print only storage partitions containing `/dev/`.
- **PL:** Uruchom `df -h` i wypisz tylko linie zawierające `/dev/sda`.
### Task 05: Custom Script Execution
- **Requirement (EN):** Execute local management script `wp-status` and stream output.
- **PL:** Uruchom swój skrypt `wp-status` i wypisz jego wynik.
### Task 06: Redirect Output to File
- **Requirement (EN):** Execute `wp-fleet` and persist stdout to `fleet_report.txt`.
- **PL:** Uruchom `wp-fleet` i zapisz wynik do pliku `raport_fleet.txt`.
### Task 07: Shell Redirection Operator
- **Requirement (EN):** Execute command with shell redirection: `echo 'pipeline active' > test.txt`.
- **PL:** Uruchom komendę z przekierowaniem (`shell=True`): `echo 'test' > test.txt`.
### Task 08: Database Backup Status
- **Requirement (EN):** Execute `mysql-backup-all` simulation and verify process exit code.
- **PL:** Uruchom `mysql-backup-all` i sprawdź, czy zakończył się sukcesem.
### Task 09: Execution Benchmark Timer
- **Requirement (EN):** Execute command and measure precise execution elapsed time.
- **PL:** Uruchom `wp-backup-lite` i zmierz czas wykonania.
### Task 10: Process Error Handling
- **Requirement (EN):** Execute invalid command intentionally and handle `subprocess.CalledProcessError`.
- **PL:** Uruchom komendę, która celowo zwróci błąd – obsłuż `CalledProcessError`.
### Task 11: Process Timeout Guard
- **Requirement (EN):** Execute process with strict timeout (e.g. `timeout=3` on long-running task).
- **PL:** Uruchom komendę z timeoutem (np. `timeout=5` dla `sleep 10`).
### Task 12: Output Line Count Parsing
- **Requirement (EN):** Execute CLI utility and parse output to count total discovered sites.
- **PL:** Uruchom `wp-cli-validator` i sparsuj wynik – wypisz tylko liczbę znalezionych stron.
### Task 13: Script Discovery Validator
- **Requirement (EN):** Write function `script_exists(name)` checking if automation script exists in `~/scripts/`.
- **PL:** Stwórz funkcję `czy_skrypt_istnieje(nazwa)`, która sprawdza czy skrypt WSMS jest w `~/scripts/`.
### Task 14: Structured Line Splitter
- **Requirement (EN):** Capture command output and transform it into a list of stripped string lines.
- **PL:** Uruchom `backup-list` i zapisz wynik jako listę stringów.
### Task 15: Consolidated System Health Report
- **Requirement (EN):** Build `health_check` uniting disk space, status, and fleet metrics into a single JSON report.
- **PL:** Stwórz własną komendę `wp-health-check`, która łączy wyniki w jeden raport JSON.

---
[Back to Part 2 Overview](../README.md)

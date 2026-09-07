# Moduł 5: Subprocess – Automatyzacja Powłoki i CLI

[🇬🇧 English](README.md) | [🇵🇱 Polski](README.pl.md)

---

## 🎯 O tym module
Wykonywanie poleceń systemowych, przechwytywanie stdout/stderr, obsługa timeoutów i kodów wyjścia.

- **Cel:** Praktyczna automatyzacja środowisk serwerowych i Cloud DevOps.
- **Standard wizualny:** Przejrzysty układ, przewidywalny rytm, limit 88 znaków.

---

## 📝 Zadania Praktyczne (15 zadań)

### Zadanie 01: Directory Listing Subprocess
- **Wymaganie (PL):** Uruchom `ls -la` z Pythona i wypisz wynik.
- **EN:** Execute `ls -la` via Python `subprocess.run()` and print captured stdout.
### Zadanie 02: Capture Working Directory
- **Wymaganie (PL):** Uruchom `pwd` i zapisz wynik do zmiennej.
- **EN:** Execute `pwd` and capture clean directory string in a variable.
### Zadanie 03: Ping Return Code Assertion
- **Wymaganie (PL):** Sprawdź, czy komenda `ping -c 1 google.com` się powiodła (returncode == 0).
- **EN:** Verify network reachability by checking if `ping -c 1 8.8.8.8` returns code 0.
### Zadanie 04: Filtered Disk Space Query
- **Wymaganie (PL):** Uruchom `df -h` i wypisz tylko linie zawierające `/dev/sda`.
- **EN:** Execute `df -h` and print only storage partitions containing `/dev/`.
### Zadanie 05: Custom Script Execution
- **Wymaganie (PL):** Uruchom swój skrypt `wp-status` i wypisz jego wynik.
- **EN:** Execute local management script `wp-status` and stream output.
### Zadanie 06: Redirect Output to File
- **Wymaganie (PL):** Uruchom `wp-fleet` i zapisz wynik do pliku `raport_fleet.txt`.
- **EN:** Execute `wp-fleet` and persist stdout to `fleet_report.txt`.
### Zadanie 07: Shell Redirection Operator
- **Wymaganie (PL):** Uruchom komendę z przekierowaniem (`shell=True`): `echo 'test' > test.txt`.
- **EN:** Execute command with shell redirection: `echo 'pipeline active' > test.txt`.
### Zadanie 08: Database Backup Status
- **Wymaganie (PL):** Uruchom `mysql-backup-all` i sprawdź, czy zakończył się sukcesem.
- **EN:** Execute `mysql-backup-all` simulation and verify process exit code.
### Zadanie 09: Execution Benchmark Timer
- **Wymaganie (PL):** Uruchom `wp-backup-lite` i zmierz czas wykonania.
- **EN:** Execute command and measure precise execution elapsed time.
### Zadanie 10: Process Error Handling
- **Wymaganie (PL):** Uruchom komendę, która celowo zwróci błąd – obsłuż `CalledProcessError`.
- **EN:** Execute invalid command intentionally and handle `subprocess.CalledProcessError`.
### Zadanie 11: Process Timeout Guard
- **Wymaganie (PL):** Uruchom komendę z timeoutem (np. `timeout=5` dla `sleep 10`).
- **EN:** Execute process with strict timeout (e.g. `timeout=3` on long-running task).
### Zadanie 12: Output Line Count Parsing
- **Wymaganie (PL):** Uruchom `wp-cli-validator` i sparsuj wynik – wypisz tylko liczbę znalezionych stron.
- **EN:** Execute CLI utility and parse output to count total discovered sites.
### Zadanie 13: Script Discovery Validator
- **Wymaganie (PL):** Stwórz funkcję `czy_skrypt_istnieje(nazwa)`, która sprawdza czy skrypt WSMS jest w `~/scripts/`.
- **EN:** Write function `script_exists(name)` checking if automation script exists in `~/scripts/`.
### Zadanie 14: Structured Line Splitter
- **Wymaganie (PL):** Uruchom `backup-list` i zapisz wynik jako listę stringów.
- **EN:** Capture command output and transform it into a list of stripped string lines.
### Zadanie 15: Consolidated System Health Report
- **Wymaganie (PL):** Stwórz własną komendę `wp-health-check`, która łączy wyniki w jeden raport JSON.
- **EN:** Build `health_check` uniting disk space, status, and fleet metrics into a single JSON report.

---
[Powrót do Spisu Treści Części 2](../README.pl.md)

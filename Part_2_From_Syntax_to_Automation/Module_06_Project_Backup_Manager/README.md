# Module 6: Capstone Mini-Project — Backup Manager CLI

[🇬🇧 English](README.md) | [🇵🇱 Polski](README.pl.md)

---

## 🎯 About This Module
Construct an end-to-end production backup rotation and retention tool with CLI arguments, logging, and metrics.

- **Target Focus:** Real-world sysadmin & cloud automation practices.
- **Visual Standard:** Clean layout, predictable structure, max 88 columns.

---

## 📝 Hands-on Practical Tasks (15 tasks)

### Task 01: List Backups Engine
- **Requirement (EN):** Create `backup_manager.py` with function `list_backups(directory)`.
- **PL:** Stwórz plik `backup_manager.py` z funkcją `list_backups(folder)`.
### Task 02: Aggregate Archive Statistics
- **Requirement (EN):** Add function `get_stats(files)` returning count, total size, oldest, and newest archive.
- **PL:** Dodaj funkcję `stats(backupy)`, która zwraca liczbę, łączny rozmiar, najstarszy i najnowszy plik.
### Task 03: Retention Cleaning Policy
- **Requirement (EN):** Add function `clean_old(folder, days=14)` deleting archives older than retention threshold.
- **PL:** Dodaj funkcję `clean_old(folder, days=14)`, która usuwa pliki starsze niż `days`.
### Task 04: Safe Dry-Run Flag
- **Requirement (EN):** Implement `--dry-run` parameter printing scheduled deletions without modifying disk.
- **PL:** Dodaj opcję `--dry-run` – tylko wypisuje, co by usunęła.
### Task 05: Cleaning Audit JSON Log
- **Requirement (EN):** Persist rotation audit trail to JSON: deleted items, timestamp, and freed bytes.
- **PL:** Dodaj zapisywanie raportu z czyszczenia do JSON.
### Task 06: Multi-Directory Federation
- **Requirement (EN):** Support scanning across directories: `~/backups-lite`, `~/backups-full`, `~/mysql-backups`.
- **PL:** Dodaj obsługę wielu folderów z backupami.
### Task 07: Storage Delta Calculation
- **Requirement (EN):** Measure and display free storage delta before and after rotation execution.
- **PL:** Dodaj sprawdzanie wolnego miejsca przed i po czyszczeniu.
### Task 08: Low Storage Warning Threshold
- **Requirement (EN):** Issue high-priority alert if available storage falls below 10% capacity.
- **PL:** Dodaj ostrzeżenie, jeśli wolnego miejsca jest mniej niż 10%.
### Task 09: Interactive Console Menu
- **Requirement (EN):** Provide menu: `1. List`, `2. Stats`, `3. Clean`, `4. Exit`.
- **PL:** Dodaj interaktywne menu: `1. Listuj`, `2. Statystyki`, `3. Czyść`, `4. Wyjście`.
### Task 10: Custom Retention Period Flag
- **Requirement (EN):** Allow user to pass custom retention period (e.g. `--days 30`).
- **PL:** Dodaj możliwość podania własnej liczby dni przy czyszczeniu.
### Task 11: Persistent File Logging
- **Requirement (EN):** Route rotation logs to rotating log file on disk.
- **PL:** Dodaj logowanie operacji do pliku (nie tylko na ekran).
### Task 12: Rich Table Presentation
- **Requirement (EN):** Format backup status reports in colorful ASCII terminal tables.
- **PL:** Użyj formatowania tabelarycznego do wyświetlania wyników.
### Task 13: Machine-Readable JSON Output
- **Requirement (EN):** Add `--json` flag outputting statistics in pure JSON format for monitoring integrations.
- **PL:** Dodaj opcję `--json`, która wypisuje statystyki w formacie JSON.
### Task 14: File Exclusion Pattern
- **Requirement (EN):** Allow excluding protected archives (e.g. `*.important` or `*golden*`).
- **PL:** Dodaj możliwość wykluczenia konkretnych plików z czyszczenia.
### Task 15: Standalone Executable CLI
- **Requirement (EN):** Package utility with shebang `#!/usr/bin/env python3` and execution permissions.
- **PL:** Przygotuj skrypt tak, by działał jako bezpośrednia komenda terminala.

---
[Back to Part 2 Overview](../README.md)

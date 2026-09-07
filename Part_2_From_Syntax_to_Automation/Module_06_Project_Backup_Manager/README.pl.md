# Moduł 6: Mini-Projekt – Menedżer Backupów CLI

[🇬🇧 English](README.md) | [🇵🇱 Polski](README.pl.md)

---

## 🎯 O tym module
Budowa kompletnego menedżera archiwów: rotacja, retencja, parametry CLI, logowanie i statystyki.

- **Cel:** Praktyczna automatyzacja środowisk serwerowych i Cloud DevOps.
- **Standard wizualny:** Przejrzysty układ, przewidywalny rytm, limit 88 znaków.

---

## 📝 Zadania Praktyczne (15 zadań)

### Zadanie 01: List Backups Engine
- **Wymaganie (PL):** Stwórz plik `backup_manager.py` z funkcją `list_backups(folder)`.
- **EN:** Create `backup_manager.py` with function `list_backups(directory)`.
### Zadanie 02: Aggregate Archive Statistics
- **Wymaganie (PL):** Dodaj funkcję `stats(backupy)`, która zwraca liczbę, łączny rozmiar, najstarszy i najnowszy plik.
- **EN:** Add function `get_stats(files)` returning count, total size, oldest, and newest archive.
### Zadanie 03: Retention Cleaning Policy
- **Wymaganie (PL):** Dodaj funkcję `clean_old(folder, days=14)`, która usuwa pliki starsze niż `days`.
- **EN:** Add function `clean_old(folder, days=14)` deleting archives older than retention threshold.
### Zadanie 04: Safe Dry-Run Flag
- **Wymaganie (PL):** Dodaj opcję `--dry-run` – tylko wypisuje, co by usunęła.
- **EN:** Implement `--dry-run` parameter printing scheduled deletions without modifying disk.
### Zadanie 05: Cleaning Audit JSON Log
- **Wymaganie (PL):** Dodaj zapisywanie raportu z czyszczenia do JSON.
- **EN:** Persist rotation audit trail to JSON: deleted items, timestamp, and freed bytes.
### Zadanie 06: Multi-Directory Federation
- **Wymaganie (PL):** Dodaj obsługę wielu folderów z backupami.
- **EN:** Support scanning across directories: `~/backups-lite`, `~/backups-full`, `~/mysql-backups`.
### Zadanie 07: Storage Delta Calculation
- **Wymaganie (PL):** Dodaj sprawdzanie wolnego miejsca przed i po czyszczeniu.
- **EN:** Measure and display free storage delta before and after rotation execution.
### Zadanie 08: Low Storage Warning Threshold
- **Wymaganie (PL):** Dodaj ostrzeżenie, jeśli wolnego miejsca jest mniej niż 10%.
- **EN:** Issue high-priority alert if available storage falls below 10% capacity.
### Zadanie 09: Interactive Console Menu
- **Wymaganie (PL):** Dodaj interaktywne menu: `1. Listuj`, `2. Statystyki`, `3. Czyść`, `4. Wyjście`.
- **EN:** Provide menu: `1. List`, `2. Stats`, `3. Clean`, `4. Exit`.
### Zadanie 10: Custom Retention Period Flag
- **Wymaganie (PL):** Dodaj możliwość podania własnej liczby dni przy czyszczeniu.
- **EN:** Allow user to pass custom retention period (e.g. `--days 30`).
### Zadanie 11: Persistent File Logging
- **Wymaganie (PL):** Dodaj logowanie operacji do pliku (nie tylko na ekran).
- **EN:** Route rotation logs to rotating log file on disk.
### Zadanie 12: Rich Table Presentation
- **Wymaganie (PL):** Użyj formatowania tabelarycznego do wyświetlania wyników.
- **EN:** Format backup status reports in colorful ASCII terminal tables.
### Zadanie 13: Machine-Readable JSON Output
- **Wymaganie (PL):** Dodaj opcję `--json`, która wypisuje statystyki w formacie JSON.
- **EN:** Add `--json` flag outputting statistics in pure JSON format for monitoring integrations.
### Zadanie 14: File Exclusion Pattern
- **Wymaganie (PL):** Dodaj możliwość wykluczenia konkretnych plików z czyszczenia.
- **EN:** Allow excluding protected archives (e.g. `*.important` or `*golden*`).
### Zadanie 15: Standalone Executable CLI
- **Wymaganie (PL):** Przygotuj skrypt tak, by działał jako bezpośrednia komenda terminala.
- **EN:** Package utility with shebang `#!/usr/bin/env python3` and execution permissions.

---
[Powrót do Spisu Treści Części 2](../README.pl.md)

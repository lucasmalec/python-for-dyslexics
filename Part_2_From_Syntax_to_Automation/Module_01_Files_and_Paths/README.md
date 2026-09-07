# Module 1: Working with Files & Paths (open, os, pathlib)

[🇬🇧 English](README.md) | [🇵🇱 Polski](README.pl.md)

---

## 🎯 About This Module
Master safe file I/O, context managers (`with`), directory scanning, and modern path resolution with `pathlib`.

- **Target Focus:** Real-world sysadmin & cloud automation practices.
- **Visual Standard:** Clean layout, predictable structure, max 88 columns.

---

## 📝 Hands-on Practical Tasks (15 tasks)

### Task 01: Print Current Working Directory
- **Requirement (EN):** Print your current working directory using `os.getcwd()`.
- **PL:** Wypisz swoją bieżącą ścieżkę roboczą (`os.getcwd()`).
### Task 02: Create Backup Directory
- **Requirement (EN):** Create directory `test_backups` in your home folder using `pathlib` or `os.mkdir()`.
- **PL:** Stwórz folder `test_backupy` w swoim katalogu domowym.
### Task 03: Create Batch Text Files
- **Requirement (EN):** Inside `test_backups`, create 3 text files: `backup1.txt`, `backup2.txt`, `backup3.txt`.
- **PL:** W tym folderze stwórz 3 pliki tekstowe: `backup1.txt`, `backup2.txt`, `backup3.txt`.
### Task 04: Write Timestamped Headers
- **Requirement (EN):** Write `Backup created on: [current date]` into each created file.
- **PL:** Do każdego pliku wpisz: `Backup z dnia: [dzisiejsza data]`.
### Task 05: Read and Print All Files
- **Requirement (EN):** Read the contents of all 3 files and display them in the terminal.
- **PL:** Odczytaj zawartość wszystkich 3 plików i wypisz je na ekran.
### Task 06: File Existence Verification
- **Requirement (EN):** Check if `nonexistent.txt` exists; if not, output a clear status message.
- **PL:** Sprawdź, czy plik `nieistnieje.txt` istnieje – jeśli nie, wypisz komunikat.
### Task 07: List Files by Extension
- **Requirement (EN):** List all `.txt` files in directory `test_backups`.
- **PL:** Wypisz listę wszystkich plików `.txt` w folderze `test_backupy`.
### Task 08: Rename File
- **Requirement (EN):** Rename file `backup1.txt` to `backup1_old.txt`.
- **PL:** Zmień nazwę pliku `backup1.txt` na `backup1_old.txt`.
### Task 09: Copy File
- **Requirement (EN):** Copy `backup2.txt` to `backup2_copy.txt` using `shutil.copy()`.
- **PL:** Skopiuj plik `backup2.txt` do `backup2_kopia.txt`.
### Task 10: Delete File Safely
- **Requirement (EN):** Delete file `backup3.txt` verifying its removal.
- **PL:** Usuń plik `backup3.txt`.
### Task 11: File Size Inspection
- **Requirement (EN):** Inspect the exact size of `backup2.txt` in bytes.
- **PL:** Sprawdź rozmiar pliku `backup2.txt` w bajtach.
### Task 12: Pathlib Resolution
- **Requirement (EN):** Using `pathlib.Path`, resolve path to `~/scripts/wp-status` and check its existence.
- **PL:** Używając `pathlib`, stwórz ścieżkę do `~/scripts/wp-status` i sprawdź, czy istnieje.
### Task 13: Filter Shell Scripts
- **Requirement (EN):** List all files in your home directory that possess the `.sh` extension.
- **PL:** Wypisz wszystkie pliki w swoim katalogu domowym, które mają rozszerzenie `.sh`.
### Task 14: Disk Free Space Function
- **Requirement (EN):** Write function `get_free_disk_space(path)` that returns available space in gigabytes (GB).
- **PL:** Napisz funkcję `przestrzen_dysku(sciezka)`, która zwraca wolne miejsce w GB.
### Task 15: Directory Manifest Generator
- **Requirement (EN):** Build a utility scanning `~/backups-lite` and writing discovered filenames into `backup_manifest.txt`.
- **PL:** Stwórz program, który listuje wszystkie pliki w folderze `~/backups-lite` i zapisuje ich nazwy do `lista_backupow.txt`.

---
[Back to Part 2 Overview](../README.md)

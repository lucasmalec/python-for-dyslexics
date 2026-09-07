# Moduł 1: Praca z Plikami i Ścieżkami (open, os, pathlib)

[🇬🇧 English](README.md) | [🇵🇱 Polski](README.pl.md)

---

## 🎯 O tym module
Zrozumienie bezpiecznego odczytu i zapisu plików, menedżerów kontekstu `with`, operacji na katalogach oraz nowoczesnego modułu `pathlib`.

- **Cel:** Praktyczna automatyzacja środowisk serwerowych i Cloud DevOps.
- **Standard wizualny:** Przejrzysty układ, przewidywalny rytm, limit 88 znaków.

---

## 📝 Zadania Praktyczne (15 zadań)

### Zadanie 01: Print Current Working Directory
- **Wymaganie (PL):** Wypisz swoją bieżącą ścieżkę roboczą (`os.getcwd()`).
- **EN:** Print your current working directory using `os.getcwd()`.
### Zadanie 02: Create Backup Directory
- **Wymaganie (PL):** Stwórz folder `test_backupy` w swoim katalogu domowym.
- **EN:** Create directory `test_backups` in your home folder using `pathlib` or `os.mkdir()`.
### Zadanie 03: Create Batch Text Files
- **Wymaganie (PL):** W tym folderze stwórz 3 pliki tekstowe: `backup1.txt`, `backup2.txt`, `backup3.txt`.
- **EN:** Inside `test_backups`, create 3 text files: `backup1.txt`, `backup2.txt`, `backup3.txt`.
### Zadanie 04: Write Timestamped Headers
- **Wymaganie (PL):** Do każdego pliku wpisz: `Backup z dnia: [dzisiejsza data]`.
- **EN:** Write `Backup created on: [current date]` into each created file.
### Zadanie 05: Read and Print All Files
- **Wymaganie (PL):** Odczytaj zawartość wszystkich 3 plików i wypisz je na ekran.
- **EN:** Read the contents of all 3 files and display them in the terminal.
### Zadanie 06: File Existence Verification
- **Wymaganie (PL):** Sprawdź, czy plik `nieistnieje.txt` istnieje – jeśli nie, wypisz komunikat.
- **EN:** Check if `nonexistent.txt` exists; if not, output a clear status message.
### Zadanie 07: List Files by Extension
- **Wymaganie (PL):** Wypisz listę wszystkich plików `.txt` w folderze `test_backupy`.
- **EN:** List all `.txt` files in directory `test_backups`.
### Zadanie 08: Rename File
- **Wymaganie (PL):** Zmień nazwę pliku `backup1.txt` na `backup1_old.txt`.
- **EN:** Rename file `backup1.txt` to `backup1_old.txt`.
### Zadanie 09: Copy File
- **Wymaganie (PL):** Skopiuj plik `backup2.txt` do `backup2_kopia.txt`.
- **EN:** Copy `backup2.txt` to `backup2_copy.txt` using `shutil.copy()`.
### Zadanie 10: Delete File Safely
- **Wymaganie (PL):** Usuń plik `backup3.txt`.
- **EN:** Delete file `backup3.txt` verifying its removal.
### Zadanie 11: File Size Inspection
- **Wymaganie (PL):** Sprawdź rozmiar pliku `backup2.txt` w bajtach.
- **EN:** Inspect the exact size of `backup2.txt` in bytes.
### Zadanie 12: Pathlib Resolution
- **Wymaganie (PL):** Używając `pathlib`, stwórz ścieżkę do `~/scripts/wp-status` i sprawdź, czy istnieje.
- **EN:** Using `pathlib.Path`, resolve path to `~/scripts/wp-status` and check its existence.
### Zadanie 13: Filter Shell Scripts
- **Wymaganie (PL):** Wypisz wszystkie pliki w swoim katalogu domowym, które mają rozszerzenie `.sh`.
- **EN:** List all files in your home directory that possess the `.sh` extension.
### Zadanie 14: Disk Free Space Function
- **Wymaganie (PL):** Napisz funkcję `przestrzen_dysku(sciezka)`, która zwraca wolne miejsce w GB.
- **EN:** Write function `get_free_disk_space(path)` that returns available space in gigabytes (GB).
### Zadanie 15: Directory Manifest Generator
- **Wymaganie (PL):** Stwórz program, który listuje wszystkie pliki w folderze `~/backups-lite` i zapisuje ich nazwy do `lista_backupow.txt`.
- **EN:** Build a utility scanning `~/backups-lite` and writing discovered filenames into `backup_manifest.txt`.

---
[Powrót do Spisu Treści Części 2](../README.pl.md)

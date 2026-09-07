# Module 3: Modules & Imports (Architecture & Packaging)

[🇬🇧 English](README.md) | [🇵🇱 Polski](README.pl.md)

---

## 🎯 About This Module
Understand Python import mechanics, module resolution in `sys.path`, package namespaces, and `__init__.py`.

- **Target Focus:** Real-world sysadmin & cloud automation practices.
- **Visual Standard:** Clean layout, predictable structure, max 88 columns.

---

## 📝 Hands-on Practical Tasks (15 tasks)

### Task 01: Math Helper Module
- **Requirement (EN):** Create module `calculator.py` with functions `add()`, `subtract()`, `multiply()`, `divide()`.
- **PL:** Stwórz plik `kalkulator.py` z funkcjami `dodaj()`, `odejmij()`, `pomnoz()`, `podziel()`.
### Task 02: Full Module Import
- **Requirement (EN):** In `main.py`, import the entire `calculator` module and test each arithmetic function.
- **PL:** W pliku `main.py` zaimportuj cały moduł `kalkulator` i użyj każdej funkcji.
### Task 03: Selective Function Import
- **Requirement (EN):** In a new script, selectively import only `add` and `divide` from `calculator`.
- **PL:** W nowym pliku zaimportuj tylko `dodaj` i `podziel` z `kalkulator`.
### Task 04: Package Architecture Initialization
- **Requirement (EN):** Create directory `utils` with `__init__.py` and relocate `calculator.py` inside it.
- **PL:** Stwórz folder `utils` z plikiem `__init__.py` i przenieś tam `kalkulator.py`.
### Task 05: Package Submodule Import
- **Requirement (EN):** Import `calculator` from `utils` using syntax `from utils import calculator`.
- **PL:** Zaimportuj `kalkulator` z folderu `utils` używając `from utils import kalkulator`.
### Task 06: Configuration Constant Module
- **Requirement (EN):** Create `config.py` declaring constants: `BACKUP_DIR = '~/backups'`, `RETENTION_DAYS = 14`.
- **PL:** Stwórz plik `config.py` ze zmiennymi: `BACKUP_DIR = '~/backups'`, `RETENCJA_DNI = 14`.
### Task 07: Configuration Import and Consumption
- **Requirement (EN):** Import `config` in `main.py` and print the active configuration constants.
- **PL:** Zaimportuj `config` w `main.py` i wypisz wartości zmiennych.
### Task 08: Import Aliasing
- **Requirement (EN):** Import constant with alias: `from config import BACKUP_DIR as BD`.
- **PL:** Użyj `from config import BACKUP_DIR as BD` (alias).
### Task 09: Dedicated Logger Module
- **Requirement (EN):** Create `logger.py` with function `log_message(text, level='INFO')`.
- **PL:** Stwórz moduł `logi.py` z funkcją `zapisz_log(tekst, poziom='INFO')`.
### Task 10: Integrated Logger Execution
- **Requirement (EN):** In `main.py`, import `logger` and record: `log_message('Application initialized')`.
- **PL:** W `main.py` zaimportuj `logi` i wywołaj `zapisz_log('Start programu')`.
### Task 11: Inspect Python Search Path
- **Requirement (EN):** Inspect Python module resolution paths by printing `sys.path` entries.
- **PL:** Sprawdź, czy Python widzi Twój moduł – wypisz `sys.path`.
### Task 12: Package Export Exposing in __init__
- **Requirement (EN):** In `utils/__init__.py`, import `add` and `divide` so `from utils import add` works cleanly.
- **PL:** Stwórz plik `__init__.py` w `utils`, który importuje `dodaj` i `podziel`.
### Task 13: Unit Self-Test Entry Guard
- **Requirement (EN):** Add `if __name__ == '__main__':` in `calculator.py` with standalone self-tests.
- **PL:** Użyj `if __name__ == '__main__':` w `kalkulator.py` – dodaj testy funkcji.
### Task 14: Module Load Notification Hook
- **Requirement (EN):** Create a module that prints `'Module successfully initialized'` upon import.
- **PL:** Stwórz moduł, który przy imporcie wypisuje `'Moduł załadowany'`.
### Task 15: Hot Reloading with importlib
- **Requirement (EN):** Use `importlib.reload()` to reload a modified module dynamically without interpreter restart.
- **PL:** Użyj `importlib.reload()` do przeładowania modułu bez restartu Pythona.

---
[Back to Part 2 Overview](../README.md)

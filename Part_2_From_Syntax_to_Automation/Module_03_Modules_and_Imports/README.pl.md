# Moduł 3: Moduły i Importy (Architektura i Pakiety)

[🇬🇧 English](README.md) | [🇵🇱 Polski](README.pl.md)

---

## 🎯 O tym module
Zrozumienie mechanizmów importu w Pythonie, ścieżki `sys.path`, przestrzeni pakietów i roli `__init__.py`.

- **Cel:** Praktyczna automatyzacja środowisk serwerowych i Cloud DevOps.
- **Standard wizualny:** Przejrzysty układ, przewidywalny rytm, limit 88 znaków.

---

## 📝 Zadania Praktyczne (15 zadań)

### Zadanie 01: Math Helper Module
- **Wymaganie (PL):** Stwórz plik `kalkulator.py` z funkcjami `dodaj()`, `odejmij()`, `pomnoz()`, `podziel()`.
- **EN:** Create module `calculator.py` with functions `add()`, `subtract()`, `multiply()`, `divide()`.
### Zadanie 02: Full Module Import
- **Wymaganie (PL):** W pliku `main.py` zaimportuj cały moduł `kalkulator` i użyj każdej funkcji.
- **EN:** In `main.py`, import the entire `calculator` module and test each arithmetic function.
### Zadanie 03: Selective Function Import
- **Wymaganie (PL):** W nowym pliku zaimportuj tylko `dodaj` i `podziel` z `kalkulator`.
- **EN:** In a new script, selectively import only `add` and `divide` from `calculator`.
### Zadanie 04: Package Architecture Initialization
- **Wymaganie (PL):** Stwórz folder `utils` z plikiem `__init__.py` i przenieś tam `kalkulator.py`.
- **EN:** Create directory `utils` with `__init__.py` and relocate `calculator.py` inside it.
### Zadanie 05: Package Submodule Import
- **Wymaganie (PL):** Zaimportuj `kalkulator` z folderu `utils` używając `from utils import kalkulator`.
- **EN:** Import `calculator` from `utils` using syntax `from utils import calculator`.
### Zadanie 06: Configuration Constant Module
- **Wymaganie (PL):** Stwórz plik `config.py` ze zmiennymi: `BACKUP_DIR = '~/backups'`, `RETENCJA_DNI = 14`.
- **EN:** Create `config.py` declaring constants: `BACKUP_DIR = '~/backups'`, `RETENTION_DAYS = 14`.
### Zadanie 07: Configuration Import and Consumption
- **Wymaganie (PL):** Zaimportuj `config` w `main.py` i wypisz wartości zmiennych.
- **EN:** Import `config` in `main.py` and print the active configuration constants.
### Zadanie 08: Import Aliasing
- **Wymaganie (PL):** Użyj `from config import BACKUP_DIR as BD` (alias).
- **EN:** Import constant with alias: `from config import BACKUP_DIR as BD`.
### Zadanie 09: Dedicated Logger Module
- **Wymaganie (PL):** Stwórz moduł `logi.py` z funkcją `zapisz_log(tekst, poziom='INFO')`.
- **EN:** Create `logger.py` with function `log_message(text, level='INFO')`.
### Zadanie 10: Integrated Logger Execution
- **Wymaganie (PL):** W `main.py` zaimportuj `logi` i wywołaj `zapisz_log('Start programu')`.
- **EN:** In `main.py`, import `logger` and record: `log_message('Application initialized')`.
### Zadanie 11: Inspect Python Search Path
- **Wymaganie (PL):** Sprawdź, czy Python widzi Twój moduł – wypisz `sys.path`.
- **EN:** Inspect Python module resolution paths by printing `sys.path` entries.
### Zadanie 12: Package Export Exposing in __init__
- **Wymaganie (PL):** Stwórz plik `__init__.py` w `utils`, który importuje `dodaj` i `podziel`.
- **EN:** In `utils/__init__.py`, import `add` and `divide` so `from utils import add` works cleanly.
### Zadanie 13: Unit Self-Test Entry Guard
- **Wymaganie (PL):** Użyj `if __name__ == '__main__':` w `kalkulator.py` – dodaj testy funkcji.
- **EN:** Add `if __name__ == '__main__':` in `calculator.py` with standalone self-tests.
### Zadanie 14: Module Load Notification Hook
- **Wymaganie (PL):** Stwórz moduł, który przy imporcie wypisuje `'Moduł załadowany'`.
- **EN:** Create a module that prints `'Module successfully initialized'` upon import.
### Zadanie 15: Hot Reloading with importlib
- **Wymaganie (PL):** Użyj `importlib.reload()` do przeładowania modułu bez restartu Pythona.
- **EN:** Use `importlib.reload()` to reload a modified module dynamically without interpreter restart.

---
[Powrót do Spisu Treści Części 2](../README.pl.md)

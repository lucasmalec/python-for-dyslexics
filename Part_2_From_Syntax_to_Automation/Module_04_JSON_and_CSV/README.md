# Module 4: Structured Data — JSON & CSV

[🇬🇧 English](README.md) | [🇵🇱 Polski](README.pl.md)

---

## 🎯 About This Module
Serialize and deserialize server configurations, site inventories, metrics, and logs with `json` and `csv`.

- **Target Focus:** Real-world sysadmin & cloud automation practices.
- **Visual Standard:** Clean layout, predictable structure, max 88 columns.

---

## 📝 Hands-on Practical Tasks (15 tasks)

### Task 01: Dictionary to JSON File
- **Requirement (EN):** Create dictionary `server = {'name': 'Ubuntu', 'version': '22.04', 'ram_gb': 8}` and dump to `server.json`.
- **PL:** Stwórz słownik `serwer = {'nazwa': 'Ubuntu', 'wersja': '22.04', 'ram_gb': 8}` i zapisz go do `serwer.json`.
### Task 02: Parse and Iterate JSON
- **Requirement (EN):** Read `server.json` and display all key-value configuration pairs.
- **PL:** Odczytaj `serwer.json` i wypisz wszystkie klucze i wartości.
### Task 03: JSON Update and Persistence
- **Requirement (EN):** Modify dictionary (add `'disk_gb': 100`) and persist updates to `server.json`.
- **PL:** Zmodyfikuj słownik (dodaj `'dysk_gb': 100`) i zapisz ponownie do tego samego pliku.
### Task 04: Indented Multi-record JSON
- **Requirement (EN):** Create list of website dicts and save to JSON with 2-space indentation formatting.
- **PL:** Stwórz listę słowników stron i zapisz do JSON z `indent=2`.
### Task 05: JSON Filter Query
- **Requirement (EN):** Read websites JSON inventory and filter items matching version `'6.2'`.
- **PL:** Odczytaj listę stron i wypisz tylko te z wersją `6.2`.
### Task 06: CSV Header Initialization
- **Requirement (EN):** Create CSV file `sites.csv` with headers: `name`, `version`, `status`.
- **PL:** Stwórz plik CSV `strony.csv` z kolumnami: `nazwa`, `wersja`, `status`.
### Task 07: Append Rows to CSV
- **Requirement (EN):** Append 3 rows of structured website records to `sites.csv`.
- **PL:** Dodaj 3 wiersze danych do `strony.csv`.
### Task 08: DictReader CSV Parsing
- **Requirement (EN):** Read `sites.csv` and yield each record as a dictionary via `csv.DictReader`.
- **PL:** Odczytaj `strony.csv` i wypisz każdy wiersz jako słownik (`csv.DictReader`).
### Task 09: Filtered Search on CSV
- **Requirement (EN):** Find and print all site records in the CSV flagged with status `'Update needed'`.
- **PL:** Znajdź w CSV wszystkie strony ze statusem `'Update needed'`.
### Task 10: JSON to CSV Pipeline Converter
- **Requirement (EN):** Write function `json_to_csv(json_path, csv_path)` transforming JSON records into CSV format.
- **PL:** Stwórz funkcję `json_do_csv(json_file, csv_file)`, która konwertuje plik JSON na CSV.
### Task 11: CSV to JSON Pipeline Converter
- **Requirement (EN):** Write function `csv_to_json(csv_path, json_path)` converting CSV tables into JSON objects.
- **PL:** Stwórz funkcję `csv_do_json(csv_file, json_file)`.
### Task 12: ISO Datetime Serialization
- **Requirement (EN):** Serialize current timestamp (`datetime.now().isoformat()`) alongside operational payload into JSON.
- **PL:** Zapisz do JSON datę i godzinę (`datetime.now().isoformat()`) wraz z dowolnymi danymi.
### Task 13: Datetime Deserialization
- **Requirement (EN):** Parse ISO timestamp string from JSON back into a native Python `datetime` object.
- **PL:** Odczytaj JSON zawierający datę i przekonwertuj string z powrotem na obiekt `datetime`.
### Task 14: Multi-file JSON Combiner
- **Requirement (EN):** Build a utility merging two JSON lists into a single consolidated JSON archive.
- **PL:** Stwórz program, który łączy dwa pliki JSON (listy) w jeden.
### Task 15: Schema Validation Guard
- **Requirement (EN):** Write a validator asserting that imported JSON objects possess required schema keys (`'name'`, `'version'`).
- **PL:** Napisz walidator – sprawdź, czy wczytany JSON ma wymagane klucze (`'nazwa'`, `'wersja'`).

---
[Back to Part 2 Overview](../README.md)

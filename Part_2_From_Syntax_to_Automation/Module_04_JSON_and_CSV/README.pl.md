# Moduł 4: Dane Strukturalne – JSON i CSV

[🇬🇧 English](README.md) | [🇵🇱 Polski](README.pl.md)

---

## 🎯 O tym module
Serializacja i parsowanie konfiguracji serwerowych, inwentaryzacji stron i logów za pomocą bibliotek `json` i `csv`.

- **Cel:** Praktyczna automatyzacja środowisk serwerowych i Cloud DevOps.
- **Standard wizualny:** Przejrzysty układ, przewidywalny rytm, limit 88 znaków.

---

## 📝 Zadania Praktyczne (15 zadań)

### Zadanie 01: Dictionary to JSON File
- **Wymaganie (PL):** Stwórz słownik `serwer = {'nazwa': 'Ubuntu', 'wersja': '22.04', 'ram_gb': 8}` i zapisz go do `serwer.json`.
- **EN:** Create dictionary `server = {'name': 'Ubuntu', 'version': '22.04', 'ram_gb': 8}` and dump to `server.json`.
### Zadanie 02: Parse and Iterate JSON
- **Wymaganie (PL):** Odczytaj `serwer.json` i wypisz wszystkie klucze i wartości.
- **EN:** Read `server.json` and display all key-value configuration pairs.
### Zadanie 03: JSON Update and Persistence
- **Wymaganie (PL):** Zmodyfikuj słownik (dodaj `'dysk_gb': 100`) i zapisz ponownie do tego samego pliku.
- **EN:** Modify dictionary (add `'disk_gb': 100`) and persist updates to `server.json`.
### Zadanie 04: Indented Multi-record JSON
- **Wymaganie (PL):** Stwórz listę słowników stron i zapisz do JSON z `indent=2`.
- **EN:** Create list of website dicts and save to JSON with 2-space indentation formatting.
### Zadanie 05: JSON Filter Query
- **Wymaganie (PL):** Odczytaj listę stron i wypisz tylko te z wersją `6.2`.
- **EN:** Read websites JSON inventory and filter items matching version `'6.2'`.
### Zadanie 06: CSV Header Initialization
- **Wymaganie (PL):** Stwórz plik CSV `strony.csv` z kolumnami: `nazwa`, `wersja`, `status`.
- **EN:** Create CSV file `sites.csv` with headers: `name`, `version`, `status`.
### Zadanie 07: Append Rows to CSV
- **Wymaganie (PL):** Dodaj 3 wiersze danych do `strony.csv`.
- **EN:** Append 3 rows of structured website records to `sites.csv`.
### Zadanie 08: DictReader CSV Parsing
- **Wymaganie (PL):** Odczytaj `strony.csv` i wypisz każdy wiersz jako słownik (`csv.DictReader`).
- **EN:** Read `sites.csv` and yield each record as a dictionary via `csv.DictReader`.
### Zadanie 09: Filtered Search on CSV
- **Wymaganie (PL):** Znajdź w CSV wszystkie strony ze statusem `'Update needed'`.
- **EN:** Find and print all site records in the CSV flagged with status `'Update needed'`.
### Zadanie 10: JSON to CSV Pipeline Converter
- **Wymaganie (PL):** Stwórz funkcję `json_do_csv(json_file, csv_file)`, która konwertuje plik JSON na CSV.
- **EN:** Write function `json_to_csv(json_path, csv_path)` transforming JSON records into CSV format.
### Zadanie 11: CSV to JSON Pipeline Converter
- **Wymaganie (PL):** Stwórz funkcję `csv_do_json(csv_file, json_file)`.
- **EN:** Write function `csv_to_json(csv_path, json_path)` converting CSV tables into JSON objects.
### Zadanie 12: ISO Datetime Serialization
- **Wymaganie (PL):** Zapisz do JSON datę i godzinę (`datetime.now().isoformat()`) wraz z dowolnymi danymi.
- **EN:** Serialize current timestamp (`datetime.now().isoformat()`) alongside operational payload into JSON.
### Zadanie 13: Datetime Deserialization
- **Wymaganie (PL):** Odczytaj JSON zawierający datę i przekonwertuj string z powrotem na obiekt `datetime`.
- **EN:** Parse ISO timestamp string from JSON back into a native Python `datetime` object.
### Zadanie 14: Multi-file JSON Combiner
- **Wymaganie (PL):** Stwórz program, który łączy dwa pliki JSON (listy) w jeden.
- **EN:** Build a utility merging two JSON lists into a single consolidated JSON archive.
### Zadanie 15: Schema Validation Guard
- **Wymaganie (PL):** Napisz walidator – sprawdź, czy wczytany JSON ma wymagane klucze (`'nazwa'`, `'wersja'`).
- **EN:** Write a validator asserting that imported JSON objects possess required schema keys (`'name'`, `'version'`).

---
[Powrót do Spisu Treści Części 2](../README.pl.md)

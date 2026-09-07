# Poziom 2: Pełna Lista 115 Zadań Automatyzacji
### Python w Inżynierii Systemowej i Cloud DevOps

> [!NOTE]
> 8 Modułów × Konkretne Zadania Praktyczne = 115 wyzwań automatyzacyjnych.
> Obejmuje pliki, pathlib, subprocess, JSON/CSV, requests, rich i usługi systemd.

[🇬🇧 English version (ALL_115_TASKS.md)](ALL_115_TASKS.md)

---

## Moduł 1: Praca z Plikami i Ścieżkami (open, os, pathlib)

1. **Print Current Working Directory**: Wypisz swoją bieżącą ścieżkę roboczą (`os.getcwd()`).  
   *EN:* Print your current working directory using `os.getcwd()`.
2. **Create Backup Directory**: Stwórz folder `test_backupy` w swoim katalogu domowym.  
   *EN:* Create directory `test_backups` in your home folder using `pathlib` or `os.mkdir()`.
3. **Create Batch Text Files**: W tym folderze stwórz 3 pliki tekstowe: `backup1.txt`, `backup2.txt`, `backup3.txt`.  
   *EN:* Inside `test_backups`, create 3 text files: `backup1.txt`, `backup2.txt`, `backup3.txt`.
4. **Write Timestamped Headers**: Do każdego pliku wpisz: `Backup z dnia: [dzisiejsza data]`.  
   *EN:* Write `Backup created on: [current date]` into each created file.
5. **Read and Print All Files**: Odczytaj zawartość wszystkich 3 plików i wypisz je na ekran.  
   *EN:* Read the contents of all 3 files and display them in the terminal.
6. **File Existence Verification**: Sprawdź, czy plik `nieistnieje.txt` istnieje – jeśli nie, wypisz komunikat.  
   *EN:* Check if `nonexistent.txt` exists; if not, output a clear status message.
7. **List Files by Extension**: Wypisz listę wszystkich plików `.txt` w folderze `test_backupy`.  
   *EN:* List all `.txt` files in directory `test_backups`.
8. **Rename File**: Zmień nazwę pliku `backup1.txt` na `backup1_old.txt`.  
   *EN:* Rename file `backup1.txt` to `backup1_old.txt`.
9. **Copy File**: Skopiuj plik `backup2.txt` do `backup2_kopia.txt`.  
   *EN:* Copy `backup2.txt` to `backup2_copy.txt` using `shutil.copy()`.
10. **Delete File Safely**: Usuń plik `backup3.txt`.  
   *EN:* Delete file `backup3.txt` verifying its removal.
11. **File Size Inspection**: Sprawdź rozmiar pliku `backup2.txt` w bajtach.  
   *EN:* Inspect the exact size of `backup2.txt` in bytes.
12. **Pathlib Resolution**: Używając `pathlib`, stwórz ścieżkę do `~/scripts/wp-status` i sprawdź, czy istnieje.  
   *EN:* Using `pathlib.Path`, resolve path to `~/scripts/wp-status` and check its existence.
13. **Filter Shell Scripts**: Wypisz wszystkie pliki w swoim katalogu domowym, które mają rozszerzenie `.sh`.  
   *EN:* List all files in your home directory that possess the `.sh` extension.
14. **Disk Free Space Function**: Napisz funkcję `przestrzen_dysku(sciezka)`, która zwraca wolne miejsce w GB.  
   *EN:* Write function `get_free_disk_space(path)` that returns available space in gigabytes (GB).
15. **Directory Manifest Generator**: Stwórz program, który listuje wszystkie pliki w folderze `~/backups-lite` i zapisuje ich nazwy do `lista_backupow.txt`.  
   *EN:* Build a utility scanning `~/backups-lite` and writing discovered filenames into `backup_manifest.txt`.

## Moduł 2: Funkcje Zaawansowane (*args, **kwargs, domknięcia, dekoratory)

1. **Variable Positional Sum**: Napisz funkcję `suma_wszystkich(*args)`, która przyjmuje dowolną liczbę liczb i zwraca ich sumę.  
   *EN:* Write function `sum_all(*args)` returning the arithmetic sum of any number of passed values.
2. **Variable Average Calculation**: Stwórz funkcję `srednia(*args)`, która liczy średnią (uwzględnij dzielenie przez zero).  
   *EN:* Write function `calculate_average(*args)` returning the arithmetic mean of passed arguments.
3. **Default Arguments Configuration**: Napisz funkcję `backup(folder, cel='~/backups', kompresja=True)` z domyślnymi argumentami.  
   *EN:* Write function `create_backup(source, target='~/backups', compress=True)`.
4. **Keyword Arguments Inspection**: Napisz funkcję `info_o_serwerze(**kwargs)`, która wypisuje wszystkie przekazane parametry w formacie `klucz: wartosc`.  
   *EN:* Write function `print_server_info(**kwargs)` printing each configuration key and value.
5. **Combined Signature Handler**: Stwórz funkcję `wykonaj_akcje(akcja, *foldery, **opcje)`, która łączy `*args` i `**kwargs`.  
   *EN:* Write function `dispatch(action, *targets, **options)` demonstrating combined argument handling.
6. **Type Validation Assertion**: Napisz funkcję `mnoz(a, b)`, która sprawdza typy argumentów i rzuca `TypeError`, jeśli nie są int/float.  
   *EN:* Write function `safe_multiply(a, b)` raising a `TypeError` if parameters are not numeric.
7. **Structured Log Writer**: Napisz funkcję `loguj(poziom='INFO', **dane)`, która zapisuje do pliku logi w formacie: `[DATA] [POZIOM] dane`.  
   *EN:* Write function `write_log(level='INFO', **data)` outputting entries: `[TIMESTAMP] [LEVEL] data`.
8. **Arguments Pair to Dictionary**: Stwórz funkcję `lista_do_dict(*args)`, która z `('name=Jack', 'age=35')` tworzy słownik.  
   *EN:* Write function `pairs_to_dict(*args)` transforming strings like `('name=Alex', 'age=30')` into a dictionary.
9. **Type Hints Signature**: Napisz funkcję z adnotacjami typów: `def podziel(a: float, b: float) -> float:`.  
   *EN:* Write a division function with complete type hints: `def safe_divide(a: float, b: float) -> float:`.
10. **Closure Memory Cache**: Stwórz funkcję `cache()`, która zapamiętuje wyniki poprzednich wywołań (użyj słownika wewnątrz funkcji).  
   *EN:* Create a closure `memoize()` that retains previous execution results inside an internal cache dictionary.
11. **Dynamic Config Updater**: Napisz funkcję `odswiez_config(**nowe)`, która aktualizuje globalny słownik `CONFIG`.  
   *EN:* Write function `update_config(**overrides)` that dynamically merges updates into a global `CONFIG` dict.
12. **Higher-Order Multiplier Factory**: Stwórz funkcję wyższego rzędu `razy_n(n)`, która zwraca funkcję mnożącą przez `n`.  
   *EN:* Build higher-order function `make_multiplier(factor)` returning a closure multiplying by `factor`.
13. **Execution Timing Decorator**: Napisz dekorator `@czas`, który mierzy czas wykonania funkcji.  
   *EN:* Write timing decorator `@measure_time` measuring and logging execution elapsed duration.
14. **Functional Mapping with Lambda**: Użyj `map()` i lambdy, aby zamienić listę napisów `['1', '2', '3']` na listę intów.  
   *EN:* Use `map()` and lambda to transform a list of strings `['1', '2', '3']` into a list of integers.
15. **Variadic Dictionary Merger**: Napisz funkcję `merge_dicts(*dicts)`, która łączy dowolną liczbę słowników (nadpisując klucze).  
   *EN:* Write function `merge_dicts(*dicts)` combining an arbitrary number of dictionaries with sequential overrides.

## Moduł 3: Moduły i Importy (Architektura i Pakiety)

1. **Math Helper Module**: Stwórz plik `kalkulator.py` z funkcjami `dodaj()`, `odejmij()`, `pomnoz()`, `podziel()`.  
   *EN:* Create module `calculator.py` with functions `add()`, `subtract()`, `multiply()`, `divide()`.
2. **Full Module Import**: W pliku `main.py` zaimportuj cały moduł `kalkulator` i użyj każdej funkcji.  
   *EN:* In `main.py`, import the entire `calculator` module and test each arithmetic function.
3. **Selective Function Import**: W nowym pliku zaimportuj tylko `dodaj` i `podziel` z `kalkulator`.  
   *EN:* In a new script, selectively import only `add` and `divide` from `calculator`.
4. **Package Architecture Initialization**: Stwórz folder `utils` z plikiem `__init__.py` i przenieś tam `kalkulator.py`.  
   *EN:* Create directory `utils` with `__init__.py` and relocate `calculator.py` inside it.
5. **Package Submodule Import**: Zaimportuj `kalkulator` z folderu `utils` używając `from utils import kalkulator`.  
   *EN:* Import `calculator` from `utils` using syntax `from utils import calculator`.
6. **Configuration Constant Module**: Stwórz plik `config.py` ze zmiennymi: `BACKUP_DIR = '~/backups'`, `RETENCJA_DNI = 14`.  
   *EN:* Create `config.py` declaring constants: `BACKUP_DIR = '~/backups'`, `RETENTION_DAYS = 14`.
7. **Configuration Import and Consumption**: Zaimportuj `config` w `main.py` i wypisz wartości zmiennych.  
   *EN:* Import `config` in `main.py` and print the active configuration constants.
8. **Import Aliasing**: Użyj `from config import BACKUP_DIR as BD` (alias).  
   *EN:* Import constant with alias: `from config import BACKUP_DIR as BD`.
9. **Dedicated Logger Module**: Stwórz moduł `logi.py` z funkcją `zapisz_log(tekst, poziom='INFO')`.  
   *EN:* Create `logger.py` with function `log_message(text, level='INFO')`.
10. **Integrated Logger Execution**: W `main.py` zaimportuj `logi` i wywołaj `zapisz_log('Start programu')`.  
   *EN:* In `main.py`, import `logger` and record: `log_message('Application initialized')`.
11. **Inspect Python Search Path**: Sprawdź, czy Python widzi Twój moduł – wypisz `sys.path`.  
   *EN:* Inspect Python module resolution paths by printing `sys.path` entries.
12. **Package Export Exposing in __init__**: Stwórz plik `__init__.py` w `utils`, który importuje `dodaj` i `podziel`.  
   *EN:* In `utils/__init__.py`, import `add` and `divide` so `from utils import add` works cleanly.
13. **Unit Self-Test Entry Guard**: Użyj `if __name__ == '__main__':` w `kalkulator.py` – dodaj testy funkcji.  
   *EN:* Add `if __name__ == '__main__':` in `calculator.py` with standalone self-tests.
14. **Module Load Notification Hook**: Stwórz moduł, który przy imporcie wypisuje `'Moduł załadowany'`.  
   *EN:* Create a module that prints `'Module successfully initialized'` upon import.
15. **Hot Reloading with importlib**: Użyj `importlib.reload()` do przeładowania modułu bez restartu Pythona.  
   *EN:* Use `importlib.reload()` to reload a modified module dynamically without interpreter restart.

## Moduł 4: Dane Strukturalne – JSON i CSV

1. **Dictionary to JSON File**: Stwórz słownik `serwer = {'nazwa': 'Ubuntu', 'wersja': '22.04', 'ram_gb': 8}` i zapisz go do `serwer.json`.  
   *EN:* Create dictionary `server = {'name': 'Ubuntu', 'version': '22.04', 'ram_gb': 8}` and dump to `server.json`.
2. **Parse and Iterate JSON**: Odczytaj `serwer.json` i wypisz wszystkie klucze i wartości.  
   *EN:* Read `server.json` and display all key-value configuration pairs.
3. **JSON Update and Persistence**: Zmodyfikuj słownik (dodaj `'dysk_gb': 100`) i zapisz ponownie do tego samego pliku.  
   *EN:* Modify dictionary (add `'disk_gb': 100`) and persist updates to `server.json`.
4. **Indented Multi-record JSON**: Stwórz listę słowników stron i zapisz do JSON z `indent=2`.  
   *EN:* Create list of website dicts and save to JSON with 2-space indentation formatting.
5. **JSON Filter Query**: Odczytaj listę stron i wypisz tylko te z wersją `6.2`.  
   *EN:* Read websites JSON inventory and filter items matching version `'6.2'`.
6. **CSV Header Initialization**: Stwórz plik CSV `strony.csv` z kolumnami: `nazwa`, `wersja`, `status`.  
   *EN:* Create CSV file `sites.csv` with headers: `name`, `version`, `status`.
7. **Append Rows to CSV**: Dodaj 3 wiersze danych do `strony.csv`.  
   *EN:* Append 3 rows of structured website records to `sites.csv`.
8. **DictReader CSV Parsing**: Odczytaj `strony.csv` i wypisz każdy wiersz jako słownik (`csv.DictReader`).  
   *EN:* Read `sites.csv` and yield each record as a dictionary via `csv.DictReader`.
9. **Filtered Search on CSV**: Znajdź w CSV wszystkie strony ze statusem `'Update needed'`.  
   *EN:* Find and print all site records in the CSV flagged with status `'Update needed'`.
10. **JSON to CSV Pipeline Converter**: Stwórz funkcję `json_do_csv(json_file, csv_file)`, która konwertuje plik JSON na CSV.  
   *EN:* Write function `json_to_csv(json_path, csv_path)` transforming JSON records into CSV format.
11. **CSV to JSON Pipeline Converter**: Stwórz funkcję `csv_do_json(csv_file, json_file)`.  
   *EN:* Write function `csv_to_json(csv_path, json_path)` converting CSV tables into JSON objects.
12. **ISO Datetime Serialization**: Zapisz do JSON datę i godzinę (`datetime.now().isoformat()`) wraz z dowolnymi danymi.  
   *EN:* Serialize current timestamp (`datetime.now().isoformat()`) alongside operational payload into JSON.
13. **Datetime Deserialization**: Odczytaj JSON zawierający datę i przekonwertuj string z powrotem na obiekt `datetime`.  
   *EN:* Parse ISO timestamp string from JSON back into a native Python `datetime` object.
14. **Multi-file JSON Combiner**: Stwórz program, który łączy dwa pliki JSON (listy) w jeden.  
   *EN:* Build a utility merging two JSON lists into a single consolidated JSON archive.
15. **Schema Validation Guard**: Napisz walidator – sprawdź, czy wczytany JSON ma wymagane klucze (`'nazwa'`, `'wersja'`).  
   *EN:* Write a validator asserting that imported JSON objects possess required schema keys (`'name'`, `'version'`).

## Moduł 5: Subprocess – Automatyzacja Powłoki i CLI

1. **Directory Listing Subprocess**: Uruchom `ls -la` z Pythona i wypisz wynik.  
   *EN:* Execute `ls -la` via Python `subprocess.run()` and print captured stdout.
2. **Capture Working Directory**: Uruchom `pwd` i zapisz wynik do zmiennej.  
   *EN:* Execute `pwd` and capture clean directory string in a variable.
3. **Ping Return Code Assertion**: Sprawdź, czy komenda `ping -c 1 google.com` się powiodła (returncode == 0).  
   *EN:* Verify network reachability by checking if `ping -c 1 8.8.8.8` returns code 0.
4. **Filtered Disk Space Query**: Uruchom `df -h` i wypisz tylko linie zawierające `/dev/sda`.  
   *EN:* Execute `df -h` and print only storage partitions containing `/dev/`.
5. **Custom Script Execution**: Uruchom swój skrypt `wp-status` i wypisz jego wynik.  
   *EN:* Execute local management script `wp-status` and stream output.
6. **Redirect Output to File**: Uruchom `wp-fleet` i zapisz wynik do pliku `raport_fleet.txt`.  
   *EN:* Execute `wp-fleet` and persist stdout to `fleet_report.txt`.
7. **Shell Redirection Operator**: Uruchom komendę z przekierowaniem (`shell=True`): `echo 'test' > test.txt`.  
   *EN:* Execute command with shell redirection: `echo 'pipeline active' > test.txt`.
8. **Database Backup Status**: Uruchom `mysql-backup-all` i sprawdź, czy zakończył się sukcesem.  
   *EN:* Execute `mysql-backup-all` simulation and verify process exit code.
9. **Execution Benchmark Timer**: Uruchom `wp-backup-lite` i zmierz czas wykonania.  
   *EN:* Execute command and measure precise execution elapsed time.
10. **Process Error Handling**: Uruchom komendę, która celowo zwróci błąd – obsłuż `CalledProcessError`.  
   *EN:* Execute invalid command intentionally and handle `subprocess.CalledProcessError`.
11. **Process Timeout Guard**: Uruchom komendę z timeoutem (np. `timeout=5` dla `sleep 10`).  
   *EN:* Execute process with strict timeout (e.g. `timeout=3` on long-running task).
12. **Output Line Count Parsing**: Uruchom `wp-cli-validator` i sparsuj wynik – wypisz tylko liczbę znalezionych stron.  
   *EN:* Execute CLI utility and parse output to count total discovered sites.
13. **Script Discovery Validator**: Stwórz funkcję `czy_skrypt_istnieje(nazwa)`, która sprawdza czy skrypt WSMS jest w `~/scripts/`.  
   *EN:* Write function `script_exists(name)` checking if automation script exists in `~/scripts/`.
14. **Structured Line Splitter**: Uruchom `backup-list` i zapisz wynik jako listę stringów.  
   *EN:* Capture command output and transform it into a list of stripped string lines.
15. **Consolidated System Health Report**: Stwórz własną komendę `wp-health-check`, która łączy wyniki w jeden raport JSON.  
   *EN:* Build `health_check` uniting disk space, status, and fleet metrics into a single JSON report.

## Moduł 6: Mini-Projekt – Menedżer Backupów CLI

1. **List Backups Engine**: Stwórz plik `backup_manager.py` z funkcją `list_backups(folder)`.  
   *EN:* Create `backup_manager.py` with function `list_backups(directory)`.
2. **Aggregate Archive Statistics**: Dodaj funkcję `stats(backupy)`, która zwraca liczbę, łączny rozmiar, najstarszy i najnowszy plik.  
   *EN:* Add function `get_stats(files)` returning count, total size, oldest, and newest archive.
3. **Retention Cleaning Policy**: Dodaj funkcję `clean_old(folder, days=14)`, która usuwa pliki starsze niż `days`.  
   *EN:* Add function `clean_old(folder, days=14)` deleting archives older than retention threshold.
4. **Safe Dry-Run Flag**: Dodaj opcję `--dry-run` – tylko wypisuje, co by usunęła.  
   *EN:* Implement `--dry-run` parameter printing scheduled deletions without modifying disk.
5. **Cleaning Audit JSON Log**: Dodaj zapisywanie raportu z czyszczenia do JSON.  
   *EN:* Persist rotation audit trail to JSON: deleted items, timestamp, and freed bytes.
6. **Multi-Directory Federation**: Dodaj obsługę wielu folderów z backupami.  
   *EN:* Support scanning across directories: `~/backups-lite`, `~/backups-full`, `~/mysql-backups`.
7. **Storage Delta Calculation**: Dodaj sprawdzanie wolnego miejsca przed i po czyszczeniu.  
   *EN:* Measure and display free storage delta before and after rotation execution.
8. **Low Storage Warning Threshold**: Dodaj ostrzeżenie, jeśli wolnego miejsca jest mniej niż 10%.  
   *EN:* Issue high-priority alert if available storage falls below 10% capacity.
9. **Interactive Console Menu**: Dodaj interaktywne menu: `1. Listuj`, `2. Statystyki`, `3. Czyść`, `4. Wyjście`.  
   *EN:* Provide menu: `1. List`, `2. Stats`, `3. Clean`, `4. Exit`.
10. **Custom Retention Period Flag**: Dodaj możliwość podania własnej liczby dni przy czyszczeniu.  
   *EN:* Allow user to pass custom retention period (e.g. `--days 30`).
11. **Persistent File Logging**: Dodaj logowanie operacji do pliku (nie tylko na ekran).  
   *EN:* Route rotation logs to rotating log file on disk.
12. **Rich Table Presentation**: Użyj formatowania tabelarycznego do wyświetlania wyników.  
   *EN:* Format backup status reports in colorful ASCII terminal tables.
13. **Machine-Readable JSON Output**: Dodaj opcję `--json`, która wypisuje statystyki w formacie JSON.  
   *EN:* Add `--json` flag outputting statistics in pure JSON format for monitoring integrations.
14. **File Exclusion Pattern**: Dodaj możliwość wykluczenia konkretnych plików z czyszczenia.  
   *EN:* Allow excluding protected archives (e.g. `*.important` or `*golden*`).
15. **Standalone Executable CLI**: Przygotuj skrypt tak, by działał jako bezpośrednia komenda terminala.  
   *EN:* Package utility with shebang `#!/usr/bin/env python3` and execution permissions.

## Moduł 7: Biblioteki Zewnętrzne (requests, rich, dotenv)

1. **HTTP GET Request**: Zainstaluj `requests` i pobierz zawartość strony `https://api.github.com`.  
   *EN:* Install `requests` and fetch payload from `https://api.github.com`.
2. **Public API Profile Inspection**: Pobierz informacje o profilu GitHub i wypisz liczbę publicznych repozytoriów.  
   *EN:* Query GitHub user API endpoint and print public repository count.
3. **Iterate Repository Names**: Pobierz listę repozytoriów i wypisz ich nazwy.  
   *EN:* Fetch repository list from public API and display names sequentially.
4. **HTTP Status Code Check**: Sprawdź status odpowiedzi – jeśli nie 200, wypisz błąd.  
   *EN:* Inspect response status code and handle non-200 responses gracefully.
5. **Request Timeout Configuration**: Dodaj timeout do requesta (np. `timeout=5`).  
   *EN:* Configure explicit timeout parameter (e.g. `timeout=5.0`) to avoid hanging sockets.
6. **Rich Styled Console Print**: Zainstaluj `rich` i wypisz kolorowy komunikat: `✅ Sukces!` na zielono.  
   *EN:* Install `rich` and print styled green success status notification.
7. **Rich Formatted Table**: Stwórz tabelę używając `rich` z danymi skryptów serwerowych.  
   *EN:* Render formatted terminal table displaying script names, statuses, and descriptions.
8. **Rich Progress Bar Animation**: Dodaj pasek postępu (`Progress`) symulujący przetwarzanie 10 stron.  
   *EN:* Implement `rich.progress.Progress` bar simulating batch site maintenance.
9. **Rich Boxed Panel Display**: Użyj `rich.panel` do wyświetlenia wyniku skryptu w ramce.  
   *EN:* Render script diagnostic output inside a styled `rich.panel.Panel` border.
10. **Environment Variables via Dotenv**: Zainstaluj `python-dotenv` i wczytaj zmienne środowiskowe z pliku `.env`.  
   *EN:* Install `python-dotenv` and load environment variables from `.env`.
11. **Read Environment Variable**: Użyj `os.getenv()` do pobrania zmiennej.  
   *EN:* Read system variable using `os.getenv('BACKUP_DIR', '/default/path')`.
12. **Configure Retention via .env**: Stwórz plik `.env` z `RETENCJA_DNI=30` i wczytaj go w programie.  
   *EN:* Define `RETENTION_DAYS=30` in `.env` and consume in Python application.
13. **Webhook POST Simulation**: Użyj `requests` do wysłania POST (np. do webhooka – symulacja).  
   *EN:* Dispatch HTTP POST request with JSON payload to simulated monitoring webhook.
14. **Combined Process and Rich Box**: Połącz `subprocess` i `rich` – uruchom polecenie i wyświetl w kolorowej ramce.  
   *EN:* Execute status command via subprocess and wrap output inside a rich bordered panel.
15. **Periodic Uptime Ping Monitor**: Stwórz prosty monitoring – co 5 sekund sprawdza status strony i wyświetla ✅ lub ❌.  
   *EN:* Build periodic site uptime checker executing request every 5 seconds with status indicators.

## Moduł 8: Zadania Integracyjne – Łączenie Wszystkiego

1. **Core Monitor Daemon**: Stwórz program `wsms_monitor.py` koordynujący sprawdzanie stanu systemu.  
   *EN:* Build `server_monitor.py` coordinating disk, load, and service checks into a single report.
2. **Fleet Maintenance Inspector**: Rozszerz program o sprawdzanie, czy któraś strona wymaga aktualizacji.  
   *EN:* Integrate site update checks into monitoring pipeline.
3. **Automatic Storage Purge Trigger**: Dodaj automatyczne czyszczenie backupów, jeśli dysk jest zapełniony w >80%.  
   *EN:* Trigger automatic backup cleaning when partition disk usage exceeds 80%.
4. **Email Notification Dispatcher**: Dodaj wysyłanie raportu na email (symulacja – zapis do pliku `.email`).  
   *EN:* Simulate alert notification dispatch to email file queue upon critical error.
5. **Scheduled Monitoring Loop**: Stwórz harmonogram zadań – program działa w pętli, co godzinę robi monitoring.  
   *EN:* Implement recurring hourly monitoring execution loop with clean termination handler.
6. **INI Configuration Parser**: Dodaj plik konfiguracyjny `wsms_monitor.ini` (użyj `configparser`).  
   *EN:* Read server settings from `monitor.ini` using Python standard `configparser`.
7. **Rotating File Log Handler**: Dodaj logowanie do pliku z rotacją (nowy plik dziennie).  
   *EN:* Configure `logging.handlers.TimedRotatingFileHandler` generating daily log archives.
8. **Standard Packaging Setup**: Stwórz instalator Pythona (`pyproject.toml`), który instaluje zależności.  
   *EN:* Create `pyproject.toml` declaring project metadata, dependencies, and entry scripts.
9. **Systemd Service Definition**: Przygotuj skrypt do uruchamiania jako usługa systemd (dla Ubuntu).  
   *EN:* Craft a Linux systemd service unit file to manage the monitoring script as a background daemon.
10. **Production README Documentation**: Stwórz dokumentację w `README.md` z opisem instalacji i użycia.  
   *EN:* Author complete deployment, configuration, and troubleshooting guide in `README.md`.

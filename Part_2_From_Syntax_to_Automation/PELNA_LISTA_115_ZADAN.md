# Stage 2: All 115 Tasks / Poziom 2: Wszystkie 115 Zadań

- [🇬🇧 English Version: ALL_115_TASKS.md](ALL_115_TASKS.md)
- [🇵🇱 Wersja Polska: PELNA_LISTA_115_ZADAN.pl.md](PELNA_LISTA_115_ZADAN.pl.md)

---


[🇵🇱 Polska wersja (PELNA_LISTA_115_ZADAN.pl.md)](PELNA_LISTA_115_ZADAN.pl.md)

---

## Module 1: Working with Files & Paths (open, os, pathlib)

1. **Print Current Working Directory**: Print your current working directory using `os.getcwd()`.  
   *PL:* Wypisz swoją bieżącą ścieżkę roboczą (`os.getcwd()`).
2. **Create Backup Directory**: Create directory `test_backups` in your home folder using `pathlib` or `os.mkdir()`.  
   *PL:* Stwórz folder `test_backupy` w swoim katalogu domowym.
3. **Create Batch Text Files**: Inside `test_backups`, create 3 text files: `backup1.txt`, `backup2.txt`, `backup3.txt`.  
   *PL:* W tym folderze stwórz 3 pliki tekstowe: `backup1.txt`, `backup2.txt`, `backup3.txt`.
4. **Write Timestamped Headers**: Write `Backup created on: [current date]` into each created file.  
   *PL:* Do każdego pliku wpisz: `Backup z dnia: [dzisiejsza data]`.
5. **Read and Print All Files**: Read the contents of all 3 files and display them in the terminal.  
   *PL:* Odczytaj zawartość wszystkich 3 plików i wypisz je na ekran.
6. **File Existence Verification**: Check if `nonexistent.txt` exists; if not, output a clear status message.  
   *PL:* Sprawdź, czy plik `nieistnieje.txt` istnieje – jeśli nie, wypisz komunikat.
7. **List Files by Extension**: List all `.txt` files in directory `test_backups`.  
   *PL:* Wypisz listę wszystkich plików `.txt` w folderze `test_backupy`.
8. **Rename File**: Rename file `backup1.txt` to `backup1_old.txt`.  
   *PL:* Zmień nazwę pliku `backup1.txt` na `backup1_old.txt`.
9. **Copy File**: Copy `backup2.txt` to `backup2_copy.txt` using `shutil.copy()`.  
   *PL:* Skopiuj plik `backup2.txt` do `backup2_kopia.txt`.
10. **Delete File Safely**: Delete file `backup3.txt` verifying its removal.  
   *PL:* Usuń plik `backup3.txt`.
11. **File Size Inspection**: Inspect the exact size of `backup2.txt` in bytes.  
   *PL:* Sprawdź rozmiar pliku `backup2.txt` w bajtach.
12. **Pathlib Resolution**: Using `pathlib.Path`, resolve path to `~/scripts/wp-status` and check its existence.  
   *PL:* Używając `pathlib`, stwórz ścieżkę do `~/scripts/wp-status` i sprawdź, czy istnieje.
13. **Filter Shell Scripts**: List all files in your home directory that possess the `.sh` extension.  
   *PL:* Wypisz wszystkie pliki w swoim katalogu domowym, które mają rozszerzenie `.sh`.
14. **Disk Free Space Function**: Write function `get_free_disk_space(path)` that returns available space in gigabytes (GB).  
   *PL:* Napisz funkcję `przestrzen_dysku(sciezka)`, która zwraca wolne miejsce w GB.
15. **Directory Manifest Generator**: Build a utility scanning `~/backups-lite` and writing discovered filenames into `backup_manifest.txt`.  
   *PL:* Stwórz program, który listuje wszystkie pliki w folderze `~/backups-lite` i zapisuje ich nazwy do `lista_backupow.txt`.

## Module 2: Advanced Functions (*args, **kwargs, Closures, Decorators)

1. **Variable Positional Sum**: Write function `sum_all(*args)` returning the arithmetic sum of any number of passed values.  
   *PL:* Napisz funkcję `suma_wszystkich(*args)`, która przyjmuje dowolną liczbę liczb i zwraca ich sumę.
2. **Variable Average Calculation**: Write function `calculate_average(*args)` returning the arithmetic mean of passed arguments.  
   *PL:* Stwórz funkcję `srednia(*args)`, która liczy średnią (uwzględnij dzielenie przez zero).
3. **Default Arguments Configuration**: Write function `create_backup(source, target='~/backups', compress=True)`.  
   *PL:* Napisz funkcję `backup(folder, cel='~/backups', kompresja=True)` z domyślnymi argumentami.
4. **Keyword Arguments Inspection**: Write function `print_server_info(**kwargs)` printing each configuration key and value.  
   *PL:* Napisz funkcję `info_o_serwerze(**kwargs)`, która wypisuje wszystkie przekazane parametry w formacie `klucz: wartosc`.
5. **Combined Signature Handler**: Write function `dispatch(action, *targets, **options)` demonstrating combined argument handling.  
   *PL:* Stwórz funkcję `wykonaj_akcje(akcja, *foldery, **opcje)`, która łączy `*args` i `**kwargs`.
6. **Type Validation Assertion**: Write function `safe_multiply(a, b)` raising a `TypeError` if parameters are not numeric.  
   *PL:* Napisz funkcję `mnoz(a, b)`, która sprawdza typy argumentów i rzuca `TypeError`, jeśli nie są int/float.
7. **Structured Log Writer**: Write function `write_log(level='INFO', **data)` outputting entries: `[TIMESTAMP] [LEVEL] data`.  
   *PL:* Napisz funkcję `loguj(poziom='INFO', **dane)`, która zapisuje do pliku logi w formacie: `[DATA] [POZIOM] dane`.
8. **Arguments Pair to Dictionary**: Write function `pairs_to_dict(*args)` transforming strings like `('name=Alex', 'age=30')` into a dictionary.  
   *PL:* Stwórz funkcję `lista_do_dict(*args)`, która z `('name=Jack', 'age=35')` tworzy słownik.
9. **Type Hints Signature**: Write a division function with complete type hints: `def safe_divide(a: float, b: float) -> float:`.  
   *PL:* Napisz funkcję z adnotacjami typów: `def podziel(a: float, b: float) -> float:`.
10. **Closure Memory Cache**: Create a closure `memoize()` that retains previous execution results inside an internal cache dictionary.  
   *PL:* Stwórz funkcję `cache()`, która zapamiętuje wyniki poprzednich wywołań (użyj słownika wewnątrz funkcji).
11. **Dynamic Config Updater**: Write function `update_config(**overrides)` that dynamically merges updates into a global `CONFIG` dict.  
   *PL:* Napisz funkcję `odswiez_config(**nowe)`, która aktualizuje globalny słownik `CONFIG`.
12. **Higher-Order Multiplier Factory**: Build higher-order function `make_multiplier(factor)` returning a closure multiplying by `factor`.  
   *PL:* Stwórz funkcję wyższego rzędu `razy_n(n)`, która zwraca funkcję mnożącą przez `n`.
13. **Execution Timing Decorator**: Write timing decorator `@measure_time` measuring and logging execution elapsed duration.  
   *PL:* Napisz dekorator `@czas`, który mierzy czas wykonania funkcji.
14. **Functional Mapping with Lambda**: Use `map()` and lambda to transform a list of strings `['1', '2', '3']` into a list of integers.  
   *PL:* Użyj `map()` i lambdy, aby zamienić listę napisów `['1', '2', '3']` na listę intów.
15. **Variadic Dictionary Merger**: Write function `merge_dicts(*dicts)` combining an arbitrary number of dictionaries with sequential overrides.  
   *PL:* Napisz funkcję `merge_dicts(*dicts)`, która łączy dowolną liczbę słowników (nadpisując klucze).

## Module 3: Modules & Imports (Architecture & Packaging)

1. **Math Helper Module**: Create module `calculator.py` with functions `add()`, `subtract()`, `multiply()`, `divide()`.  
   *PL:* Stwórz plik `kalkulator.py` z funkcjami `dodaj()`, `odejmij()`, `pomnoz()`, `podziel()`.
2. **Full Module Import**: In `main.py`, import the entire `calculator` module and test each arithmetic function.  
   *PL:* W pliku `main.py` zaimportuj cały moduł `kalkulator` i użyj każdej funkcji.
3. **Selective Function Import**: In a new script, selectively import only `add` and `divide` from `calculator`.  
   *PL:* W nowym pliku zaimportuj tylko `dodaj` i `podziel` z `kalkulator`.
4. **Package Architecture Initialization**: Create directory `utils` with `__init__.py` and relocate `calculator.py` inside it.  
   *PL:* Stwórz folder `utils` z plikiem `__init__.py` i przenieś tam `kalkulator.py`.
5. **Package Submodule Import**: Import `calculator` from `utils` using syntax `from utils import calculator`.  
   *PL:* Zaimportuj `kalkulator` z folderu `utils` używając `from utils import kalkulator`.
6. **Configuration Constant Module**: Create `config.py` declaring constants: `BACKUP_DIR = '~/backups'`, `RETENTION_DAYS = 14`.  
   *PL:* Stwórz plik `config.py` ze zmiennymi: `BACKUP_DIR = '~/backups'`, `RETENCJA_DNI = 14`.
7. **Configuration Import and Consumption**: Import `config` in `main.py` and print the active configuration constants.  
   *PL:* Zaimportuj `config` w `main.py` i wypisz wartości zmiennych.
8. **Import Aliasing**: Import constant with alias: `from config import BACKUP_DIR as BD`.  
   *PL:* Użyj `from config import BACKUP_DIR as BD` (alias).
9. **Dedicated Logger Module**: Create `logger.py` with function `log_message(text, level='INFO')`.  
   *PL:* Stwórz moduł `logi.py` z funkcją `zapisz_log(tekst, poziom='INFO')`.
10. **Integrated Logger Execution**: In `main.py`, import `logger` and record: `log_message('Application initialized')`.  
   *PL:* W `main.py` zaimportuj `logi` i wywołaj `zapisz_log('Start programu')`.
11. **Inspect Python Search Path**: Inspect Python module resolution paths by printing `sys.path` entries.  
   *PL:* Sprawdź, czy Python widzi Twój moduł – wypisz `sys.path`.
12. **Package Export Exposing in __init__**: In `utils/__init__.py`, import `add` and `divide` so `from utils import add` works cleanly.  
   *PL:* Stwórz plik `__init__.py` w `utils`, który importuje `dodaj` i `podziel`.
13. **Unit Self-Test Entry Guard**: Add `if __name__ == '__main__':` in `calculator.py` with standalone self-tests.  
   *PL:* Użyj `if __name__ == '__main__':` w `kalkulator.py` – dodaj testy funkcji.
14. **Module Load Notification Hook**: Create a module that prints `'Module successfully initialized'` upon import.  
   *PL:* Stwórz moduł, który przy imporcie wypisuje `'Moduł załadowany'`.
15. **Hot Reloading with importlib**: Use `importlib.reload()` to reload a modified module dynamically without interpreter restart.  
   *PL:* Użyj `importlib.reload()` do przeładowania modułu bez restartu Pythona.

## Module 4: Structured Data — JSON & CSV

1. **Dictionary to JSON File**: Create dictionary `server = {'name': 'Ubuntu', 'version': '22.04', 'ram_gb': 8}` and dump to `server.json`.  
   *PL:* Stwórz słownik `serwer = {'nazwa': 'Ubuntu', 'wersja': '22.04', 'ram_gb': 8}` i zapisz go do `serwer.json`.
2. **Parse and Iterate JSON**: Read `server.json` and display all key-value configuration pairs.  
   *PL:* Odczytaj `serwer.json` i wypisz wszystkie klucze i wartości.
3. **JSON Update and Persistence**: Modify dictionary (add `'disk_gb': 100`) and persist updates to `server.json`.  
   *PL:* Zmodyfikuj słownik (dodaj `'dysk_gb': 100`) i zapisz ponownie do tego samego pliku.
4. **Indented Multi-record JSON**: Create list of website dicts and save to JSON with 2-space indentation formatting.  
   *PL:* Stwórz listę słowników stron i zapisz do JSON z `indent=2`.
5. **JSON Filter Query**: Read websites JSON inventory and filter items matching version `'6.2'`.  
   *PL:* Odczytaj listę stron i wypisz tylko te z wersją `6.2`.
6. **CSV Header Initialization**: Create CSV file `sites.csv` with headers: `name`, `version`, `status`.  
   *PL:* Stwórz plik CSV `strony.csv` z kolumnami: `nazwa`, `wersja`, `status`.
7. **Append Rows to CSV**: Append 3 rows of structured website records to `sites.csv`.  
   *PL:* Dodaj 3 wiersze danych do `strony.csv`.
8. **DictReader CSV Parsing**: Read `sites.csv` and yield each record as a dictionary via `csv.DictReader`.  
   *PL:* Odczytaj `strony.csv` i wypisz każdy wiersz jako słownik (`csv.DictReader`).
9. **Filtered Search on CSV**: Find and print all site records in the CSV flagged with status `'Update needed'`.  
   *PL:* Znajdź w CSV wszystkie strony ze statusem `'Update needed'`.
10. **JSON to CSV Pipeline Converter**: Write function `json_to_csv(json_path, csv_path)` transforming JSON records into CSV format.  
   *PL:* Stwórz funkcję `json_do_csv(json_file, csv_file)`, która konwertuje plik JSON na CSV.
11. **CSV to JSON Pipeline Converter**: Write function `csv_to_json(csv_path, json_path)` converting CSV tables into JSON objects.  
   *PL:* Stwórz funkcję `csv_do_json(csv_file, json_file)`.
12. **ISO Datetime Serialization**: Serialize current timestamp (`datetime.now().isoformat()`) alongside operational payload into JSON.  
   *PL:* Zapisz do JSON datę i godzinę (`datetime.now().isoformat()`) wraz z dowolnymi danymi.
13. **Datetime Deserialization**: Parse ISO timestamp string from JSON back into a native Python `datetime` object.  
   *PL:* Odczytaj JSON zawierający datę i przekonwertuj string z powrotem na obiekt `datetime`.
14. **Multi-file JSON Combiner**: Build a utility merging two JSON lists into a single consolidated JSON archive.  
   *PL:* Stwórz program, który łączy dwa pliki JSON (listy) w jeden.
15. **Schema Validation Guard**: Write a validator asserting that imported JSON objects possess required schema keys (`'name'`, `'version'`).  
   *PL:* Napisz walidator – sprawdź, czy wczytany JSON ma wymagane klucze (`'nazwa'`, `'wersja'`).

## Module 5: Subprocess & Shell Automation

1. **Directory Listing Subprocess**: Execute `ls -la` via Python `subprocess.run()` and print captured stdout.  
   *PL:* Uruchom `ls -la` z Pythona i wypisz wynik.
2. **Capture Working Directory**: Execute `pwd` and capture clean directory string in a variable.  
   *PL:* Uruchom `pwd` i zapisz wynik do zmiennej.
3. **Ping Return Code Assertion**: Verify network reachability by checking if `ping -c 1 8.8.8.8` returns code 0.  
   *PL:* Sprawdź, czy komenda `ping -c 1 google.com` się powiodła (returncode == 0).
4. **Filtered Disk Space Query**: Execute `df -h` and print only storage partitions containing `/dev/`.  
   *PL:* Uruchom `df -h` i wypisz tylko linie zawierające `/dev/sda`.
5. **Custom Script Execution**: Execute local management script `wp-status` and stream output.  
   *PL:* Uruchom swój skrypt `wp-status` i wypisz jego wynik.
6. **Redirect Output to File**: Execute `wp-fleet` and persist stdout to `fleet_report.txt`.  
   *PL:* Uruchom `wp-fleet` i zapisz wynik do pliku `raport_fleet.txt`.
7. **Shell Redirection Operator**: Execute command with shell redirection: `echo 'pipeline active' > test.txt`.  
   *PL:* Uruchom komendę z przekierowaniem (`shell=True`): `echo 'test' > test.txt`.
8. **Database Backup Status**: Execute `mysql-backup-all` simulation and verify process exit code.  
   *PL:* Uruchom `mysql-backup-all` i sprawdź, czy zakończył się sukcesem.
9. **Execution Benchmark Timer**: Execute command and measure precise execution elapsed time.  
   *PL:* Uruchom `wp-backup-lite` i zmierz czas wykonania.
10. **Process Error Handling**: Execute invalid command intentionally and handle `subprocess.CalledProcessError`.  
   *PL:* Uruchom komendę, która celowo zwróci błąd – obsłuż `CalledProcessError`.
11. **Process Timeout Guard**: Execute process with strict timeout (e.g. `timeout=3` on long-running task).  
   *PL:* Uruchom komendę z timeoutem (np. `timeout=5` dla `sleep 10`).
12. **Output Line Count Parsing**: Execute CLI utility and parse output to count total discovered sites.  
   *PL:* Uruchom `wp-cli-validator` i sparsuj wynik – wypisz tylko liczbę znalezionych stron.
13. **Script Discovery Validator**: Write function `script_exists(name)` checking if automation script exists in `~/scripts/`.  
   *PL:* Stwórz funkcję `czy_skrypt_istnieje(nazwa)`, która sprawdza czy skrypt WSMS jest w `~/scripts/`.
14. **Structured Line Splitter**: Capture command output and transform it into a list of stripped string lines.  
   *PL:* Uruchom `backup-list` i zapisz wynik jako listę stringów.
15. **Consolidated System Health Report**: Build `health_check` uniting disk space, status, and fleet metrics into a single JSON report.  
   *PL:* Stwórz własną komendę `wp-health-check`, która łączy wyniki w jeden raport JSON.

## Module 6: Capstone Mini-Project — Backup Manager CLI

1. **List Backups Engine**: Create `backup_manager.py` with function `list_backups(directory)`.  
   *PL:* Stwórz plik `backup_manager.py` z funkcją `list_backups(folder)`.
2. **Aggregate Archive Statistics**: Add function `get_stats(files)` returning count, total size, oldest, and newest archive.  
   *PL:* Dodaj funkcję `stats(backupy)`, która zwraca liczbę, łączny rozmiar, najstarszy i najnowszy plik.
3. **Retention Cleaning Policy**: Add function `clean_old(folder, days=14)` deleting archives older than retention threshold.  
   *PL:* Dodaj funkcję `clean_old(folder, days=14)`, która usuwa pliki starsze niż `days`.
4. **Safe Dry-Run Flag**: Implement `--dry-run` parameter printing scheduled deletions without modifying disk.  
   *PL:* Dodaj opcję `--dry-run` – tylko wypisuje, co by usunęła.
5. **Cleaning Audit JSON Log**: Persist rotation audit trail to JSON: deleted items, timestamp, and freed bytes.  
   *PL:* Dodaj zapisywanie raportu z czyszczenia do JSON.
6. **Multi-Directory Federation**: Support scanning across directories: `~/backups-lite`, `~/backups-full`, `~/mysql-backups`.  
   *PL:* Dodaj obsługę wielu folderów z backupami.
7. **Storage Delta Calculation**: Measure and display free storage delta before and after rotation execution.  
   *PL:* Dodaj sprawdzanie wolnego miejsca przed i po czyszczeniu.
8. **Low Storage Warning Threshold**: Issue high-priority alert if available storage falls below 10% capacity.  
   *PL:* Dodaj ostrzeżenie, jeśli wolnego miejsca jest mniej niż 10%.
9. **Interactive Console Menu**: Provide menu: `1. List`, `2. Stats`, `3. Clean`, `4. Exit`.  
   *PL:* Dodaj interaktywne menu: `1. Listuj`, `2. Statystyki`, `3. Czyść`, `4. Wyjście`.
10. **Custom Retention Period Flag**: Allow user to pass custom retention period (e.g. `--days 30`).  
   *PL:* Dodaj możliwość podania własnej liczby dni przy czyszczeniu.
11. **Persistent File Logging**: Route rotation logs to rotating log file on disk.  
   *PL:* Dodaj logowanie operacji do pliku (nie tylko na ekran).
12. **Rich Table Presentation**: Format backup status reports in colorful ASCII terminal tables.  
   *PL:* Użyj formatowania tabelarycznego do wyświetlania wyników.
13. **Machine-Readable JSON Output**: Add `--json` flag outputting statistics in pure JSON format for monitoring integrations.  
   *PL:* Dodaj opcję `--json`, która wypisuje statystyki w formacie JSON.
14. **File Exclusion Pattern**: Allow excluding protected archives (e.g. `*.important` or `*golden*`).  
   *PL:* Dodaj możliwość wykluczenia konkretnych plików z czyszczenia.
15. **Standalone Executable CLI**: Package utility with shebang `#!/usr/bin/env python3` and execution permissions.  
   *PL:* Przygotuj skrypt tak, by działał jako bezpośrednia komenda terminala.

## Module 7: External Libraries (requests, rich, dotenv)

1. **HTTP GET Request**: Install `requests` and fetch payload from `https://api.github.com`.  
   *PL:* Zainstaluj `requests` i pobierz zawartość strony `https://api.github.com`.
2. **Public API Profile Inspection**: Query GitHub user API endpoint and print public repository count.  
   *PL:* Pobierz informacje o profilu GitHub i wypisz liczbę publicznych repozytoriów.
3. **Iterate Repository Names**: Fetch repository list from public API and display names sequentially.  
   *PL:* Pobierz listę repozytoriów i wypisz ich nazwy.
4. **HTTP Status Code Check**: Inspect response status code and handle non-200 responses gracefully.  
   *PL:* Sprawdź status odpowiedzi – jeśli nie 200, wypisz błąd.
5. **Request Timeout Configuration**: Configure explicit timeout parameter (e.g. `timeout=5.0`) to avoid hanging sockets.  
   *PL:* Dodaj timeout do requesta (np. `timeout=5`).
6. **Rich Styled Console Print**: Install `rich` and print styled green success status notification.  
   *PL:* Zainstaluj `rich` i wypisz kolorowy komunikat: `✅ Sukces!` na zielono.
7. **Rich Formatted Table**: Render formatted terminal table displaying script names, statuses, and descriptions.  
   *PL:* Stwórz tabelę używając `rich` z danymi skryptów serwerowych.
8. **Rich Progress Bar Animation**: Implement `rich.progress.Progress` bar simulating batch site maintenance.  
   *PL:* Dodaj pasek postępu (`Progress`) symulujący przetwarzanie 10 stron.
9. **Rich Boxed Panel Display**: Render script diagnostic output inside a styled `rich.panel.Panel` border.  
   *PL:* Użyj `rich.panel` do wyświetlenia wyniku skryptu w ramce.
10. **Environment Variables via Dotenv**: Install `python-dotenv` and load environment variables from `.env`.  
   *PL:* Zainstaluj `python-dotenv` i wczytaj zmienne środowiskowe z pliku `.env`.
11. **Read Environment Variable**: Read system variable using `os.getenv('BACKUP_DIR', '/default/path')`.  
   *PL:* Użyj `os.getenv()` do pobrania zmiennej.
12. **Configure Retention via .env**: Define `RETENTION_DAYS=30` in `.env` and consume in Python application.  
   *PL:* Stwórz plik `.env` z `RETENCJA_DNI=30` i wczytaj go w programie.
13. **Webhook POST Simulation**: Dispatch HTTP POST request with JSON payload to simulated monitoring webhook.  
   *PL:* Użyj `requests` do wysłania POST (np. do webhooka – symulacja).
14. **Combined Process and Rich Box**: Execute status command via subprocess and wrap output inside a rich bordered panel.  
   *PL:* Połącz `subprocess` i `rich` – uruchom polecenie i wyświetl w kolorowej ramce.
15. **Periodic Uptime Ping Monitor**: Build periodic site uptime checker executing request every 5 seconds with status indicators.  
   *PL:* Stwórz prosty monitoring – co 5 sekund sprawdza status strony i wyświetla ✅ lub ❌.

## Module 8: Complete System Integration (Capstones)

1. **Core Monitor Daemon**: Build `server_monitor.py` coordinating disk, load, and service checks into a single report.  
   *PL:* Stwórz program `wsms_monitor.py` koordynujący sprawdzanie stanu systemu.
2. **Fleet Maintenance Inspector**: Integrate site update checks into monitoring pipeline.  
   *PL:* Rozszerz program o sprawdzanie, czy któraś strona wymaga aktualizacji.
3. **Automatic Storage Purge Trigger**: Trigger automatic backup cleaning when partition disk usage exceeds 80%.  
   *PL:* Dodaj automatyczne czyszczenie backupów, jeśli dysk jest zapełniony w >80%.
4. **Email Notification Dispatcher**: Simulate alert notification dispatch to email file queue upon critical error.  
   *PL:* Dodaj wysyłanie raportu na email (symulacja – zapis do pliku `.email`).
5. **Scheduled Monitoring Loop**: Implement recurring hourly monitoring execution loop with clean termination handler.  
   *PL:* Stwórz harmonogram zadań – program działa w pętli, co godzinę robi monitoring.
6. **INI Configuration Parser**: Read server settings from `monitor.ini` using Python standard `configparser`.  
   *PL:* Dodaj plik konfiguracyjny `wsms_monitor.ini` (użyj `configparser`).
7. **Rotating File Log Handler**: Configure `logging.handlers.TimedRotatingFileHandler` generating daily log archives.  
   *PL:* Dodaj logowanie do pliku z rotacją (nowy plik dziennie).
8. **Standard Packaging Setup**: Create `pyproject.toml` declaring project metadata, dependencies, and entry scripts.  
   *PL:* Stwórz instalator Pythona (`pyproject.toml`), który instaluje zależności.
9. **Systemd Service Definition**: Craft a Linux systemd service unit file to manage the monitoring script as a background daemon.  
   *PL:* Przygotuj skrypt do uruchamiania jako usługa systemd (dla Ubuntu).
10. **Production README Documentation**: Author complete deployment, configuration, and troubleshooting guide in `README.md`.  
   *PL:* Stwórz dokumentację w `README.md` z opisem instalacji i użycia.


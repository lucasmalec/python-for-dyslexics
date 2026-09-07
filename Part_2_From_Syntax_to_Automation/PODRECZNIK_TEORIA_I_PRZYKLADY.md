Oczywiście. Oto **KURS PYTHON 2.0** – naturalna kontynuacja Twojej ściągawki i lista ćwiczeń, które już robisz. Zakładam, że masz już opanowane: zmienne, typy, pętle, funkcje i podstawową obsługę błędów.

---

# 🐍 KURS PYTHON 2.0 – OD SKŁADNI DO PROJEKTU

**Dla kogo:** Po opanowaniu podstaw (12 punktów z listy ćwiczeń)  
**Cel:** Połączenie wiedzy w działające programy i przygotowanie do pracy z systemem (Twoje WSMS PRO)

---

## MODUŁ 1: PRACA Z PLIKAMI I ŚCIEŻKAMI

### 1.1 Odczytywanie i zapisywanie plików

```python
# Zapis do pliku
with open("dane.txt", "w") as f:
    f.write("Linia 1\n")
    f.write("Linia 2\n")

# Odczyt całego pliku
with open("dane.txt", "r") as f:
    tresc = f.read()
    print(tresc)

# Odczyt linia po linii
with open("dane.txt", "r") as f:
    for linia in f:
        print(f"Linia: {linia.strip()}")
```

**Tryby otwarcia:**
| Tryb | Znaczenie |
|:---|:---|
| `"r"` | odczyt |
| `"w"` | zapis (kasuje zawartość) |
| `"a"` | dopisywanie |
| `"r+"` | odczyt i zapis |

### 1.2 Moduł `os` – operacje systemowe

```python
import os

# Ścieżki i foldery
print(os.getcwd())                    # bieżący katalog
os.mkdir("nowy_folder")               # tworzy folder
os.chdir("nowy_folder")               # zmienia katalog
print(os.listdir("."))                # lista plików

# Sprawdzanie istnienia
if os.path.exists("plik.txt"):
    print("Plik istnieje")

# Łączenie ścieżek (działa na Windows i Linux!)
sciezka = os.path.join("folder", "podfolder", "plik.txt")
print(sciezka)  # folder/podfolder/plik.txt
```

### 1.3 `pathlib` – nowoczesne podejście (Python 3.4+)

```python
from pathlib import Path

# Tworzenie ścieżki
plik = Path("dane") / "raport.txt"
print(plik)  # dane/raport.txt

# Sprawdzanie
if plik.exists():
    print(f"Rozmiar: {plik.stat().st_size} bajtów")

# Czytanie i zapis
plik.write_text("Hello World")
tresc = plik.read_text()
```

**ĆWICZENIA MODUŁ 1:**
1. Napisz program, który listuje wszystkie pliki `.txt` w podanym folderze
2. Stwórz program do kopiowania pliku (odczyt z jednego, zapis do drugiego)
3. Napisz skrypt zliczający liczbę linii we wszystkich plikach `.py` w folderze

---

## MODUŁ 2: FUNKCJE ZAAWANSOWANE

### 2.1 Argumenty domyślne i nazwane

```python
def powitanie(imie, powtorzen=1, glosno=False):
    tekst = f"Cześć {imie}! "
    if glosno:
        tekst = tekst.upper()
    return tekst * powtorzen

print(powitanie("Jack"))                     # Cześć Jack!
print(powitanie("Jack", 3))                  # Cześć Jack! Cześć Jack! Cześć Jack!
print(powitanie("Jack", glosno=True))        # CZEŚĆ JACK!
```

### 2.2 `*args` i `**kwargs` – dowolna liczba argumentów

```python
# *args – dowolna liczba argumentów pozycyjnych
def suma_wszystkiego(*liczby):
    return sum(liczby)

print(suma_wszystkiego(1, 2, 3, 4, 5))  # 15

# **kwargs – dowolna liczba argumentów nazwanych
def opis_osoby(**dane):
    for klucz, wartosc in dane.items():
        print(f"{klucz}: {wartosc}")

opis_osoby(imie="Jack", wiek=35, miasto="Tortuga")
```

### 2.3 Funkcje lambda (anonimowe)

```python
# Zamiast:
def kwadrat(x):
    return x ** 2

# Można:
kwadrat = lambda x: x ** 2

# Przydatne z map() i filter()
liczby = [1, 2, 3, 4, 5]
kwadraty = list(map(lambda x: x**2, liczby))  # [1, 4, 9, 16, 25]
parzyste = list(filter(lambda x: x % 2 == 0, liczby))  # [2, 4]
```

**ĆWICZENIA MODUŁ 2:**
1. Napisz funkcję `konfiguruj_serwer(**opcje)`, która przyjmuje dowolne parametry i zapisuje je do pliku
2. Stwórz funkcję `filtruj_pliki(folder, *rozszerzenia)`, która zwraca tylko pliki o podanych rozszerzeniach

---

## MODUŁ 3: MODUŁY I IMPORTY

### 3.1 Tworzenie własnego modułu

**Plik: `serwer_utils.py`**
```python
def sprawdz_dysk(sciezka="/"):
    import shutil
    total, used, free = shutil.disk_usage(sciezka)
    return {
        "total_gb": total // (2**30),
        "free_gb": free // (2**30),
        "procent": (used / total) * 100
    }

def ping(host):
    import subprocess
    result = subprocess.run(["ping", "-c", "1", host], capture_output=True)
    return result.returncode == 0
```

**Plik: `main.py`**
```python
# Import całego modułu
import serwer_utils

dysk = serwer_utils.sprawdz_dysk()
print(f"Wolne: {dysk['free_gb']} GB")

# Import konkretnej funkcji
from serwer_utils import ping

if ping("google.com"):
    print("Internet działa")
```

### 3.2 Struktura większego projektu

```
moj_projekt/
├── main.py
├── utils/
│   ├── __init__.py      # (może być pusty – ważne!)
│   ├── dysk.py
│   └── siec.py
└── config.py
```

**Import z podfolderu:**
```python
from utils.dysk import sprawdz_dysk
from utils.siec import ping
```

**ĆWICZENIA MODUŁ 3:**
1. Podziel swój kod z ćwiczeń na moduły (osobno funkcje do plików, osobno do obliczeń)
2. Stwórz plik `config.py` z ustawieniami i importuj go w `main.py`

---

## MODUŁ 4: DANE STRUKTURALNE (JSON, CSV)

### 4.1 JSON – wymiana danych

```python
import json

# Zapis słownika do JSON
dane = {
    "serwer": "Ubuntu 22.04",
    "strony": ["wp1", "wp2"],
    "backupy": {
        "ostatni": "2026-04-20",
        "rozmiar_mb": 156
    }
}

with open("config.json", "w") as f:
    json.dump(dane, f, indent=4)  # indent=4 dla czytelności

# Odczyt JSON
with open("config.json", "r") as f:
    wczytane = json.load(f)
    print(wczytane["serwer"])
```

### 4.2 CSV – tabele danych

```python
import csv

# Zapis
with open("raport.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Strona", "Wersja WP", "Status"])
    writer.writerow(["wp1", "6.2", "OK"])
    writer.writerow(["wp2", "6.1", "Update needed"])

# Odczyt jako słowniki
with open("raport.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(f"{row['Strona']}: {row['Status']}")
```

**ĆWICZENIA MODUŁ 4:**
1. Napisz program, który zapisuje wyniki `wp-fleet` (Twój skrypt Bash) do pliku JSON
2. Stwórz generator raportu CSV z listy stron WordPress (nazwa, wersja, data ostatniej aktualizacji)

---

## MODUŁ 5: URUCHAMIANIE KOMEND SYSTEMOWYCH (subprocess)

To **kluczowy moduł** dla Ciebie – most między Pythonem a Twoim WSMS PRO w Bashu.

### 5.1 Podstawy `subprocess`

```python
import subprocess

# Proste wywołanie – wynik jako tekst
result = subprocess.run(["ls", "-la"], capture_output=True, text=True)
print(result.stdout)

# Sprawdzanie kodu wyjścia
result = subprocess.run(["ping", "-c", "1", "google.com"])
if result.returncode == 0:
    print("✅ Ping OK")
else:
    print("❌ Błąd")
```

### 5.2 Wykonywanie skryptów Bash

```python
# Wywołanie Twojego skryptu WSMS
result = subprocess.run(
    ["/home/jack/scripts/wp-status"],
    capture_output=True,
    text=True,
    shell=True  # potrzebne dla aliasów i ~
)

# Podział wyniku na linie
for linia in result.stdout.split("\n"):
    if "WordPress" in linia:
        print(linia)
```

### 5.3 Przykład: wrapper Pythona dla WSMS

```python
import subprocess
import json
from pathlib import Path

def wp_status():
    """Uruchamia wp-status i zwraca wynik jako string."""
    result = subprocess.run(
        ["/home/jack/scripts/wp-status"],
        capture_output=True,
        text=True,
        shell=True
    )
    return result.stdout

def backup_all_sites():
    """Uruchamia backup dla wszystkich stron."""
    scripts = [
        "wp-backup-lite",
        "mysql-backup-all"
    ]
    wyniki = {}
    for script in scripts:
        result = subprocess.run([script], capture_output=True, text=True, shell=True)
        wyniki[script] = result.returncode == 0
    return wyniki

# Użycie
print(wp_status())
print(backup_all_sites())  # {'wp-backup-lite': True, 'mysql-backup-all': True}
```

**ĆWICZENIA MODUŁ 5:**
1. Napisz funkcję `sprawdz_logi(plik_logu)`, która odczytuje plik logu WSMS i zwraca tylko linie z "ERROR"
2. Stwórz skrypt Pythona, który:
   - Uruchamia `wp-fleet`
   - Parsuje wynik
   - Zapisuje do JSON listę stron wymagających aktualizacji
3. Napisz własny `wp-status` w Pythonie (użyj `shutil.disk_usage`, `subprocess` do `wp-cli`)

---

## MODUŁ 6: MINI-PROJEKT – MENEDŻER BACKUPÓW W PYTHONIE

To zadanie integracyjne – łączy wszystko, czego się nauczyłeś.

### Specyfikacja

Stwórz program `backup_manager.py`, który:

1. **Listuje backupy** z folderu `~/backups-lite/`
2. **Wyświetla statystyki**: całkowity rozmiar, liczba plików, najstarszy/najnowszy
3. **Czyści stare backupy** – usuwa starsze niż N dni
4. **Zapisuje raport** do JSON po każdym czyszczeniu

### Szkielet rozwiązania

```python
#!/usr/bin/env python3
import os
import json
import shutil
from pathlib import Path
from datetime import datetime, timedelta

BACKUP_DIR = Path.home() / "backups-lite"
REPORT_FILE = Path.home() / "logs" / "backup_cleaner_report.json"

def list_backups():
    """Zwraca listę plików backupów z datami modyfikacji."""
    backupy = []
    for plik in BACKUP_DIR.glob("*"):
        if plik.is_file():
            stat = plik.stat()
            backupy.append({
                "nazwa": plik.name,
                "rozmiar_mb": stat.st_size / (1024 * 1024),
                "data": datetime.fromtimestamp(stat.st_mtime)
            })
    return backupy

def stats(backupy):
    """Oblicza statystyki backupów."""
    if not backupy:
        return {"liczba": 0, "rozmiar_mb": 0}
    
    return {
        "liczba": len(backupy),
        "rozmiar_mb": sum(b["rozmiar_mb"] for b in backupy),
        "najstarszy": min(b["data"] for b in backupy),
        "najnowszy": max(b["data"] for b in backupy)
    }

def clean_old(days=14):
    """Usuwa backupy starsze niż days dni."""
    backupy = list_backups()
    cutoff = datetime.now() - timedelta(days=days)
    
    usuniete = []
    for b in backupy:
        if b["data"] < cutoff:
            plik = BACKUP_DIR / b["nazwa"]
            plik.unlink()  # usunięcie pliku
            usuniete.append(b["nazwa"])
    
    # Zapisz raport
    raport = {
        "data_czyszczenia": datetime.now().isoformat(),
        "usunieto": usuniete,
        "liczba_usunietych": len(usuniete),
        "statystyki_po": stats(list_backups())
    }
    
    with open(REPORT_FILE, "w") as f:
        json.dump(raport, f, indent=4)
    
    return raport

def main():
    print("=== Menedżer Backupów WSMS ===")
    backupy = list_backups()
    print(f"Znaleziono {len(backupy)} backupów")
    
    staty = stats(backupy)
    print(f"Łączny rozmiar: {staty['rozmiar_mb']:.2f} MB")
    
    odp = input("Czyścić starsze niż 14 dni? [t/N]: ")
    if odp.lower() == "t":
        raport = clean_old(14)
        print(f"Usunięto {raport['liczba_usunietych']} plików")
        print(f"Raport zapisany w {REPORT_FILE}")

if __name__ == "__main__":
    main()
```

**ĆWICZENIA MODUŁ 6:**
1. Uruchom powyższy kod w swoim środowisku
2. Dodaj opcję `--dry-run`, która tylko pokazuje co by usunęła, bez faktycznego usuwania
3. Rozszerz program o obsługę `~/backups-full/` i `~/mysql-backups/`
4. Dodaj powiadomienie (np. `print` w kolorze czerwonym) gdy wolnego miejsca jest mniej niż 10%

---

## MODUŁ 7: BIBLIOTEKI ZEWNĘTRZNE (pip)

### 7.1 Instalacja i używanie

```bash
# Instalacja
pip install requests
pip install rich  # ładne formatowanie w terminalu
```

### 7.2 `requests` – HTTP i API

```python
import requests

# Pobieranie strony
response = requests.get("https://api.github.com/users/octocat")
if response.status_code == 200:
    dane = response.json()
    print(f"Użytkownik: {dane['login']}")
    print(f"Publicznych repo: {dane['public_repos']}")
```

### 7.3 `rich` – ładny terminal

```python
from rich.console import Console
from rich.table import Table
from rich.progress import track
import time

console = Console()

# Kolorowe komunikaty
console.print("✅ Sukces!", style="green")
console.print("❌ Błąd!", style="red bold")

# Tabela
table = Table(title="Status serwerów WP")
table.add_column("Strona", style="cyan")
table.add_column("Wersja WP", style="magenta")
table.add_column("Status", style="green")

table.add_row("wp1.local", "6.2", "OK")
table.add_row("wp2.local", "6.1", "Update needed")

console.print(table)

# Pasek postępu
for i in track(range(10), description="Przetwarzanie..."):
    time.sleep(0.1)
```

**ĆWICZENIA MODUŁ 7:**
1. Użyj `requests` do pobrania informacji o swoim repo WSMS PRO z API GitHuba
2. Przerób swój `backup_manager.py` używając `rich` do ładniejszego wyświetlania wyników

---

## PODSUMOWANIE KURSU 2.0

### Co już umiesz po tym kursie:

| Umiejętność | Gdzie wykorzystasz |
|:---|:---|
| Praca z plikami i ścieżkami | Logi, konfiguracje, backupy |
| Funkcje zaawansowane | Czysty, modułowy kod |
| Własne moduły | Organizacja większych projektów |
| JSON/CSV | Raporty, wymiana danych między skryptami |
| `subprocess` | **Most między Pythonem a Twoim WSMS PRO** |
| Biblioteki zewnętrzne | Rozszerzanie możliwości Pythona |

### Następny krok

Gdy skończysz ten kurs, będziesz gotowy na:
- **Przepisanie fragmentów WSMS PRO z Basha na Pythona**
- **Stworzenie webowego interfejsu** (Flask/FastAPI)
- **Automatyzację z użyciem API** (GitHub, Slack, monitoring)

---

**Powodzenia z ćwiczeniami. Wracaj, gdy skończysz Moduł 6 – wtedy omówimy, jak podłączyć to do Twojego WSMS PRO.**
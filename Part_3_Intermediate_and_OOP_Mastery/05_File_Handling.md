# Moduł 5: File Handling — Praca z Plikami

## 5.1 Podstawowe operacje z plikami

```python
# Pisanie do pliku
with open("test.txt", "w") as f:
    f.write("Cześć świecie!\n")
    f.write("Linia 2\n")

# Czytanie z pliku
with open("test.txt", "r") as f:
    content = f.read()  # Cały plik jako string
    print(content)

# Czytanie linia po linii
with open("test.txt", "r") as f:
    for line in f:
        print(line.strip())

# Odczyt do listy
with open("test.txt", "r") as f:
    lines = f.readlines()
    print(lines)  # ['Cześć świecie!\n', 'Linia 2\n']
```

## 5.2 Tryby otwarcia pliku

| Tryb | Opis |
|------|------|
| `r` | Czytanie (domyślny) |
| `w` | Pisanie (nadpisuje plik) |
| `a` | Dopisywanie (append) |
| `r+` | Czytanie i pisanie |
| `b` | Tryb binarny (np. `rb`, `wb`) |

```python
# Dopisanie do pliku
with open("test.txt", "a") as f:
    f.write("Nowa linia na końcu\n")

# Plik binarny
with open("image.png", "rb") as f:
    data = f.read()
```

## 5.3 JSON

```python
import json

# Słownik → JSON
person = {"name": "Alice", "age": 30, "city": "Warsaw"}
json_string = json.dumps(person)
print(json_string)  # {"name": "Alice", "age": 30, "city": "Warsaw"}

# Zapis do pliku
with open("person.json", "w") as f:
    json.dump(person, f, indent=2)

# Czytanie z pliku
with open("person.json", "r") as f:
    loaded = json.load(f)
    print(loaded["name"])  # Alice

# JSON → słownik
json_str = '{"x": 10, "y": 20}'
data = json.loads(json_str)
print(data)  # {'x': 10, 'y': 20}
```

## 5.4 CSV

```python
import csv

# Pisanie CSV
data = [
    ["name", "age", "city"],
    ["Alice", 30, "Warsaw"],
    ["Bob", 25, "Krakow"],
    ["Charlie", 35, "Gdansk"]
]

with open("people.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(data)

# Czytanie CSV
with open("people.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

# Czytanie jako słowniki
with open("people.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row)  # {'name': 'Alice', 'age': '30', 'city': 'Warsaw'}
```

## 5.5 pathlib — nowoczesny sposób pracy ze ścieżkami

```python
from pathlib import Path

# Tworzenie ścieżki
p = Path("data") / "file.txt"  # data/file.txt
print(p)

# Operacje na ścieżkach
print(p.exists())         # Czy plik istnieje?
print(p.is_file())        # Czy to plik?
print(p.is_dir())         # Czy to folder?
print(p.name)             # 'file.txt'
print(p.stem)             # 'file'
print(p.suffix)           # '.txt'
print(p.parent)           # 'data'

# Tworzenie katalogów
p.parent.mkdir(parents=True, exist_ok=True)

# Listowanie plików
data_dir = Path("data")
for file in data_dir.glob("*.txt"):
    print(file)

# Czytanie/pisanie
content = p.read_text()
p.write_text("Hello world")
```

## 5.6 Obsługa błędów przy pracy z plikami

```python
from pathlib import Path

def safe_read_file(filename):
    try:
        with open(filename, "r") as f:
            return f.read()
    except FileNotFoundError:
        print(f"Plik {filename} nie istnieje")
        return None
    except PermissionError:
        print(f"Brak uprawnień do {filename}")
        return None
    except Exception as e:
        print(f"Błąd: {e}")
        return None
```

---

## Zadania

### Zadanie 5.1: Zapis i czytanie tekstowe
1. Stwórz plik `notes.txt` i wpisz 5 linijek tekstu
2. Odczytaj plik i wypisz każdą linię z numerem

### Zadanie 5.2: JSON
1. Stwórz listę słowników zawierającą dane: name, email, age dla 3 osób
2. Zapisz do `people.json` z formatowaniem
3. Odczytaj plik i wypisz

### Zadanie 5.3: CSV
Stwórz plik CSV z tabelą produktów (name, price, quantity)  
Następnie odczytaj i wypisz tylko produkty ze stanu > 10

### Zadanie 5.4: pathlib
Stwórz strukturę folderów: `project/src/main.py` i `project/data/file.txt`  
Używając pathlib, sprawdź czy pliki istnieją


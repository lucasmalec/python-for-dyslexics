# Moduł 6: Modules & Packages — Organizacja Kodu

## 6.1 Import — podstawy

```python
# Importowanie całego modułu
import math
print(math.sqrt(16))  # 4.0

# Importowanie konkretnej funkcji
from math import sqrt, pi
print(sqrt(25))  # 5.0
print(pi)        # 3.14159265359

# Alias
import numpy as np
from collections import defaultdict as dd

# Importowanie wszystkiego (unikaj!)
from math import *  # ❌ Zła praktyka
```

## 6.2 Twój własny moduł

### struktura:
```
my_project/
├── main.py
└── utils.py
```

### utils.py
```python
def greet(name):
    return f"Cześć {name}!"

def add(a, b):
    return a + b

PI = 3.14159
```

### main.py
```python
from utils import greet, add, PI

print(greet("Alice"))  # Cześć Alice!
print(add(5, 3))       # 8
print(PI)              # 3.14159
```

## 6.3 Package — folder z modułami

### struktura:
```
my_app/
├── __init__.py
├── main.py
├── math_utils/
│   ├── __init__.py
│   ├── operations.py
│   └── geometry.py
└── data/
    ├── __init__.py
    └── loader.py
```

### math_utils/__init__.py
```python
# To czyni folder packageiem
from .operations import add, subtract
from .geometry import circle_area

__all__ = ['add', 'subtract', 'circle_area']
```

### math_utils/operations.py
```python
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b
```

### main.py
```python
# Importowanie z package
from math_utils import add, circle_area

result = add(10, 5)
area = circle_area(5)
```

## 6.4 __name__ == '__main__'

```python
# calc.py

def multiply(a, b):
    return a * b

if __name__ == '__main__':
    # Ten kod wykonuje się TYLKO gdy plik jest uruchomiony bezpośrednio
    print(multiply(5, 3))
    # Nie wykonuje się przy importowaniu!

# Użycie w innym pliku
from calc import multiply
result = multiply(10, 2)  # multiply się nie wywoła przy imporcie
```

## 6.5 sys.path i PYTHONPATH

```python
import sys

# Bieżące lokalizacje importu
print(sys.path)

# Dodanie własnego folderu
sys.path.insert(0, '/Users/user/my_modules')

# Teraz możliwe: from my_module import something
```

## 6.6 Virtual environments (venv)

```bash
# Tworzenie
python -m venv myenv

# Aktywacja (Mac/Linux)
source myenv/bin/activate

# Aktywacja (Windows)
myenv\Scripts\activate

# Instalacja pakietów
pip install requests pandas

# Zapisanie zależności
pip freeze > requirements.txt

# Instalacja z pliku
pip install -r requirements.txt

# Deaktywacja
deactivate
```

## 6.7 Dobra praktyka — struktura projektu

```
my_project/
├── README.md
├── requirements.txt
├── setup.py
├── src/
│   └── my_package/
│       ├── __init__.py
│       ├── main.py
│       ├── utils.py
│       └── config.py
├── tests/
│   ├── __init__.py
│   ├── test_utils.py
│   └── test_main.py
└── docs/
    └── guide.md
```

---

## Zadania

### Zadanie 6.1: Stwórz moduł
Stwórz `geometry.py` z funkcjami:
- `rectangle_area(width, height)`
- `circle_area(radius)`
- `triangle_area(base, height)`

Zaimportuj w `main.py` i testuj

### Zadanie 6.2: Package
Stwórz package `statistics_lib/` z modułami:
- `avg.py` — średnia
- `median.py` — mediana
- `__init__.py` — export funkcji

### Zadanie 6.3: Virtual environment
1. Utwórz venv
2. Zainstaluj: requests, pandas
3. Stwórz `requirements.txt`
4. Usuń venv i przywróć z `requirements.txt`


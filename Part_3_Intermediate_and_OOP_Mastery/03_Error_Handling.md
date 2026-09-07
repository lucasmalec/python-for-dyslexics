# Moduł 3: Error Handling — Obsługa Błędów

## 3.1 Try/Except/Finally

```python
try:
    x = 1 / 0  # ZeroDivisionError
except ZeroDivisionError:
    print("Nie można dzielić przez zero!")
except Exception as e:
    print(f"Błąd: {e}")
finally:
    print("Kod, który zawsze się wykonuje")
```

## 3.2 Hierarchia wyjątków

```
BaseException
├── SystemExit
├── KeyboardInterrupt
└── Exception
    ├── StopIteration
    ├── GeneratorExit
    ├── ValueError
    ├── TypeError
    ├── ZeroDivisionError
    ├── KeyError
    ├── IndexError
    └── ...
```

Unikaj łapania `Exception` lub `BaseException` — bądź konkretny:

```python
# ❌ Źle
try:
    something()
except:
    pass

# ✅ Dobrze
try:
    int("abc")
except ValueError:
    print("Nie można skonwertować na int")
```

## 3.3 Własne wyjątki (Custom Exceptions)

```python
class InsufficientFundsError(Exception):
    """Brakuje pieniędzy na koncie"""
    pass

class InvalidAccountError(Exception):
    """Nieprawidłowy numer konta"""
    pass

class BankAccount:
    def __init__(self, account_no, balance):
        if not isinstance(account_no, str):
            raise InvalidAccountError("Numer konta musi być string")
        self.account_no = account_no
        self.balance = balance
    
    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientFundsError(f"Brakuje {amount - self.balance} zł")
        self.balance -= amount

# Użycie
try:
    account = BankAccount(12345, 100)  # Błąd!
except InvalidAccountError as e:
    print(f"Błąd: {e}")
```

## 3.4 Else w try/except

```python
try:
    result = 10 / 2
except ZeroDivisionError:
    print("Dzielenie przez zero!")
else:
    print(f"Wynik: {result}")  # Wykonuje się jeśli BRAK błędu
finally:
    print("Koniec")
```

## 3.5 Context managers — with statement

```python
# ❌ Stary sposób
file = open("test.txt")
content = file.read()
file.close()

# ✅ Nowy sposób
with open("test.txt") as file:
    content = file.read()
# Plik automatycznie się zamyka!
```

### Twój własny context manager

```python
class DatabaseConnection:
    def __init__(self, name):
        self.name = name
    
    def __enter__(self):
        print(f"Łączę się do {self.name}")
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"Rozłączam się z {self.name}")
        if exc_type:
            print(f"Błąd: {exc_val}")
        return False  # False = nie ukrywaj wyjątku

with DatabaseConnection("MySQL") as db:
    print("Pracuję z bazą danych")
    # __exit__ się wywoła automatycznie
```

## 3.6 Logowanie błędów

```python
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger(__name__)

try:
    value = int("abc")
except ValueError:
    logger.error("Nie można skonwertować na int", exc_info=True)
    logger.warning("Używam wartości domyślnej: 0")
```

---

## Zadania

### Zadanie 3.1: Kalkulator z obsługą błędów
Stwórz funkcję `safe_divide(a, b)`, która:
- Zwraca wynik dzielenia
- Obsługuje ZeroDivisionError
- Obsługuje TypeError (jeśli argument nie jest liczbą)
- Loguje błędy

### Zadanie 3.2: Własny wyjątek
Stwórz wyjątek `PasswordTooWeakError` i funkcję `validate_password(pwd)`:
- Jeśli hasło ma < 8 znaków → rzuć wyjątek
- Obsłuż wyjątek w main

### Zadanie 3.3: Context Manager
Stwórz context manager `Timer`, który mierzy czas wykonania kodu w bloku `with`


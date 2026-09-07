# Moduł 1: Funkcje Zaawansowane

## 1.1 Zakresy zmiennych (Scope)

### Poziomy zakresu: LEGB
- **L** — Local (lokalne — wewnątrz funkcji)
- **E** — Enclosing (otaczające — nested functions)
- **G** — Global (globalne — moduł)
- **B** — Built-in (wbudowane — funkcje Pythona)

```python
x = "global"  # G

def outer():
    x = "enclosing"  # E
    
    def inner():
        x = "local"  # L
        print(x)
    
    inner()
    print(x)

outer()
print(x)
```

**Output:**
```
local
enclosing
global
```

### global i nonlocal

```python
x = 0

def increment():
    global x
    x += 1
    return x

print(increment())  # 1
print(increment())  # 2
```

## 1.2 Closures

Funkcja wewnętrzna, która "zapamiętuje" zmienne z zakresu zewnętrznego:

```python
def make_multiplier(factor):
    def multiplier(x):
        return x * factor
    return multiplier

times_three = make_multiplier(3)
times_five = make_multiplier(5)

print(times_three(10))  # 30
print(times_five(10))   # 50
```

## 1.3 *args i **kwargs

### *args — zmienna liczba argumentów pozycyjnych

```python
def sum_all(*args):
    print(f"Argumenty: {args}")
    return sum(args)

sum_all(1, 2, 3, 4, 5)  # (1, 2, 3, 4, 5)
```

### **kwargs — argumenty nazwane

```python
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Ala", age=25, city="Warsaw")
```

### Łączenie *args i **kwargs

```python
def flexible_func(a, *args, **kwargs):
    print(f"a: {a}")
    print(f"args: {args}")
    print(f"kwargs: {kwargs}")

flexible_func(1, 2, 3, name="test", value=42)
```

## 1.4 Dekoratory

Funkcja, która modyfikuje inną funkcję bez zmieniania jej kodu:

```python
def timer_decorator(func):
    import time
    
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} zajęła {end - start:.4f} sekund")
        return result
    
    return wrapper

@timer_decorator
def slow_function():
    import time
    time.sleep(2)
    return "Done"

slow_function()
```

## 1.5 Type Hints

Wskazówki typu (nie wymuszane, ale ułatwiają debugowanie):

```python
def greet(name: str, age: int) -> str:
    return f"Cześć {name}, masz {age} lat"

def add(a: int, b: int) -> int:
    return a + b

from typing import List, Dict, Optional

def process_items(items: List[str]) -> Dict[str, int]:
    return {item: len(item) for item in items}

def find_user(user_id: int) -> Optional[str]:
    users = {1: "Alice", 2: "Bob"}
    return users.get(user_id)
```

---

## Zadania

### Zadanie 1.1: Closure na licznik
Stwórz funkcję `make_counter()`, która zwraca funkcję incrementującą licznik każdorazowo:

```python
counter = make_counter()
print(counter())  # 1
print(counter())  # 2
print(counter())  # 3
```

### Zadanie 1.2: Dekorator do logowania
Stwórz dekorator `@log_calls`, który loguje każde wywołanie funkcji:

```python
@log_calls
def add(a, b):
    return a + b

add(5, 3)  # Powinno wypisać: "add(5, 3) -> 8"
```

### Zadanie 1.3: Funkcja z type hints
Stwórz funkcję `filter_even(numbers: List[int]) -> List[int]` zwracającą tylko liczby parzyste


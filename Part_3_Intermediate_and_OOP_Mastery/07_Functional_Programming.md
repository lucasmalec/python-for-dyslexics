# Moduł 7: Functional Programming

## 7.1 Lambda — anonimowe funkcje

```python
# Zwykła funkcja
def add(a, b):
    return a + b

# Lambda — one-liner
add = lambda a, b: a + b

# Użycie w praktyce
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))
print(squared)  # [1, 4, 9, 16, 25]

# Sortowanie po własnym kluczu
people = [("Alice", 30), ("Bob", 25), ("Charlie", 35)]
sorted_people = sorted(people, key=lambda x: x[1])
print(sorted_people)  # [('Bob', 25), ('Alice', 30), ('Charlie', 35)]
```

## 7.2 map() — mapowanie funkcji

```python
# map(function, iterable) → iterator

numbers = [1, 2, 3, 4, 5]

# Podwoić każdą liczbę
doubled = list(map(lambda x: x * 2, numbers))
print(doubled)  # [2, 4, 6, 8, 10]

# Konwertować do stringów
str_numbers = list(map(str, numbers))
print(str_numbers)  # ['1', '2', '3', '4', '5']

# Wiele iterables
a = [1, 2, 3]
b = [10, 20, 30]
result = list(map(lambda x, y: x + y, a, b))
print(result)  # [11, 22, 33]
```

## 7.3 filter() — filtrowanie

```python
# filter(predicate, iterable) → iterator

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Tylko liczby parzyste
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)  # [2, 4, 6, 8, 10]

# Filtrowanie stringów
words = ["python", "java", "go", "rust", "javascript"]
short = list(filter(lambda w: len(w) < 5, words))
print(short)  # ['java', 'python', 'rust']

# Usuń None i falsy values
data = [1, None, 2, 0, 3, "", 4]
clean = list(filter(None, data))
print(clean)  # [1, 2, 3, 4]
```

## 7.4 reduce() — akumulacja

```python
from functools import reduce

numbers = [1, 2, 3, 4, 5]

# Suma wszystkich
total = reduce(lambda x, y: x + y, numbers)
print(total)  # 15

# Iloczyn
product = reduce(lambda x, y: x * y, numbers)
print(product)  # 120

# Znalezienie max
maximum = reduce(lambda x, y: x if x > y else y, numbers)
print(maximum)  # 5

# Z wartością początkową
result = reduce(lambda x, y: x + y, numbers, 100)
print(result)  # 115 (100 + suma)
```

## 7.5 functools.partial — częściowa aplikacja

```python
from functools import partial

def multiply(x, y):
    return x * y

# Utwórz nową funkcję z x=10
times_ten = partial(multiply, 10)
print(times_ten(5))   # 50
print(times_ten(100)) # 1000

# Z więcej argumentami
def power(base, exponent):
    return base ** exponent

square = partial(power, exponent=2)
print(square(5))  # 25
print(square(10)) # 100
```

## 7.6 functools.lru_cache — memoizacja

```python
from functools import lru_cache
import time

# Bez cache
def slow_fibonacci(n):
    if n < 2:
        return n
    return slow_fibonacci(n-1) + slow_fibonacci(n-2)

# Liczenie fib(35) zajmuje długo!

# Z cache
@lru_cache(maxsize=128)
def fast_fibonacci(n):
    if n < 2:
        return n
    return fast_fibonacci(n-1) + fast_fibonacci(n-2)

print(fast_fibonacci(35))  # Natychmiast!
```

## 7.7 Composable functions — komponowanie

```python
# Łączenie operacji
def compose(*functions):
    def composed(x):
        for f in reversed(functions):
            x = f(x)
        return x
    return composed

add_one = lambda x: x + 1
multiply_two = lambda x: x * 2
square = lambda x: x ** 2

# compose(square, multiply_two, add_one)(5)
# = square(multiply_two(add_one(5)))
# = square(multiply_two(6))
# = square(12)
# = 144

pipeline = compose(square, multiply_two, add_one)
print(pipeline(5))  # 144
```

---

## Zadania

### Zadanie 7.1: Lambda i map
Mając listę: `names = ["alice", "bob", "charlie"]`  
Użyj map() z lambda żeby zwrócić listę (name, length):
```python
# Wynik: [("alice", 5), ("bob", 3), ("charlie", 7)]
```

### Zadanie 7.2: filter
Mając listę: `numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]`  
Przefiltruj tylko liczby większe od 5 i mniejsze od 9

### Zadanie 7.3: reduce
Użyj reduce() do:
- Obliczenia sumy
- Obliczenia maksimum
- Konkatenacji stringów: `["Hello", "World", "!"]` → `"HelloWorld!"`

### Zadanie 7.4: partial
Stwórz funkcję `divide(a, b)` i użyj partial do utworzenia:
- `divide_by_2 = partial(divide, b=2)`
- `divide_by_10 = partial(divide, b=10)`


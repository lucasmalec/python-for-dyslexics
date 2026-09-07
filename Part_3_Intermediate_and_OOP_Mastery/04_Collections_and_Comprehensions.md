# Moduł 4: Collections & Comprehensions

## 4.1 List Comprehensions

```python
# Podstawowa forma
squares = [x**2 for x in range(1, 6)]
print(squares)  # [1, 4, 9, 16, 25]

# Z warunkiem
evens = [x for x in range(1, 11) if x % 2 == 0]
print(evens)  # [2, 4, 6, 8, 10]

# Z warunkiem else
result = [x if x % 2 == 0 else -x for x in range(1, 6)]
print(result)  # [-1, 2, -3, 4, -5]

# Zagnieżdżone
matrix = [[j for j in range(3)] for i in range(3)]
print(matrix)  # [[0, 1, 2], [0, 1, 2], [0, 1, 2]]
```

## 4.2 Dict Comprehensions

```python
# Podstawowa forma
squares_dict = {x: x**2 for x in range(1, 5)}
print(squares_dict)  # {1: 1, 2: 4, 3: 9, 4: 16}

# Z warunkiem
even_squares = {x: x**2 for x in range(1, 11) if x % 2 == 0}

# Zamiana klucza i wartości
original = {'a': 1, 'b': 2, 'c': 3}
swapped = {v: k for k, v in original.items()}
print(swapped)  # {1: 'a', 2: 'b', 3: 'c'}
```

## 4.3 Set Comprehensions

```python
# Zbiór unikalnych elementów
numbers = [1, 2, 2, 3, 3, 3, 4]
unique = {x for x in numbers}
print(unique)  # {1, 2, 3, 4}

# Z warunkiem
evens = {x for x in range(1, 21) if x % 2 == 0}
```

## 4.4 Generator Expressions

```python
# Bardzo podobne do list comprehensions, ale lazy evaluation
squares_gen = (x**2 for x in range(1000000))
print(next(squares_gen))  # 0
print(next(squares_gen))  # 1

# Oszczędzanie pamięci
def process_large_file(filename):
    with open(filename) as f:
        lines = (line.strip() for line in f)  # Generator, nie lista!
        for line in lines:
            print(line)
```

## 4.5 Collections module

### defaultdict

```python
from collections import defaultdict

# Zamiast sprawdzać czy klucz istnieje
d = defaultdict(list)
d['a'].append(1)
d['a'].append(2)
d['b'].append(3)
print(d)  # defaultdict(<class 'list'>, {'a': [1, 2], 'b': [3]})
```

### Counter

```python
from collections import Counter

text = "mississippi"
letter_count = Counter(text)
print(letter_count)  # Counter({'i': 4, 's': 4, 'p': 2, 'm': 1})
print(letter_count.most_common(2))  # [('i', 4), ('s', 4)]

# Zliczanie słów
words = "python jest fajny python jest".split()
word_count = Counter(words)
print(word_count)  # Counter({'python': 2, 'jest': 2, 'fajny': 1})
```

### namedtuple

```python
from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])
p = Point(3, 4)
print(p.x, p.y)     # 3 4
print(p[0], p[1])   # 3 4

Person = namedtuple('Person', ['name', 'age', 'job'])
alice = Person('Alice', 30, 'Engineer')
print(alice)  # Person(name='Alice', age=30, job='Engineer')
```

### OrderedDict i deque

```python
from collections import OrderedDict, deque

# OrderedDict — zapamiętuje kolejność wstawienia
d = OrderedDict()
d['first'] = 1
d['second'] = 2
d['third'] = 3

# deque — dwa-końcowa kolejka
queue = deque([1, 2, 3])
queue.appendleft(0)      # [0, 1, 2, 3]
queue.append(4)          # [0, 1, 2, 3, 4]
print(queue.popleft())   # 0
```

---

## Zadania

### Zadanie 4.1: List comprehension
Stwórz listę wszystkich liczb od 1 do 100, które są podzielne przez 3 lub 5

### Zadanie 4.2: Dict comprehension
Mając listę imion: `names = ['alice', 'bob', 'charlie']`  
Stwórz słownik: `{'alice': 5, 'bob': 3, 'charlie': 7}` (długość każdego imienia)

### Zadanie 4.3: Counter
Mając tekst: `"the quick brown fox jumps over the lazy dog"`  
Policz ile razy pojawia się każda litera (ignorując spacje)

### Zadanie 4.4: namedtuple
Stwórz `Student = namedtuple('Student', ['name', 'grade', 'score'])`  
i utwórz listę 3 studentów z danymi


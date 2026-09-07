# Moduł 2: OOP — Klasy i Obiekty

## 2.1 Podstawy klas

### Definiowanie klasy

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def greet(self):
        return f"Cześć, jestem {self.name}"
    
    def birthday(self):
        self.age += 1

# Tworzenie obiektu (instancji)
person = Person("Anna", 25)
print(person.greet())      # Cześć, jestem Anna
print(person.age)          # 25
person.birthday()
print(person.age)          # 26
```

## 2.2 Konstruktor i destruktor

```python
class File:
    def __init__(self, filename):
        self.filename = filename
        self.file = open(filename, 'r')
        print(f"Plik {filename} otworzony")
    
    def __del__(self):
        self.file.close()
        print(f"Plik {self.filename} zamknięty")

# __del__ wywoła się przy usunięciu obiektu
```

## 2.3 Dziedziczenie

```python
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        return f"{self.name} wydaje dźwięk"

class Dog(Animal):
    def speak(self):  # Nadpisanie (override)
        return f"{self.name} gawka!"

class Cat(Animal):
    def speak(self):
        return f"{self.name} miauczy"

dog = Dog("Reksio")
print(dog.speak())  # Reksio gawka!
```

## 2.4 super() — dostęp do klasy rodzica

```python
class Vehicle:
    def __init__(self, brand):
        self.brand = brand

class Car(Vehicle):
    def __init__(self, brand, color):
        super().__init__(brand)  # Wywołanie __init__ rodzica
        self.color = color

car = Car("Toyota", "Red")
print(f"{car.brand} {car.color}")  # Toyota Red
```

## 2.5 Metody statyczne i klasowe

```python
class Math:
    PI = 3.14159
    
    @staticmethod
    def add(a, b):
        """Metoda statyczna — nie ma dostępu do self ani cls"""
        return a + b
    
    @classmethod
    def from_string(cls, value_str):
        """Metoda klasowa — ma dostęp do klasy (cls)"""
        return cls(int(value_str))

# Statyczna
print(Math.add(5, 3))  # 8

# Klasowa
obj = Math.from_string("42")
```

## 2.6 Właściwości (@property)

```python
class Circle:
    def __init__(self, radius):
        self._radius = radius
    
    @property
    def radius(self):
        return self._radius
    
    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError("Promień nie może być ujemny")
        self._radius = value
    
    @property
    def area(self):
        return 3.14159 * self._radius ** 2

circle = Circle(5)
print(circle.area)      # 78.53975
circle.radius = 10
print(circle.area)      # 314.159
```

## 2.7 Polimorfizm

```python
class Shape:
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14159 * self.radius ** 2

shapes = [Rectangle(5, 10), Circle(3)]
for shape in shapes:
    print(f"Pole: {shape.area()}")
```

## 2.8 Magiczne metody (dunder methods)

```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return f"Vector({self.x}, {self.y})"
    
    def __repr__(self):
        return f"Vector({self.x}, {self.y})"
    
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    
    def __len__(self):
        return int((self.x**2 + self.y**2)**0.5)

v1 = Vector(3, 4)
v2 = Vector(1, 2)
print(v1 + v2)      # Vector(4, 6)
print(len(v1))      # 5
```

---

## Zadania

### Zadanie 2.1: Klasa BankAccount
Stwórz klasę `BankAccount` z:
- `__init__(account_number, balance)`
- `deposit(amount)` — wpłata
- `withdraw(amount)` — wypłata (z walidacją)
- `get_balance()` — zwrócenie stanu

### Zadanie 2.2: Dziedziczenie — Employee
Stwórz klasę `Employee` z imię, stanowiskiem, wynagrodzeniem, oraz klasę `Manager(Employee)` z dodatkowym polem `team_size`

### Zadanie 2.3: Polimorfizm — Animal voices
Stwórz kilka klas zwierząt (Dog, Cat, Bird) i funkcję `make_sound(animal)` która dla każdego zwierzęcia wydaje inny dźwięk


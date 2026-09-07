# Moduł 8: Testing & Debugging

## 8.1 Testy jednostkowe (unittest)

```python
# calculator.py
def add(a, b):
    return a + b

def divide(a, b):
    if b == 0:
        raise ValueError("Nie można dzielić przez zero")
    return a / b
```

```python
# test_calculator.py
import unittest
from calculator import add, divide

class TestCalculator(unittest.TestCase):
    
    def test_add_positive(self):
        self.assertEqual(add(2, 3), 5)
    
    def test_add_negative(self):
        self.assertEqual(add(-1, -2), -3)
    
    def test_divide_positive(self):
        self.assertEqual(divide(10, 2), 5.0)
    
    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            divide(10, 0)

if __name__ == '__main__':
    unittest.main()
```

## 8.2 pytest — nowoczesne testy

```bash
# Instalacja
pip install pytest
```

```python
# test_calculator.py (z pytest)
from calculator import add, divide
import pytest

def test_add():
    assert add(2, 3) == 5
    assert add(-1, -2) == -3

def test_divide():
    assert divide(10, 2) == 5.0

def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(10, 0)

# Parametryczne testy
@pytest.mark.parametrize("a,b,expected", [
    (2, 3, 5),
    (0, 0, 0),
    (-1, 1, 0),
])
def test_add_parametrized(a, b, expected):
    assert add(a, b) == expected
```

```bash
# Uruchomienie
pytest test_calculator.py -v
```

## 8.3 Fixture — setup i teardown

```python
import pytest

@pytest.fixture
def sample_list():
    """Fixture zwracający testową listę"""
    return [1, 2, 3, 4, 5]

def test_sum_list(sample_list):
    assert sum(sample_list) == 15

def test_length_list(sample_list):
    assert len(sample_list) == 5

# Fixture z setup/teardown
@pytest.fixture
def database():
    db = connect_to_db()
    yield db  # Zwróć dla testu
    db.close()  # Cleanup

def test_with_db(database):
    result = database.query("SELECT * FROM users")
    assert len(result) > 0
```

## 8.4 Mocking — mockowanie zależności

```python
from unittest.mock import Mock, patch, MagicMock
import requests

def get_user_age(user_id):
    response = requests.get(f"https://api.example.com/users/{user_id}")
    return response.json()['age']

# Test z mockingiem
def test_get_user_age():
    with patch('requests.get') as mock_get:
        mock_response = Mock()
        mock_response.json.return_value = {'age': 30}
        mock_get.return_value = mock_response
        
        age = get_user_age(1)
        assert age == 30
        mock_get.assert_called_once_with("https://api.example.com/users/1")
```

## 8.5 Coverage — pokrycie testami

```bash
# Instalacja
pip install coverage

# Uruchomienie z coverage
coverage run -m pytest

# Raport
coverage report

# HTML report
coverage html
```

## 8.6 Debugowanie — pdb

```python
def buggy_function(numbers):
    total = 0
    for num in numbers:
        total += num
        # Wstawienie breakpointa
        import pdb; pdb.set_trace()
    return total / len(numbers)

# Komendy w debuggerze:
# l (list) — pokaż kod
# n (next) — następna linia
# s (step) — step into
# c (continue) — kontynuuj
# p variable — wypisz zmienną
# h (help) — pomoc
```

## 8.7 Asercje

```python
def validate_email(email):
    assert isinstance(email, str), "Email musi być string"
    assert '@' in email, "Email musi zawierać @"
    assert '.' in email.split('@')[1], "Domena musi zawierać ."
    return True

# Test
try:
    validate_email("test@example.com")
    validate_email("invalid")  # AssertionError
except AssertionError as e:
    print(f"Walidacja nieudana: {e}")
```

---

## Zadania

### Zadanie 8.1: unittest
Stwórz klasę `Calculator` z metodami `add()`, `subtract()`, `multiply()`, `divide()`  
Napisz testy jednostkowe dla każdej metody

### Zadanie 8.2: pytest
Przepisz testy z zadania 8.1 używając pytest  
Dodaj parametryczne testy z @pytest.mark.parametrize

### Zadanie 8.3: Fixture
Stwórz fixture `sample_data` zawierającą listę 10 liczb  
Użyj w dwóch testach

### Zadanie 8.4: Mocking
Mockuj funkcję `random.randint()` i testuj funkcję, która ją wykorzystuje

### Zadanie 8.5: Coverage
Uruchom coverage na swoich testach i sprawdź % pokrycia kodu


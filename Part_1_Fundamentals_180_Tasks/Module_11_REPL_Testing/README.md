# Module 11: REPL & Interactive Experimentation

[🇬🇧 English](README.md) | [🇵🇱 Polski](README.pl.md)

---

## 🎯 About This Module
Rapid prototyping in the Python REPL: inspecting types, evaluating expressions, and catching runtime errors.

- **Visual Limit:** Max 88 characters per line (PEP 8 / Black standard).
- **Format:** 15 hands-on progressive tasks with full English solutions.

---

## 📝 15 Hands-on Tasks

### Task 01: REPL Math Evaluation
- **Requirement:** Calculate `25 * 4 - 10`.
- **PL:** Oblicz `25 * 4 - 10`.
- **Solution:** [`solutions/task_01.py`](solutions/task_01.py)
### Task 02: Type Introspection
- **Requirement:** Inspect types of 'Python' and 3.1415 using `type()`.
- **PL:** Sprawdź typ wartości 'Python' i 3.1415.
- **Solution:** [`solutions/task_02.py`](solutions/task_02.py)
### Task 03: Power Calculation
- **Requirement:** Create `x = 6` and compute `x ** 3`.
- **PL:** Utwórz zmienną `x = 6` i oblicz `x ** 3`.
- **Solution:** [`solutions/task_03.py`](solutions/task_03.py)
### Task 04: Lexicographical Comparison
- **Requirement:** Check if 'banana' is greater than 'apple' in lexicographical order.
- **PL:** Sprawdź, czy 'banan' jest większe od 'jabłko'.
- **Solution:** [`solutions/task_04.py`](solutions/task_04.py)
### Task 05: Function Rapid Testing
- **Requirement:** Define `square(n) -> n * n` and test it with 7.
- **PL:** Zdefiniuj funkcję `kwadrat(n)` zwracającą `n * n` i przetestuj dla 7.
- **Solution:** [`solutions/task_05.py`](solutions/task_05.py)
### Task 06: REPL Interactive Echo
- **Requirement:** Prompt for name in REPL style and echo it immediately.
- **PL:** Użyj `input()` w REPL, wpisz swoje imię i wyświetl je.
- **Solution:** [`solutions/task_06.py`](solutions/task_06.py)
### Task 07: Padded Integer Parse
- **Requirement:** Test how `int('   50   ')` handles leading and trailing spaces.
- **PL:** Sprawdź działanie `int('   50   ')`.
- **Solution:** [`solutions/task_07.py`](solutions/task_07.py)
### Task 08: Float Rounding
- **Requirement:** Inspect behavior of `round(2.71828, 2)`.
- **PL:** Sprawdź, co robi `round(2.71828, 2)`.
- **Solution:** [`solutions/task_08.py`](solutions/task_08.py)
### Task 09: Truthiness of Non-Empty String
- **Requirement:** Inspect return value of `bool('False')`.
- **PL:** Sprawdź, co zwróci `bool('False')`.
- **Solution:** [`solutions/task_09.py`](solutions/task_09.py)
### Task 10: Exception Inspection
- **Requirement:** Attempt `10 / 0` inside try/except and print error type and message.
- **PL:** Spróbuj wykonać `10 / 0` i odczytaj typ błędu.
- **Solution:** [`solutions/task_10.py`](solutions/task_10.py)
### Task 11: List Length Inspection
- **Requirement:** Create list `[5, 10, 15]` and check `len(my_list)`.
- **PL:** Utwórz listę `[5, 10, 15]` i sprawdź `len(lista)`.
- **Solution:** [`solutions/task_11.py`](solutions/task_11.py)
### Task 12: Substring Search
- **Requirement:** Check whether 'gram' is present in 'programming' using the `in` keyword.
- **PL:** Sprawdź, czy napis 'programowanie' zawiera podnapis 'gram'.
- **Solution:** [`solutions/task_12.py`](solutions/task_12.py)
### Task 13: String Multiplication
- **Requirement:** Calculate `'Ha' * 5` and inspect the repeated string.
- **PL:** Oblicz `'Ha' * 5`.
- **Solution:** [`solutions/task_13.py`](solutions/task_13.py)
### Task 14: Type of None
- **Requirement:** Inspect `type(None)`.
- **PL:** Sprawdź, co zwróci `type(None)`.
- **Solution:** [`solutions/task_14.py`](solutions/task_14.py)
### Task 15: Built-in Docstring Help
- **Requirement:** Inspect docstring of `print` function using `print.__doc__`.
- **PL:** Wpisz `help(print)` i przeczytaj dokumentację.
- **Solution:** [`solutions/task_15.py`](solutions/task_15.py)

---
[Back to Part 1 Curriculum](../README.md)

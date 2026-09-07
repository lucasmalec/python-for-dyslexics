# Module 9: F-Strings & String Formatting

[🇬🇧 English](README.md) | [🇵🇱 Polski](README.pl.md)

---

## 🎯 About This Module
Master modern f-strings: padding, table alignment, number precision, date formats, and expressions.

- **Visual Limit:** Max 88 characters per line (PEP 8 / Black standard).
- **Format:** 15 hands-on progressive tasks with full English solutions.

---

## 📝 15 Hands-on Tasks

### Task 01: Basic F-String Interpolation
- **Requirement:** Display 'My name is Anna and I am 30 years old.' using variables `name` and `age`.
- **PL:** Używając f-stringa, wyświetl: 'Mam na imię Anna i mam 30 lat.' (zmienne `imie`, `wiek`).
- **Solution:** [`solutions/task_01.py`](solutions/task_01.py)
### Task 02: Pi Precision Formatting
- **Requirement:** Display pi = 3.1415926535 with 2 decimal places precision.
- **PL:** Wyświetl liczbę π = 3.1415926535 z dokładnością do 2 miejsc po przecinku.
- **Solution:** [`solutions/task_02.py`](solutions/task_02.py)
### Task 03: Fraction Division Precision
- **Requirement:** Display result of division 22/7 formatted to 3 decimal places.
- **PL:** Wyświetl wynik dzielenia 22/7 z dokładnością do 3 miejsc po przecinku.
- **Solution:** [`solutions/task_03.py`](solutions/task_03.py)
### Task 04: In-line Arithmetic in F-Strings
- **Requirement:** Evaluate arithmetic inside f-string: 'Sum of 5 and 7 is {5 + 7}'.
- **PL:** W f-stringu wykonaj obliczenie: 'Suma 5 i 7 to {5+7}'.
- **Solution:** [`solutions/task_04.py`](solutions/task_04.py)
### Task 05: Quotes Handling in F-Strings
- **Requirement:** Display: This is a 'quote' inside text using f-strings cleanly.
- **PL:** Wyświetl tekst: To jest 'cytat' w tekście używając f-stringa bez ucieczki.
- **Solution:** [`solutions/task_05.py`](solutions/task_05.py)
### Task 06: Column Alignment and Padding
- **Requirement:** Display aligned table row: `| Name: Casper   | Age: 25   |` using width padding.
- **PL:** Wyświetl tabelkę: `| imię: Kacper | wiek: 25 |` z wyrównaniem do 10 znaków.
- **Solution:** [`solutions/task_06.py`](solutions/task_06.py)
### Task 07: Leading Zeros Date Formatting
- **Requirement:** Display date in DD-MM-YYYY format with zero padding (e.g. 05-03-2026). Includes multiple approaches.
- **PL:** Wyświetl datę w formacie `DD-MM-RRRR` z zerami wiodącymi (np. `05-03-2026`).
- **Solution:** [`solutions/task_07.py`](solutions/task_07.py)
### Task 08: Percentage Formatting
- **Requirement:** Format decimal fraction 0.8567 as percentage: 85.67%.
- **PL:** Wyświetl procent 0.8567 jako `85.67%`.
- **Solution:** [`solutions/task_08.py`](solutions/task_08.py)
### Task 09: Thousands Separators
- **Requirement:** Format large integer 1234567 with commas as thousands separators: 1,234,567.
- **PL:** Wyświetl liczbę 1234567 z separatorami tysięcy: `1,234,567`.
- **Solution:** [`solutions/task_09.py`](solutions/task_09.py)
### Task 10: Function Invocation in Expressions
- **Requirement:** Call `len('Python')` directly inside f-string interpolation braces `{}`.
- **PL:** W f-stringu wywołaj funkcję `len('Python')` wewnątrz `{}`.
- **Solution:** [`solutions/task_10.py`](solutions/task_10.py)
### Task 11: Binary Number Representation
- **Requirement:** Display integer 255 formatted in binary notation using `{:b}`.
- **PL:** Wyświetl liczbę 255 w systemie binarnym.
- **Solution:** [`solutions/task_11.py`](solutions/task_11.py)
### Task 12: Explicit Positive/Negative Sign
- **Requirement:** Display number 3.14 with an explicit sign: +3.14.
- **PL:** Wyświetl liczbę 3.14 ze znakiem: `+3.14`.
- **Solution:** [`solutions/task_12.py`](solutions/task_12.py)
### Task 13: Dictionary Field Interpolation
- **Requirement:** Create dict `person = {'name': 'Eve', 'age': 28}` and format its contents.
- **PL:** Utwórz słownik `osoba = {'imie': 'Ewa', 'wiek': 28}` i wyświetl jego zawartość za pomocą f-stringa.
- **Solution:** [`solutions/task_13.py`](solutions/task_13.py)
### Task 14: Scientific Notation
- **Requirement:** Display number 0.0001234 in scientific exponential notation.
- **PL:** Wyświetl liczbę 0.0001234 w notacji naukowej.
- **Solution:** [`solutions/task_14.py`](solutions/task_14.py)
### Task 15: Direct Prompt Greeting F-String
- **Requirement:** Combine input prompt and greeting interpolation cleanly.
- **PL:** Połącz f-stringa z `input()` w jednej linii: zapytaj o imię i od razu wyświetl powitanie.
- **Solution:** [`solutions/task_15.py`](solutions/task_15.py)

---
[Back to Part 1 Curriculum](../README.md)

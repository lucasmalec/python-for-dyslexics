# Moduł 9: F-Stringi i Formatowanie Napisów

[🇬🇧 English](README.md) | [🇵🇱 Polski](README.pl.md)

---

## 🎯 O tym module
Opanowanie f-stringów: dopełnianie zerami, wyrównywanie tabel, precyzja float i formatowanie dat.

- **Limit wizualny:** Maksymalnie 88 znaków w wierszu (standard PEP 8 / Black).
- **Format:** 15 praktycznych zadań krok po kroku z gotowymi rozwiązaniami w języku angielskim.

---

## 📝 15 Praktycznych Zadań

### Zadanie 01: Basic F-String Interpolation
- **Treść:** Używając f-stringa, wyświetl: 'Mam na imię Anna i mam 30 lat.' (zmienne `imie`, `wiek`).
- **EN:** Display 'My name is Anna and I am 30 years old.' using variables `name` and `age`.
- **Rozwiązanie:** [`solutions/task_01.py`](solutions/task_01.py)
### Zadanie 02: Pi Precision Formatting
- **Treść:** Wyświetl liczbę π = 3.1415926535 z dokładnością do 2 miejsc po przecinku.
- **EN:** Display pi = 3.1415926535 with 2 decimal places precision.
- **Rozwiązanie:** [`solutions/task_02.py`](solutions/task_02.py)
### Zadanie 03: Fraction Division Precision
- **Treść:** Wyświetl wynik dzielenia 22/7 z dokładnością do 3 miejsc po przecinku.
- **EN:** Display result of division 22/7 formatted to 3 decimal places.
- **Rozwiązanie:** [`solutions/task_03.py`](solutions/task_03.py)
### Zadanie 04: In-line Arithmetic in F-Strings
- **Treść:** W f-stringu wykonaj obliczenie: 'Suma 5 i 7 to {5+7}'.
- **EN:** Evaluate arithmetic inside f-string: 'Sum of 5 and 7 is {5 + 7}'.
- **Rozwiązanie:** [`solutions/task_04.py`](solutions/task_04.py)
### Zadanie 05: Quotes Handling in F-Strings
- **Treść:** Wyświetl tekst: To jest 'cytat' w tekście używając f-stringa bez ucieczki.
- **EN:** Display: This is a 'quote' inside text using f-strings cleanly.
- **Rozwiązanie:** [`solutions/task_05.py`](solutions/task_05.py)
### Zadanie 06: Column Alignment and Padding
- **Treść:** Wyświetl tabelkę: `| imię: Kacper | wiek: 25 |` z wyrównaniem do 10 znaków.
- **EN:** Display aligned table row: `| Name: Casper   | Age: 25   |` using width padding.
- **Rozwiązanie:** [`solutions/task_06.py`](solutions/task_06.py)
### Zadanie 07: Leading Zeros Date Formatting
- **Treść:** Wyświetl datę w formacie `DD-MM-RRRR` z zerami wiodącymi (np. `05-03-2026`).
- **EN:** Display date in DD-MM-YYYY format with zero padding (e.g. 05-03-2026). Includes multiple approaches.
- **Rozwiązanie:** [`solutions/task_07.py`](solutions/task_07.py)
### Zadanie 08: Percentage Formatting
- **Treść:** Wyświetl procent 0.8567 jako `85.67%`.
- **EN:** Format decimal fraction 0.8567 as percentage: 85.67%.
- **Rozwiązanie:** [`solutions/task_08.py`](solutions/task_08.py)
### Zadanie 09: Thousands Separators
- **Treść:** Wyświetl liczbę 1234567 z separatorami tysięcy: `1,234,567`.
- **EN:** Format large integer 1234567 with commas as thousands separators: 1,234,567.
- **Rozwiązanie:** [`solutions/task_09.py`](solutions/task_09.py)
### Zadanie 10: Function Invocation in Expressions
- **Treść:** W f-stringu wywołaj funkcję `len('Python')` wewnątrz `{}`.
- **EN:** Call `len('Python')` directly inside f-string interpolation braces `{}`.
- **Rozwiązanie:** [`solutions/task_10.py`](solutions/task_10.py)
### Zadanie 11: Binary Number Representation
- **Treść:** Wyświetl liczbę 255 w systemie binarnym.
- **EN:** Display integer 255 formatted in binary notation using `{:b}`.
- **Rozwiązanie:** [`solutions/task_11.py`](solutions/task_11.py)
### Zadanie 12: Explicit Positive/Negative Sign
- **Treść:** Wyświetl liczbę 3.14 ze znakiem: `+3.14`.
- **EN:** Display number 3.14 with an explicit sign: +3.14.
- **Rozwiązanie:** [`solutions/task_12.py`](solutions/task_12.py)
### Zadanie 13: Dictionary Field Interpolation
- **Treść:** Utwórz słownik `osoba = {'imie': 'Ewa', 'wiek': 28}` i wyświetl jego zawartość za pomocą f-stringa.
- **EN:** Create dict `person = {'name': 'Eve', 'age': 28}` and format its contents.
- **Rozwiązanie:** [`solutions/task_13.py`](solutions/task_13.py)
### Zadanie 14: Scientific Notation
- **Treść:** Wyświetl liczbę 0.0001234 w notacji naukowej.
- **EN:** Display number 0.0001234 in scientific exponential notation.
- **Rozwiązanie:** [`solutions/task_14.py`](solutions/task_14.py)
### Zadanie 15: Direct Prompt Greeting F-String
- **Treść:** Połącz f-stringa z `input()` w jednej linii: zapytaj o imię i od razu wyświetl powitanie.
- **EN:** Combine input prompt and greeting interpolation cleanly.
- **Rozwiązanie:** [`solutions/task_15.py`](solutions/task_15.py)

---
[Powrót do Spisu Treści Części 1](../README.pl.md)

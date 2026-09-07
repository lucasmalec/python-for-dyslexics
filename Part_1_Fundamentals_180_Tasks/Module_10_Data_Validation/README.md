# Module 10: Data Validation & Error Handling

[🇬🇧 English](README.md) | [🇵🇱 Polski](README.pl.md)

---

## 🎯 About This Module
Implement defensive programming using try/except, input sanitization, and value boundary assertions.

- **Visual Limit:** Max 88 characters per line (PEP 8 / Black standard).
- **Format:** 15 hands-on progressive tasks with full English solutions.

---

## 📝 15 Hands-on Tasks

### Task 01: Integer Parsing with try/except
- **Requirement:** Prompt for an integer and handle `ValueError` gracefully using `try/except`.
- **PL:** Poproś użytkownika o liczbę całkowitą. Użyj `try/except` do obsługi `ValueError`.
- **Solution:** [`solutions/task_01.py`](solutions/task_01.py)
### Task 02: Whitespace Sanitization Before Parse
- **Requirement:** Prompt for number and use `.strip()` prior to conversion to eliminate spaces.
- **PL:** Poproś o liczbę, użyj `strip()` przed konwersją, aby usunąć spacje.
- **Solution:** [`solutions/task_02.py`](solutions/task_02.py)
### Task 03: Empty String Guard
- **Requirement:** Prompt for text. If empty, notify user: 'No text provided.'.
- **PL:** Poproś o tekst. Jeśli użytkownik nic nie wpisze, wyświetl: 'Nie podano tekstu.'
- **Solution:** [`solutions/task_03.py`](solutions/task_03.py)
### Task 04: Float Parsing Guard
- **Requirement:** Prompt for a decimal float and handle invalid string inputs.
- **PL:** Poproś o liczbę zmiennoprzecinkową. Obsłuż błąd, jeśli użytkownik poda coś innego.
- **Solution:** [`solutions/task_04.py`](solutions/task_04.py)
### Task 05: Looping Integer Validator
- **Requirement:** Write function `get_integer(prompt)` that loops until a valid integer is entered.
- **PL:** Napisz funkcję `pobierz_int()`, która pyta aż do podania poprawnej liczby całkowitej.
- **Solution:** [`solutions/task_05.py`](solutions/task_05.py)
### Task 06: Age Range Assertion
- **Requirement:** Prompt for age and verify it falls within valid human bounds: 0 to 120.
- **PL:** Poproś o wiek. Jeśli wiek nie mieści się w zakresie 0–120, wyświetl błąd.
- **Solution:** [`solutions/task_06.py`](solutions/task_06.py)
### Task 07: Strictly Positive Number Guard
- **Requirement:** Prompt for positive number (> 0). Reject zero or negative inputs.
- **PL:** Poproś o liczbę dodatnią. Jeśli użytkownik poda 0 lub ujemną, wyświetl komunikat.
- **Solution:** [`solutions/task_07.py`](solutions/task_07.py)
### Task 08: Alphabetic Only Name Check
- **Requirement:** Prompt for text and verify it contains no numeric digits.
- **PL:** Poproś o tekst i sprawdź, czy nie zawiera cyfr.
- **Solution:** [`solutions/task_08.py`](solutions/task_08.py)
### Task 09: ZeroDivisionError Exception Handler
- **Requirement:** Prompt for two numbers and handle `ZeroDivisionError` with a try/except block.
- **PL:** Poproś o dwie liczby i wykonaj dzielenie. Obsłuż błąd dzielenia przez zero.
- **Solution:** [`solutions/task_09.py`](solutions/task_09.py)
### Task 10: LBYL Defensive Division Guard
- **Requirement:** Check denominator before division (Look Before You Leap pattern).
- **PL:** Poproś o dwie liczby. Sprawdź, czy druga liczba nie jest zerem przed dzieleniem.
- **Solution:** [`solutions/task_10.py`](solutions/task_10.py)
### Task 11: Year Range Validation
- **Requirement:** Prompt for a year and verify it falls within range 1900 to 2026.
- **PL:** Poproś o rok. Sprawdź, czy rok jest z zakresu 1900–2026.
- **Solution:** [`solutions/task_11.py`](solutions/task_11.py)
### Task 12: Full try-except-else-finally Flow
- **Requirement:** Implement complete `try/except/else/finally` control flow.
- **PL:** Użyj bloku `try/except/else/finally` – w `else` wyświetl wynik, w `finally` napisz 'Koniec operacji'.
- **Solution:** [`solutions/task_12.py`](solutions/task_12.py)
### Task 13: Allowed Options Whitelist
- **Requirement:** Prompt for color from whitelist: ['red', 'green', 'blue']. Reject other choices.
- **PL:** Poproś o kolor z listy: czerwony, zielony, niebieski. Jeśli nie ma na liście, wyświetl błąd.
- **Solution:** [`solutions/task_13.py`](solutions/task_13.py)
### Task 14: Divisibility Prime Check
- **Requirement:** Check if an integer > 3 is divisible by 2 or 3 as a baseline primality check.
- **PL:** Poproś o liczbę i sprawdź, czy jest liczbą pierwszą (dla uproszczenia sprawdź podzielność przez 2 i 3).
- **Solution:** [`solutions/task_14.py`](solutions/task_14.py)
### Task 15: Multi-field Validation Pipeline
- **Requirement:** Combine non-empty name check, bounded age (0-120), and lucky number in one program.
- **PL:** Połącz walidację imienia (niepusty tekst), wieku (liczba 0–120) i ulubionej liczby w jednym programie.
- **Solution:** [`solutions/task_15.py`](solutions/task_15.py)

---
[Back to Part 1 Curriculum](../README.md)

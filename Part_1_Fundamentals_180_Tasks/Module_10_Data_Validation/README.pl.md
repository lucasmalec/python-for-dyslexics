# Moduł 10: Walidacja Danych i Obsługa Błędów

[🇬🇧 English](README.md) | [🇵🇱 Polski](README.pl.md)

---

## 🎯 O tym module
Wdrażanie defensywnego programowania z try/except, strip() i weryfikacją zakresów wartości.

- **Limit wizualny:** Maksymalnie 88 znaków w wierszu (standard PEP 8 / Black).
- **Format:** 15 praktycznych zadań krok po kroku z gotowymi rozwiązaniami w języku angielskim.

---

## 📝 15 Praktycznych Zadań

### Zadanie 01: Integer Parsing with try/except
- **Treść:** Poproś użytkownika o liczbę całkowitą. Użyj `try/except` do obsługi `ValueError`.
- **EN:** Prompt for an integer and handle `ValueError` gracefully using `try/except`.
- **Rozwiązanie:** [`solutions/task_01.py`](solutions/task_01.py)
### Zadanie 02: Whitespace Sanitization Before Parse
- **Treść:** Poproś o liczbę, użyj `strip()` przed konwersją, aby usunąć spacje.
- **EN:** Prompt for number and use `.strip()` prior to conversion to eliminate spaces.
- **Rozwiązanie:** [`solutions/task_02.py`](solutions/task_02.py)
### Zadanie 03: Empty String Guard
- **Treść:** Poproś o tekst. Jeśli użytkownik nic nie wpisze, wyświetl: 'Nie podano tekstu.'
- **EN:** Prompt for text. If empty, notify user: 'No text provided.'.
- **Rozwiązanie:** [`solutions/task_03.py`](solutions/task_03.py)
### Zadanie 04: Float Parsing Guard
- **Treść:** Poproś o liczbę zmiennoprzecinkową. Obsłuż błąd, jeśli użytkownik poda coś innego.
- **EN:** Prompt for a decimal float and handle invalid string inputs.
- **Rozwiązanie:** [`solutions/task_04.py`](solutions/task_04.py)
### Zadanie 05: Looping Integer Validator
- **Treść:** Napisz funkcję `pobierz_int()`, która pyta aż do podania poprawnej liczby całkowitej.
- **EN:** Write function `get_integer(prompt)` that loops until a valid integer is entered.
- **Rozwiązanie:** [`solutions/task_05.py`](solutions/task_05.py)
### Zadanie 06: Age Range Assertion
- **Treść:** Poproś o wiek. Jeśli wiek nie mieści się w zakresie 0–120, wyświetl błąd.
- **EN:** Prompt for age and verify it falls within valid human bounds: 0 to 120.
- **Rozwiązanie:** [`solutions/task_06.py`](solutions/task_06.py)
### Zadanie 07: Strictly Positive Number Guard
- **Treść:** Poproś o liczbę dodatnią. Jeśli użytkownik poda 0 lub ujemną, wyświetl komunikat.
- **EN:** Prompt for positive number (> 0). Reject zero or negative inputs.
- **Rozwiązanie:** [`solutions/task_07.py`](solutions/task_07.py)
### Zadanie 08: Alphabetic Only Name Check
- **Treść:** Poproś o tekst i sprawdź, czy nie zawiera cyfr.
- **EN:** Prompt for text and verify it contains no numeric digits.
- **Rozwiązanie:** [`solutions/task_08.py`](solutions/task_08.py)
### Zadanie 09: ZeroDivisionError Exception Handler
- **Treść:** Poproś o dwie liczby i wykonaj dzielenie. Obsłuż błąd dzielenia przez zero.
- **EN:** Prompt for two numbers and handle `ZeroDivisionError` with a try/except block.
- **Rozwiązanie:** [`solutions/task_09.py`](solutions/task_09.py)
### Zadanie 10: LBYL Defensive Division Guard
- **Treść:** Poproś o dwie liczby. Sprawdź, czy druga liczba nie jest zerem przed dzieleniem.
- **EN:** Check denominator before division (Look Before You Leap pattern).
- **Rozwiązanie:** [`solutions/task_10.py`](solutions/task_10.py)
### Zadanie 11: Year Range Validation
- **Treść:** Poproś o rok. Sprawdź, czy rok jest z zakresu 1900–2026.
- **EN:** Prompt for a year and verify it falls within range 1900 to 2026.
- **Rozwiązanie:** [`solutions/task_11.py`](solutions/task_11.py)
### Zadanie 12: Full try-except-else-finally Flow
- **Treść:** Użyj bloku `try/except/else/finally` – w `else` wyświetl wynik, w `finally` napisz 'Koniec operacji'.
- **EN:** Implement complete `try/except/else/finally` control flow.
- **Rozwiązanie:** [`solutions/task_12.py`](solutions/task_12.py)
### Zadanie 13: Allowed Options Whitelist
- **Treść:** Poproś o kolor z listy: czerwony, zielony, niebieski. Jeśli nie ma na liście, wyświetl błąd.
- **EN:** Prompt for color from whitelist: ['red', 'green', 'blue']. Reject other choices.
- **Rozwiązanie:** [`solutions/task_13.py`](solutions/task_13.py)
### Zadanie 14: Divisibility Prime Check
- **Treść:** Poproś o liczbę i sprawdź, czy jest liczbą pierwszą (dla uproszczenia sprawdź podzielność przez 2 i 3).
- **EN:** Check if an integer > 3 is divisible by 2 or 3 as a baseline primality check.
- **Rozwiązanie:** [`solutions/task_14.py`](solutions/task_14.py)
### Zadanie 15: Multi-field Validation Pipeline
- **Treść:** Połącz walidację imienia (niepusty tekst), wieku (liczba 0–120) i ulubionej liczby w jednym programie.
- **EN:** Combine non-empty name check, bounded age (0-120), and lucky number in one program.
- **Rozwiązanie:** [`solutions/task_15.py`](solutions/task_15.py)

---
[Powrót do Spisu Treści Części 1](../README.pl.md)

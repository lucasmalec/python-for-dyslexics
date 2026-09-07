# Moduł 7: Ćwiczenia Rozszerzone

[🇬🇧 English](README.md) | [🇵🇱 Polski](README.pl.md)

---

## 🎯 O tym module
Krok po kroku łącz walidację wejścia, obliczenia numeryczne i interaktywne scenariusze terminalowe.

- **Limit wizualny:** Maksymalnie 88 znaków w wierszu (standard PEP 8 / Black).
- **Format:** 15 praktycznych zadań krok po kroku z gotowymi rozwiązaniami w języku angielskim.

---

## 📝 15 Praktycznych Zadań

### Zadanie 01: Basic User Profile Interaction
- **Treść:** Podstawowa wersja: poproś o imię, wiek, ulubioną liczbę. Wyświetl: 'Cześć [imię]! Za 10 lat będziesz mieć [wiek+10] lat, a Twoja liczba razy 3 to [liczba*3].'
- **EN:** Prompt for name, age, lucky number. Display future age in 10 years and number * 3.
- **Rozwiązanie:** [`solutions/task_01.py`](solutions/task_01.py)
### Zadanie 02: Explicit Type Conversions
- **Treść:** Dodaj konwersję wieku i liczby na `int` (użyj `int()`).
- **EN:** Add explicit int conversion for age and lucky number using `int()`.
- **Rozwiązanie:** [`solutions/task_02.py`](solutions/task_02.py)
### Zadanie 03: F-String Formatting Integration
- **Treść:** Sformatuj wynik za pomocą f-stringa.
- **EN:** Format results cleanly using modern Python f-strings.
- **Rozwiązanie:** [`solutions/task_03.py`](solutions/task_03.py)
### Zadanie 04: Digit String Validation
- **Treść:** Dodaj walidację: jeśli użytkownik poda wiek niebędący liczbą, wyświetl komunikat błędu.
- **EN:** Add validation: check if age input contains only digits using `.isdigit()`.
- **Rozwiązanie:** [`solutions/task_04.py`](solutions/task_04.py)
### Zadanie 05: Decimal Precision Display
- **Treść:** Oblicz wiek za 10 lat i wyświetl go z dwoma miejscami po przecinku (np. 30.00).
- **EN:** Calculate future age and format it with two decimal places (e.g. 30.00).
- **Rozwiązanie:** [`solutions/task_05.py`](solutions/task_05.py)
### Zadanie 06: Exception Handling for Input Parsing
- **Treść:** Dodaj obsługę `ValueError` przy konwersji wieku i liczby.
- **EN:** Handle `ValueError` when converting age and number inputs.
- **Rozwiązanie:** [`solutions/task_06.py`](solutions/task_06.py)
### Zadanie 07: String Sanitization with strip
- **Treść:** Użyj `strip()` przed konwersją, aby usunąć przypadkowe spacje.
- **EN:** Apply `.strip()` on inputs to eliminate accidental leading and trailing whitespace.
- **Rozwiązanie:** [`solutions/task_07.py`](solutions/task_07.py)
### Zadanie 08: Favorite Color Integration
- **Treść:** Dodaj pytanie o ulubiony kolor i wpleć go w zdanie.
- **EN:** Prompt for favorite color and seamlessly weave it into the user bio sentence.
- **Rozwiązanie:** [`solutions/task_08.py`](solutions/task_08.py)
### Zadanie 09: Square Root on Secondary Number
- **Treść:** Zapytaj o dodatkową liczbę i wyświetl jej pierwiastek kwadratowy.
- **EN:** Prompt for an additional number and compute its square root.
- **Rozwiązanie:** [`solutions/task_09.py`](solutions/task_09.py)
### Zadanie 10: Dual Favorite Numbers Math
- **Treść:** Zapytaj o dwie ulubione liczby, wyświetl ich sumę, różnicę i iloczyn.
- **EN:** Prompt for two numbers; display their sum, difference, and product.
- **Rozwiązanie:** [`solutions/task_10.py`](solutions/task_10.py)
### Zadanie 11: Unified Multi-line F-String
- **Treść:** Wyświetl wszystkie dane w jednym zdaniu z użyciem jednego f-stringa.
- **EN:** Display all gathered user attributes in a single, well-structured f-string.
- **Rozwiązanie:** [`solutions/task_11.py`](solutions/task_11.py)
### Zadanie 12: Retry Loop on Parsing Errors
- **Treść:** Dodaj pętlę, aby program pytał ponownie w przypadku błędu.
- **EN:** Add a `while True` loop to continuously re-prompt until a valid integer is provided.
- **Rozwiązanie:** [`solutions/task_12.py`](solutions/task_12.py)
### Zadanie 13: Date of Birth Age Resolution
- **Treść:** Zapytaj o datę urodzenia (dzień, miesiąc, rok) i oblicz dokładny wiek.
- **EN:** Prompt for birth day, month, year, and compute approximate age in 2026.
- **Rozwiązanie:** [`solutions/task_13.py`](solutions/task_13.py)
### Zadanie 14: Color to HEX Code Lookup
- **Treść:** Zapytaj o ulubiony kolor i wyświetl jego kod HEX (np. #FF0000 dla czerwonego – użyj słownika).
- **EN:** Ask for favorite color and look up its HEX color code using a dictionary.
- **Rozwiązanie:** [`solutions/task_14.py`](solutions/task_14.py)
### Zadanie 15: Comprehensive Registration Engine
- **Treść:** Połącz wszystko: walidacja, f-stringi, konwersje, obliczenia i czytelne komunikaty.
- **EN:** Integrate validation, loops, math, f-strings, and error handling into a coherent profile tool.
- **Rozwiązanie:** [`solutions/task_15.py`](solutions/task_15.py)

---
[Powrót do Spisu Treści Części 1](../README.pl.md)

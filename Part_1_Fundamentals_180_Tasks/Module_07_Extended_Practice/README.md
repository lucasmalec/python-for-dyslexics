# Module 7: Extended Hands-on Practice

[🇬🇧 English](README.md) | [🇵🇱 Polski](README.pl.md)

---

## 🎯 About This Module
Integrate user input sanitization, math calculations, and interactive workflows step-by-step.

- **Visual Limit:** Max 88 characters per line (PEP 8 / Black standard).
- **Format:** 15 hands-on progressive tasks with full English solutions.

---

## 📝 15 Hands-on Tasks

### Task 01: Basic User Profile Interaction
- **Requirement:** Prompt for name, age, lucky number. Display future age in 10 years and number * 3.
- **PL:** Podstawowa wersja: poproś o imię, wiek, ulubioną liczbę. Wyświetl: 'Cześć [imię]! Za 10 lat będziesz mieć [wiek+10] lat, a Twoja liczba razy 3 to [liczba*3].'
- **Solution:** [`solutions/task_01.py`](solutions/task_01.py)
### Task 02: Explicit Type Conversions
- **Requirement:** Add explicit int conversion for age and lucky number using `int()`.
- **PL:** Dodaj konwersję wieku i liczby na `int` (użyj `int()`).
- **Solution:** [`solutions/task_02.py`](solutions/task_02.py)
### Task 03: F-String Formatting Integration
- **Requirement:** Format results cleanly using modern Python f-strings.
- **PL:** Sformatuj wynik za pomocą f-stringa.
- **Solution:** [`solutions/task_03.py`](solutions/task_03.py)
### Task 04: Digit String Validation
- **Requirement:** Add validation: check if age input contains only digits using `.isdigit()`.
- **PL:** Dodaj walidację: jeśli użytkownik poda wiek niebędący liczbą, wyświetl komunikat błędu.
- **Solution:** [`solutions/task_04.py`](solutions/task_04.py)
### Task 05: Decimal Precision Display
- **Requirement:** Calculate future age and format it with two decimal places (e.g. 30.00).
- **PL:** Oblicz wiek za 10 lat i wyświetl go z dwoma miejscami po przecinku (np. 30.00).
- **Solution:** [`solutions/task_05.py`](solutions/task_05.py)
### Task 06: Exception Handling for Input Parsing
- **Requirement:** Handle `ValueError` when converting age and number inputs.
- **PL:** Dodaj obsługę `ValueError` przy konwersji wieku i liczby.
- **Solution:** [`solutions/task_06.py`](solutions/task_06.py)
### Task 07: String Sanitization with strip
- **Requirement:** Apply `.strip()` on inputs to eliminate accidental leading and trailing whitespace.
- **PL:** Użyj `strip()` przed konwersją, aby usunąć przypadkowe spacje.
- **Solution:** [`solutions/task_07.py`](solutions/task_07.py)
### Task 08: Favorite Color Integration
- **Requirement:** Prompt for favorite color and seamlessly weave it into the user bio sentence.
- **PL:** Dodaj pytanie o ulubiony kolor i wpleć go w zdanie.
- **Solution:** [`solutions/task_08.py`](solutions/task_08.py)
### Task 09: Square Root on Secondary Number
- **Requirement:** Prompt for an additional number and compute its square root.
- **PL:** Zapytaj o dodatkową liczbę i wyświetl jej pierwiastek kwadratowy.
- **Solution:** [`solutions/task_09.py`](solutions/task_09.py)
### Task 10: Dual Favorite Numbers Math
- **Requirement:** Prompt for two numbers; display their sum, difference, and product.
- **PL:** Zapytaj o dwie ulubione liczby, wyświetl ich sumę, różnicę i iloczyn.
- **Solution:** [`solutions/task_10.py`](solutions/task_10.py)
### Task 11: Unified Multi-line F-String
- **Requirement:** Display all gathered user attributes in a single, well-structured f-string.
- **PL:** Wyświetl wszystkie dane w jednym zdaniu z użyciem jednego f-stringa.
- **Solution:** [`solutions/task_11.py`](solutions/task_11.py)
### Task 12: Retry Loop on Parsing Errors
- **Requirement:** Add a `while True` loop to continuously re-prompt until a valid integer is provided.
- **PL:** Dodaj pętlę, aby program pytał ponownie w przypadku błędu.
- **Solution:** [`solutions/task_12.py`](solutions/task_12.py)
### Task 13: Date of Birth Age Resolution
- **Requirement:** Prompt for birth day, month, year, and compute approximate age in 2026.
- **PL:** Zapytaj o datę urodzenia (dzień, miesiąc, rok) i oblicz dokładny wiek.
- **Solution:** [`solutions/task_13.py`](solutions/task_13.py)
### Task 14: Color to HEX Code Lookup
- **Requirement:** Ask for favorite color and look up its HEX color code using a dictionary.
- **PL:** Zapytaj o ulubiony kolor i wyświetl jego kod HEX (np. #FF0000 dla czerwonego – użyj słownika).
- **Solution:** [`solutions/task_14.py`](solutions/task_14.py)
### Task 15: Comprehensive Registration Engine
- **Requirement:** Integrate validation, loops, math, f-strings, and error handling into a coherent profile tool.
- **PL:** Połącz wszystko: walidacja, f-stringi, konwersje, obliczenia i czytelne komunikaty.
- **Solution:** [`solutions/task_15.py`](solutions/task_15.py)

---
[Back to Part 1 Curriculum](../README.md)

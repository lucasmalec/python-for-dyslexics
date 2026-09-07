# Module 4: Type Casting & Conversions

[🇬🇧 English](README.md) | [🇵🇱 Polski](README.pl.md)

---

## 🎯 About This Module
Master explicit type casting between strings, integers, floats, and truthiness evaluation.

- **Visual Limit:** Max 88 characters per line (PEP 8 / Black standard).
- **Format:** 15 hands-on progressive tasks with full English solutions.

---

## 📝 15 Hands-on Tasks

### Task 01: String to Int and Addition
- **Requirement:** Convert string '250' to integer and add 75.
- **PL:** Zamień napis '250' na liczbę całkowitą i dodaj 75.
- **Solution:** [`solutions/task_01.py`](solutions/task_01.py)
### Task 02: String to Float and Multiplication
- **Requirement:** Convert string '6.28' to float and multiply by 3.
- **PL:** Zamień napis '6.28' na liczbę zmiennoprzecinkową i pomnóż przez 3.
- **Solution:** [`solutions/task_02.py`](solutions/task_02.py)
### Task 03: Number to String Concatenation
- **Requirement:** Convert number 99 to string and combine with ' problems'.
- **PL:** Zamień liczbę 99 na napis i połącz z napisem ' problemów'.
- **Solution:** [`solutions/task_03.py`](solutions/task_03.py)
### Task 04: Boolean Casting
- **Requirement:** Use `bool()` on values: 0, 1, '', 'Python'. Display results.
- **PL:** Użyj `bool()` na wartościach: 0, 1, '', 'Python'. Wyświetl wyniki.
- **Solution:** [`solutions/task_04.py`](solutions/task_04.py)
### Task 05: User Float Input Sum
- **Requirement:** Ask user for two decimal numbers as text, convert to float, and display sum.
- **PL:** Poproś użytkownika o dwie liczby (jako tekst), przekonwertuj je na `float` i wyświetl ich sumę.
- **Solution:** [`solutions/task_05.py`](solutions/task_05.py)
### Task 06: Float String to Integer Pitfall
- **Requirement:** Attempt `int('12.7')` and demonstrate the correct two-step conversion `int(float('12.7'))`.
- **PL:** Spróbuj zamienić napis '12.7' na `int`. Co się dzieje? Zapisz kod i zobacz efekt.
- **Solution:** [`solutions/task_06.py`](solutions/task_06.py)
### Task 07: List to String Representation
- **Requirement:** Use `str()` to concatenate list [1, 2, 3] with ' items'.
- **PL:** Użyj `str()` do połączenia listy `[1, 2, 3]` z napisem ' elementy'.
- **Solution:** [`solutions/task_07.py`](solutions/task_07.py)
### Task 08: String 'True' to Boolean Verification
- **Requirement:** Convert string 'True' to bool and observe why all non-empty strings are truthy.
- **PL:** Przekonwertuj napis 'True' na `bool` i wyświetl wynik.
- **Solution:** [`solutions/task_08.py`](solutions/task_08.py)
### Task 09: Whitespace Stripping Before Conversion
- **Requirement:** Convert string '   99   ' to int using `strip()`.
- **PL:** Zamień napis '   99   ' na `int` (użyj `strip()` przed konwersją).
- **Solution:** [`solutions/task_09.py`](solutions/task_09.py)
### Task 10: Chained Float and Int Conversion
- **Requirement:** Create `price_str = '49.99'`. Convert first to float, then to int. Display both.
- **PL:** Utwórz zmienną `cena = '49.99'`. Zamień ją najpierw na `float`, a potem na `int`. Wyświetl oba wyniki.
- **Solution:** [`solutions/task_10.py`](solutions/task_10.py)
### Task 11: String '0' Truthiness
- **Requirement:** Convert string '0' to bool – analyze the returned boolean.
- **PL:** Zamień napis '0' na `bool` – co otrzymasz?
- **Solution:** [`solutions/task_11.py`](solutions/task_11.py)
### Task 12: Exception Handling on Invalid Conversion
- **Requirement:** Try converting string 'abc' to int. Catch `ValueError` gracefully.
- **PL:** Spróbuj zamienić napis 'abc' na `int`. Użyj `try/except`, aby przechwycić błąd.
- **Solution:** [`solutions/task_12.py`](solutions/task_12.py)
### Task 13: Float to Int Truncation Analysis
- **Requirement:** Cast number 7.99 to int and inspect what happened to the decimal fraction.
- **PL:** Zamień liczbę 7.99 na `int` i wyświetl. Co się stało z częścią ułamkową?
- **Solution:** [`solutions/task_13.py`](solutions/task_13.py)
### Task 14: Defensive safe_int Function
- **Requirement:** Write function `safe_int(val)` returning parsed int or `None` on failure.
- **PL:** Napisz funkcję `bezpieczna_int(napis)`, która zwraca `None`, jeśli konwersja się nie uda.
- **Solution:** [`solutions/task_14.py`](solutions/task_14.py)
### Task 15: None to String
- **Requirement:** Convert `None` to string and display result.
- **PL:** Zamień wartość `None` na napis i wyświetl.
- **Solution:** [`solutions/task_15.py`](solutions/task_15.py)

---
[Back to Part 1 Curriculum](../README.md)

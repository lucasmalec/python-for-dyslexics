# Moduł 4: Konwersje Typów Danych

[🇬🇧 English](README.md) | [🇵🇱 Polski](README.pl.md)

---

## 🎯 O tym module
Opanowanie bezpiecznych konwersji między napisami, liczbami i ewaluacji logicznej (truthiness).

- **Limit wizualny:** Maksymalnie 88 znaków w wierszu (standard PEP 8 / Black).
- **Format:** 15 praktycznych zadań krok po kroku z gotowymi rozwiązaniami w języku angielskim.

---

## 📝 15 Praktycznych Zadań

### Zadanie 01: String to Int and Addition
- **Treść:** Zamień napis '250' na liczbę całkowitą i dodaj 75.
- **EN:** Convert string '250' to integer and add 75.
- **Rozwiązanie:** [`solutions/task_01.py`](solutions/task_01.py)
### Zadanie 02: String to Float and Multiplication
- **Treść:** Zamień napis '6.28' na liczbę zmiennoprzecinkową i pomnóż przez 3.
- **EN:** Convert string '6.28' to float and multiply by 3.
- **Rozwiązanie:** [`solutions/task_02.py`](solutions/task_02.py)
### Zadanie 03: Number to String Concatenation
- **Treść:** Zamień liczbę 99 na napis i połącz z napisem ' problemów'.
- **EN:** Convert number 99 to string and combine with ' problems'.
- **Rozwiązanie:** [`solutions/task_03.py`](solutions/task_03.py)
### Zadanie 04: Boolean Casting
- **Treść:** Użyj `bool()` na wartościach: 0, 1, '', 'Python'. Wyświetl wyniki.
- **EN:** Use `bool()` on values: 0, 1, '', 'Python'. Display results.
- **Rozwiązanie:** [`solutions/task_04.py`](solutions/task_04.py)
### Zadanie 05: User Float Input Sum
- **Treść:** Poproś użytkownika o dwie liczby (jako tekst), przekonwertuj je na `float` i wyświetl ich sumę.
- **EN:** Ask user for two decimal numbers as text, convert to float, and display sum.
- **Rozwiązanie:** [`solutions/task_05.py`](solutions/task_05.py)
### Zadanie 06: Float String to Integer Pitfall
- **Treść:** Spróbuj zamienić napis '12.7' na `int`. Co się dzieje? Zapisz kod i zobacz efekt.
- **EN:** Attempt `int('12.7')` and demonstrate the correct two-step conversion `int(float('12.7'))`.
- **Rozwiązanie:** [`solutions/task_06.py`](solutions/task_06.py)
### Zadanie 07: List to String Representation
- **Treść:** Użyj `str()` do połączenia listy `[1, 2, 3]` z napisem ' elementy'.
- **EN:** Use `str()` to concatenate list [1, 2, 3] with ' items'.
- **Rozwiązanie:** [`solutions/task_07.py`](solutions/task_07.py)
### Zadanie 08: String 'True' to Boolean Verification
- **Treść:** Przekonwertuj napis 'True' na `bool` i wyświetl wynik.
- **EN:** Convert string 'True' to bool and observe why all non-empty strings are truthy.
- **Rozwiązanie:** [`solutions/task_08.py`](solutions/task_08.py)
### Zadanie 09: Whitespace Stripping Before Conversion
- **Treść:** Zamień napis '   99   ' na `int` (użyj `strip()` przed konwersją).
- **EN:** Convert string '   99   ' to int using `strip()`.
- **Rozwiązanie:** [`solutions/task_09.py`](solutions/task_09.py)
### Zadanie 10: Chained Float and Int Conversion
- **Treść:** Utwórz zmienną `cena = '49.99'`. Zamień ją najpierw na `float`, a potem na `int`. Wyświetl oba wyniki.
- **EN:** Create `price_str = '49.99'`. Convert first to float, then to int. Display both.
- **Rozwiązanie:** [`solutions/task_10.py`](solutions/task_10.py)
### Zadanie 11: String '0' Truthiness
- **Treść:** Zamień napis '0' na `bool` – co otrzymasz?
- **EN:** Convert string '0' to bool – analyze the returned boolean.
- **Rozwiązanie:** [`solutions/task_11.py`](solutions/task_11.py)
### Zadanie 12: Exception Handling on Invalid Conversion
- **Treść:** Spróbuj zamienić napis 'abc' na `int`. Użyj `try/except`, aby przechwycić błąd.
- **EN:** Try converting string 'abc' to int. Catch `ValueError` gracefully.
- **Rozwiązanie:** [`solutions/task_12.py`](solutions/task_12.py)
### Zadanie 13: Float to Int Truncation Analysis
- **Treść:** Zamień liczbę 7.99 na `int` i wyświetl. Co się stało z częścią ułamkową?
- **EN:** Cast number 7.99 to int and inspect what happened to the decimal fraction.
- **Rozwiązanie:** [`solutions/task_13.py`](solutions/task_13.py)
### Zadanie 14: Defensive safe_int Function
- **Treść:** Napisz funkcję `bezpieczna_int(napis)`, która zwraca `None`, jeśli konwersja się nie uda.
- **EN:** Write function `safe_int(val)` returning parsed int or `None` on failure.
- **Rozwiązanie:** [`solutions/task_14.py`](solutions/task_14.py)
### Zadanie 15: None to String
- **Treść:** Zamień wartość `None` na napis i wyświetl.
- **EN:** Convert `None` to string and display result.
- **Rozwiązanie:** [`solutions/task_15.py`](solutions/task_15.py)

---
[Powrót do Spisu Treści Części 1](../README.pl.md)

# Module 8: PEP 8 Style Guide & Clean Code

[🇬🇧 English](README.md) | [🇵🇱 Polski](README.pl.md)

---

## 🎯 About This Module
Enforce snake_case, 88-character visual boundaries, docstrings, imports ordering, and main guards.

- **Visual Limit:** Max 88 characters per line (PEP 8 / Black standard).
- **Format:** 15 hands-on progressive tasks with full English solutions.

---

## 📝 15 Hands-on Tasks

### Task 01: PEP 8 snake_case Convention
- **Requirement:** Rename `myVariable` to adhere to PEP 8 snake_case: `my_variable`.
- **PL:** Zmień nazwę zmiennej `mojaZmienna` na zgodną z PEP 8 (`snake_case`).
- **Solution:** [`solutions/task_01.py`](solutions/task_01.py)
### Task 02: Four Spaces Indentation
- **Requirement:** Standardize indentation: ensure 4 spaces per indent level instead of tabs.
- **PL:** Popraw wcięcia w kodzie: zastąp tabulatory 4 spacjami.
- **Solution:** [`solutions/task_02.py`](solutions/task_02.py)
### Task 03: Whitespace Around Binary Operators
- **Requirement:** Add single spaces around arithmetic operators: `a + b * c`.
- **PL:** Dodaj spacje wokół operatorów w wyrażeniu: `a+b*c`.
- **Solution:** [`solutions/task_03.py`](solutions/task_03.py)
### Task 04: 88-Character Visual Line Limit
- **Requirement:** Break a long line exceeding limits into clean, readable wrapped lines.
- **PL:** Skróć długą linię dzieląc ją na kilka linii.
- **Solution:** [`solutions/task_04.py`](solutions/task_04.py)
### Task 05: Function snake_case Naming
- **Requirement:** Define function `calculate_rectangle_area` following snake_case convention.
- **PL:** Napisz funkcję `pole_prostokata` używając `snake_case`.
- **Solution:** [`solutions/task_05.py`](solutions/task_05.py)
### Task 06: Docstring Documentation
- **Requirement:** Add PEP 257 docstring explaining function behavior, parameters, and return value.
- **PL:** Dodaj docstring do funkcji opisujący jej działanie.
- **Solution:** [`solutions/task_06.py`](solutions/task_06.py)
### Task 07: Return Values Over Side Effects
- **Requirement:** Return results from functions with `return` instead of printing directly.
- **PL:** W funkcji użyj `return` zamiast `print` – zwróć wynik, a nie wyświetlaj.
- **Solution:** [`solutions/task_07.py`](solutions/task_07.py)
### Task 08: Blank Line Section Separation
- **Requirement:** Use blank lines to separate logical stages: input, processing, and output.
- **PL:** Oddziel w kodzie sekcje: wejście, przetwarzanie, wyjście – użyj pustych linii.
- **Solution:** [`solutions/task_08.py`](solutions/task_08.py)
### Task 09: Descriptive Identifier Names
- **Requirement:** Replace cryptic single-letter variables `a` and `b` with `width` and `height`.
- **PL:** Zmień nazwy zmiennych `a` i `b` na bardziej opisowe (np. `szerokosc`, `wysokosc`).
- **Solution:** [`solutions/task_09.py`](solutions/task_09.py)
### Task 10: Digit Grouping with Underscores
- **Requirement:** Format large integer 1000000 as `1_000_000` for visual clarity.
- **PL:** Użyj podkreśleń do oddzielenia tysięcy w liczbie `1000000`.
- **Solution:** [`solutions/task_10.py`](solutions/task_10.py)
### Task 11: Avoid Ambiguous Single-Letter Identifiers
- **Requirement:** Avoid ambiguous variable names like `l` (lowercase L); use `length` instead.
- **PL:** Unikaj używania `l` (małe L) jako nazwy zmiennej – zmień na `dlugosc`.
- **Solution:** [`solutions/task_11.py`](solutions/task_11.py)
### Task 12: Identity Check Against None
- **Requirement:** Replace `if x == None` with idiomatic `if x is None`.
- **PL:** Zamień `if x == None` na `if x is None`.
- **Solution:** [`solutions/task_12.py`](solutions/task_12.py)
### Task 13: Consistent String Quotes
- **Requirement:** Maintain consistent double quotes `"` across all string literals.
- **PL:** Ujednolic cudzysłowy – użyj `"` dla wszystkich napisów w kodzie.
- **Solution:** [`solutions/task_13.py`](solutions/task_13.py)
### Task 14: Top-Level Imports Ordering
- **Requirement:** Organize imports at the very top of the file: standard library first.
- **PL:** Umieść wszystkie importy na górze pliku.
- **Solution:** [`solutions/task_14.py`](solutions/task_14.py)
### Task 15: Main Entry Point Guard
- **Requirement:** Add `if __name__ == '__main__':` guard and encapsulate workflow in `main()`.
- **PL:** Dodaj konstrukcję `if __name__ == '__main__':` i umieść w niej wywołanie głównej funkcji.
- **Solution:** [`solutions/task_15.py`](solutions/task_15.py)

---
[Back to Part 1 Curriculum](../README.md)

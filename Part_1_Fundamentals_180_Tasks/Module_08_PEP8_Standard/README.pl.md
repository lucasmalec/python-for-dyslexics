# Moduł 8: Standard PEP 8 i Czysty Kod

[🇬🇧 English](README.md) | [🇵🇱 Polski](README.pl.md)

---

## 🎯 O tym module
Egzekwowanie czystego snake_case, limitu 88 znaków, docstringów i bloków if __name__ == '__main__':.

- **Limit wizualny:** Maksymalnie 88 znaków w wierszu (standard PEP 8 / Black).
- **Format:** 15 praktycznych zadań krok po kroku z gotowymi rozwiązaniami w języku angielskim.

---

## 📝 15 Praktycznych Zadań

### Zadanie 01: PEP 8 snake_case Convention
- **Treść:** Zmień nazwę zmiennej `mojaZmienna` na zgodną z PEP 8 (`snake_case`).
- **EN:** Rename `myVariable` to adhere to PEP 8 snake_case: `my_variable`.
- **Rozwiązanie:** [`solutions/task_01.py`](solutions/task_01.py)
### Zadanie 02: Four Spaces Indentation
- **Treść:** Popraw wcięcia w kodzie: zastąp tabulatory 4 spacjami.
- **EN:** Standardize indentation: ensure 4 spaces per indent level instead of tabs.
- **Rozwiązanie:** [`solutions/task_02.py`](solutions/task_02.py)
### Zadanie 03: Whitespace Around Binary Operators
- **Treść:** Dodaj spacje wokół operatorów w wyrażeniu: `a+b*c`.
- **EN:** Add single spaces around arithmetic operators: `a + b * c`.
- **Rozwiązanie:** [`solutions/task_03.py`](solutions/task_03.py)
### Zadanie 04: 88-Character Visual Line Limit
- **Treść:** Skróć długą linię dzieląc ją na kilka linii.
- **EN:** Break a long line exceeding limits into clean, readable wrapped lines.
- **Rozwiązanie:** [`solutions/task_04.py`](solutions/task_04.py)
### Zadanie 05: Function snake_case Naming
- **Treść:** Napisz funkcję `pole_prostokata` używając `snake_case`.
- **EN:** Define function `calculate_rectangle_area` following snake_case convention.
- **Rozwiązanie:** [`solutions/task_05.py`](solutions/task_05.py)
### Zadanie 06: Docstring Documentation
- **Treść:** Dodaj docstring do funkcji opisujący jej działanie.
- **EN:** Add PEP 257 docstring explaining function behavior, parameters, and return value.
- **Rozwiązanie:** [`solutions/task_06.py`](solutions/task_06.py)
### Zadanie 07: Return Values Over Side Effects
- **Treść:** W funkcji użyj `return` zamiast `print` – zwróć wynik, a nie wyświetlaj.
- **EN:** Return results from functions with `return` instead of printing directly.
- **Rozwiązanie:** [`solutions/task_07.py`](solutions/task_07.py)
### Zadanie 08: Blank Line Section Separation
- **Treść:** Oddziel w kodzie sekcje: wejście, przetwarzanie, wyjście – użyj pustych linii.
- **EN:** Use blank lines to separate logical stages: input, processing, and output.
- **Rozwiązanie:** [`solutions/task_08.py`](solutions/task_08.py)
### Zadanie 09: Descriptive Identifier Names
- **Treść:** Zmień nazwy zmiennych `a` i `b` na bardziej opisowe (np. `szerokosc`, `wysokosc`).
- **EN:** Replace cryptic single-letter variables `a` and `b` with `width` and `height`.
- **Rozwiązanie:** [`solutions/task_09.py`](solutions/task_09.py)
### Zadanie 10: Digit Grouping with Underscores
- **Treść:** Użyj podkreśleń do oddzielenia tysięcy w liczbie `1000000`.
- **EN:** Format large integer 1000000 as `1_000_000` for visual clarity.
- **Rozwiązanie:** [`solutions/task_10.py`](solutions/task_10.py)
### Zadanie 11: Avoid Ambiguous Single-Letter Identifiers
- **Treść:** Unikaj używania `l` (małe L) jako nazwy zmiennej – zmień na `dlugosc`.
- **EN:** Avoid ambiguous variable names like `l` (lowercase L); use `length` instead.
- **Rozwiązanie:** [`solutions/task_11.py`](solutions/task_11.py)
### Zadanie 12: Identity Check Against None
- **Treść:** Zamień `if x == None` na `if x is None`.
- **EN:** Replace `if x == None` with idiomatic `if x is None`.
- **Rozwiązanie:** [`solutions/task_12.py`](solutions/task_12.py)
### Zadanie 13: Consistent String Quotes
- **Treść:** Ujednolic cudzysłowy – użyj `"` dla wszystkich napisów w kodzie.
- **EN:** Maintain consistent double quotes `"` across all string literals.
- **Rozwiązanie:** [`solutions/task_13.py`](solutions/task_13.py)
### Zadanie 14: Top-Level Imports Ordering
- **Treść:** Umieść wszystkie importy na górze pliku.
- **EN:** Organize imports at the very top of the file: standard library first.
- **Rozwiązanie:** [`solutions/task_14.py`](solutions/task_14.py)
### Zadanie 15: Main Entry Point Guard
- **Treść:** Dodaj konstrukcję `if __name__ == '__main__':` i umieść w niej wywołanie głównej funkcji.
- **EN:** Add `if __name__ == '__main__':` guard and encapsulate workflow in `main()`.
- **Rozwiązanie:** [`solutions/task_15.py`](solutions/task_15.py)

---
[Powrót do Spisu Treści Części 1](../README.pl.md)

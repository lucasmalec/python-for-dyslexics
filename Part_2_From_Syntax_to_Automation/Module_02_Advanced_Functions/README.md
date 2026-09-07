# Module 2: Advanced Functions (*args, **kwargs, Closures, Decorators)

[🇬🇧 English](README.md) | [🇵🇱 Polski](README.pl.md)

---

## 🎯 About This Module
Deepen procedural mastery: variable positional & keyword arguments, closures, timing decorators, and type annotations.

- **Target Focus:** Real-world sysadmin & cloud automation practices.
- **Visual Standard:** Clean layout, predictable structure, max 88 columns.

---

## 📝 Hands-on Practical Tasks (15 tasks)

### Task 01: Variable Positional Sum
- **Requirement (EN):** Write function `sum_all(*args)` returning the arithmetic sum of any number of passed values.
- **PL:** Napisz funkcję `suma_wszystkich(*args)`, która przyjmuje dowolną liczbę liczb i zwraca ich sumę.
### Task 02: Variable Average Calculation
- **Requirement (EN):** Write function `calculate_average(*args)` returning the arithmetic mean of passed arguments.
- **PL:** Stwórz funkcję `srednia(*args)`, która liczy średnią (uwzględnij dzielenie przez zero).
### Task 03: Default Arguments Configuration
- **Requirement (EN):** Write function `create_backup(source, target='~/backups', compress=True)`.
- **PL:** Napisz funkcję `backup(folder, cel='~/backups', kompresja=True)` z domyślnymi argumentami.
### Task 04: Keyword Arguments Inspection
- **Requirement (EN):** Write function `print_server_info(**kwargs)` printing each configuration key and value.
- **PL:** Napisz funkcję `info_o_serwerze(**kwargs)`, która wypisuje wszystkie przekazane parametry w formacie `klucz: wartosc`.
### Task 05: Combined Signature Handler
- **Requirement (EN):** Write function `dispatch(action, *targets, **options)` demonstrating combined argument handling.
- **PL:** Stwórz funkcję `wykonaj_akcje(akcja, *foldery, **opcje)`, która łączy `*args` i `**kwargs`.
### Task 06: Type Validation Assertion
- **Requirement (EN):** Write function `safe_multiply(a, b)` raising a `TypeError` if parameters are not numeric.
- **PL:** Napisz funkcję `mnoz(a, b)`, która sprawdza typy argumentów i rzuca `TypeError`, jeśli nie są int/float.
### Task 07: Structured Log Writer
- **Requirement (EN):** Write function `write_log(level='INFO', **data)` outputting entries: `[TIMESTAMP] [LEVEL] data`.
- **PL:** Napisz funkcję `loguj(poziom='INFO', **dane)`, która zapisuje do pliku logi w formacie: `[DATA] [POZIOM] dane`.
### Task 08: Arguments Pair to Dictionary
- **Requirement (EN):** Write function `pairs_to_dict(*args)` transforming strings like `('name=Alex', 'age=30')` into a dictionary.
- **PL:** Stwórz funkcję `lista_do_dict(*args)`, która z `('name=Jack', 'age=35')` tworzy słownik.
### Task 09: Type Hints Signature
- **Requirement (EN):** Write a division function with complete type hints: `def safe_divide(a: float, b: float) -> float:`.
- **PL:** Napisz funkcję z adnotacjami typów: `def podziel(a: float, b: float) -> float:`.
### Task 10: Closure Memory Cache
- **Requirement (EN):** Create a closure `memoize()` that retains previous execution results inside an internal cache dictionary.
- **PL:** Stwórz funkcję `cache()`, która zapamiętuje wyniki poprzednich wywołań (użyj słownika wewnątrz funkcji).
### Task 11: Dynamic Config Updater
- **Requirement (EN):** Write function `update_config(**overrides)` that dynamically merges updates into a global `CONFIG` dict.
- **PL:** Napisz funkcję `odswiez_config(**nowe)`, która aktualizuje globalny słownik `CONFIG`.
### Task 12: Higher-Order Multiplier Factory
- **Requirement (EN):** Build higher-order function `make_multiplier(factor)` returning a closure multiplying by `factor`.
- **PL:** Stwórz funkcję wyższego rzędu `razy_n(n)`, która zwraca funkcję mnożącą przez `n`.
### Task 13: Execution Timing Decorator
- **Requirement (EN):** Write timing decorator `@measure_time` measuring and logging execution elapsed duration.
- **PL:** Napisz dekorator `@czas`, który mierzy czas wykonania funkcji.
### Task 14: Functional Mapping with Lambda
- **Requirement (EN):** Use `map()` and lambda to transform a list of strings `['1', '2', '3']` into a list of integers.
- **PL:** Użyj `map()` i lambdy, aby zamienić listę napisów `['1', '2', '3']` na listę intów.
### Task 15: Variadic Dictionary Merger
- **Requirement (EN):** Write function `merge_dicts(*dicts)` combining an arbitrary number of dictionaries with sequential overrides.
- **PL:** Napisz funkcję `merge_dicts(*dicts)`, która łączy dowolną liczbę słowników (nadpisując klucze).

---
[Back to Part 2 Overview](../README.md)

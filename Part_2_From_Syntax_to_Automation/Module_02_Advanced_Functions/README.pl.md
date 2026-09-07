# Moduł 2: Funkcje Zaawansowane (*args, **kwargs, domknięcia, dekoratory)

[🇬🇧 English](README.md) | [🇵🇱 Polski](README.pl.md)

---

## 🎯 O tym module
Pogłębienie wiedzy o funkcjach: zmienna liczba argumentów, domknięcia, dekoratory mierzące czas i adnotacje typów.

- **Cel:** Praktyczna automatyzacja środowisk serwerowych i Cloud DevOps.
- **Standard wizualny:** Przejrzysty układ, przewidywalny rytm, limit 88 znaków.

---

## 📝 Zadania Praktyczne (15 zadań)

### Zadanie 01: Variable Positional Sum
- **Wymaganie (PL):** Napisz funkcję `suma_wszystkich(*args)`, która przyjmuje dowolną liczbę liczb i zwraca ich sumę.
- **EN:** Write function `sum_all(*args)` returning the arithmetic sum of any number of passed values.
### Zadanie 02: Variable Average Calculation
- **Wymaganie (PL):** Stwórz funkcję `srednia(*args)`, która liczy średnią (uwzględnij dzielenie przez zero).
- **EN:** Write function `calculate_average(*args)` returning the arithmetic mean of passed arguments.
### Zadanie 03: Default Arguments Configuration
- **Wymaganie (PL):** Napisz funkcję `backup(folder, cel='~/backups', kompresja=True)` z domyślnymi argumentami.
- **EN:** Write function `create_backup(source, target='~/backups', compress=True)`.
### Zadanie 04: Keyword Arguments Inspection
- **Wymaganie (PL):** Napisz funkcję `info_o_serwerze(**kwargs)`, która wypisuje wszystkie przekazane parametry w formacie `klucz: wartosc`.
- **EN:** Write function `print_server_info(**kwargs)` printing each configuration key and value.
### Zadanie 05: Combined Signature Handler
- **Wymaganie (PL):** Stwórz funkcję `wykonaj_akcje(akcja, *foldery, **opcje)`, która łączy `*args` i `**kwargs`.
- **EN:** Write function `dispatch(action, *targets, **options)` demonstrating combined argument handling.
### Zadanie 06: Type Validation Assertion
- **Wymaganie (PL):** Napisz funkcję `mnoz(a, b)`, która sprawdza typy argumentów i rzuca `TypeError`, jeśli nie są int/float.
- **EN:** Write function `safe_multiply(a, b)` raising a `TypeError` if parameters are not numeric.
### Zadanie 07: Structured Log Writer
- **Wymaganie (PL):** Napisz funkcję `loguj(poziom='INFO', **dane)`, która zapisuje do pliku logi w formacie: `[DATA] [POZIOM] dane`.
- **EN:** Write function `write_log(level='INFO', **data)` outputting entries: `[TIMESTAMP] [LEVEL] data`.
### Zadanie 08: Arguments Pair to Dictionary
- **Wymaganie (PL):** Stwórz funkcję `lista_do_dict(*args)`, która z `('name=Jack', 'age=35')` tworzy słownik.
- **EN:** Write function `pairs_to_dict(*args)` transforming strings like `('name=Alex', 'age=30')` into a dictionary.
### Zadanie 09: Type Hints Signature
- **Wymaganie (PL):** Napisz funkcję z adnotacjami typów: `def podziel(a: float, b: float) -> float:`.
- **EN:** Write a division function with complete type hints: `def safe_divide(a: float, b: float) -> float:`.
### Zadanie 10: Closure Memory Cache
- **Wymaganie (PL):** Stwórz funkcję `cache()`, która zapamiętuje wyniki poprzednich wywołań (użyj słownika wewnątrz funkcji).
- **EN:** Create a closure `memoize()` that retains previous execution results inside an internal cache dictionary.
### Zadanie 11: Dynamic Config Updater
- **Wymaganie (PL):** Napisz funkcję `odswiez_config(**nowe)`, która aktualizuje globalny słownik `CONFIG`.
- **EN:** Write function `update_config(**overrides)` that dynamically merges updates into a global `CONFIG` dict.
### Zadanie 12: Higher-Order Multiplier Factory
- **Wymaganie (PL):** Stwórz funkcję wyższego rzędu `razy_n(n)`, która zwraca funkcję mnożącą przez `n`.
- **EN:** Build higher-order function `make_multiplier(factor)` returning a closure multiplying by `factor`.
### Zadanie 13: Execution Timing Decorator
- **Wymaganie (PL):** Napisz dekorator `@czas`, który mierzy czas wykonania funkcji.
- **EN:** Write timing decorator `@measure_time` measuring and logging execution elapsed duration.
### Zadanie 14: Functional Mapping with Lambda
- **Wymaganie (PL):** Użyj `map()` i lambdy, aby zamienić listę napisów `['1', '2', '3']` na listę intów.
- **EN:** Use `map()` and lambda to transform a list of strings `['1', '2', '3']` into a list of integers.
### Zadanie 15: Variadic Dictionary Merger
- **Wymaganie (PL):** Napisz funkcję `merge_dicts(*dicts)`, która łączy dowolną liczbę słowników (nadpisując klucze).
- **EN:** Write function `merge_dicts(*dicts)` combining an arbitrary number of dictionaries with sequential overrides.

---
[Powrót do Spisu Treści Części 2](../README.pl.md)

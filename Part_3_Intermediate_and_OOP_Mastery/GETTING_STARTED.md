# 🎓 Jak Korzystać z Kursu 6.0

## Struktura Kursu

```
Part_3_Intermediate_and_OOP_Mastery/
├── README.md                          # Przegląd kursu
├── CHECKLIST.md                       # Śledzenie postępów
├── GETTING_STARTED.md                 # Ten plik
├── 1_Funkcje_Zaawansowane.md
├── 2_OOP_Klasy_Obiekty.md
├── 3_Error_Handling.md
├── 4_Collections_Comprehensions.md
├── 5_File_Handling.md
├── 6_Modules_Packages.md
├── 7_Functional_Programming.md
├── 8_Testing_Debugging.md
├── 9_Databases.md
├── 10_Web_API.md
└── 11_Projekty_Praktyczne.md
```

## Plan Nauki

### Tydzień 1-2: Fundamenty Funkcji
**Moduł 1:** Funkcje Zaawansowane (6-8 godzin)
- Naucz się zaawansowanych koncepcji funkcji
- Zrób zadania 1.1, 1.2, 1.3
- Test: Stwórz własny dekorator logujący

### Tydzień 3-4: OOP
**Moduł 2:** OOP — Klasy i Obiekty (8-10 godzin)
- Zrozum klasy, dziedziczenie, polimorfizm
- Zrób wszystkie 3 zadania OOP
- Test: Stwórz dwie powiązane klasy z dziedziczeniem

### Tydzień 5: Error Handling
**Moduł 3:** Error Handling (4-5 godzin)
- Obsługa błędów w praktyce
- Własne wyjątki
- Context managers
- Zrób wszystkie zadania

### Tydzień 6: Collections
**Moduł 4:** Collections & Comprehensions (5-6 godzin)
- List/Dict/Set comprehensions
- Collections module (Counter, defaultdict, namedtuple)
- Zrób wszystkie zadania

### Tydzień 7: Plik & I/O
**Moduł 5:** File Handling (5-6 godzin)
- JSON, CSV, pathlib
- Praca z plikami
- Zrób wszystkie zadania

### Tydzień 8: Organizacja Kodu
**Moduł 6:** Modules & Packages (4-5 godzin)
- Strukturyzacja kodu
- Virtual environments
- Zrób wszystkie zadania

### Tydzień 9: Programowanie Funkcyjne
**Moduł 7:** Functional Programming (5-6 godzin)
- Lambda, map, filter, reduce
- functools (partial, lru_cache)
- Zrób wszystkie zadania

### Tydzień 10: Testowanie
**Moduł 8:** Testing & Debugging (6-7 godzin)
- unittest, pytest
- Fixtures i mocking
- Coverage
- Zrób wszystkie zadania

### Tydzień 11: Bazy Danych
**Moduł 9:** Databases (6-7 godzin)
- SQLite (CRUD operations)
- SQL queries
- Transactions
- Zrób wszystkie zadania

### Tydzień 12: Web & API
**Moduł 10:** Web & API (5-6 godzin)
- requests library
- GET/POST requests
- API wrappers
- Zrób wszystkie zadania

### Tydzień 13-14: Projekty
**Moduł 11:** Projekty Praktyczne (10-12 godzin)
- Wybierz 2-3 projekty
- Zaimplementuj od zera
- Dodaj testy i dokumentację

---

## Jak Pracować z Każdym Modułem

### 1. Przeczytaj Teorię
- Przeczytaj cały plik `.md`
- Zrób notatki
- Zwróć uwagę na przykłady kodu

### 2. Eksperymentuj w REPL/Python
```bash
python3
```

```python
# Testuj przykłady z kursu
# Modyfikuj je, przerwij, sprawdź jak działają
```

### 3. Zrób Zadania
- Zacznij od zadania 1
- Jeśli nie umiesz — wróć do teorii
- Jeśli utknąłeś > 30 min — spójrz na podpowiedź

### 4. Sprawdź Swoją Pracę
```python
# Przetestuj Twoje rozwiązanie
# Czy spełnia wymagania?
# Czy jest readable?
```

---

## Projekty Praktyczne — Jak Zacząć

### Projekt 1: Task Manager (8-10 godzin)
```bash
mkdir task_manager
cd task_manager
python3 main.py
```

**Checklist:**
- [ ] Struktura folderów
- [ ] Klasa TaskManager
- [ ] Menu CLI
- [ ] Zapis do JSON
- [ ] Testy dla TaskManager

### Projekt 2: Web Scraper (10-12 godzin)
```bash
pip install requests beautifulsoup4
mkdir scraper
```

**Checklist:**
- [ ] Scraper class
- [ ] SQLite database
- [ ] Parsowanie HTML
- [ ] Error handling
- [ ] Unit testy

### Projekt 3-5: Twoje Wybory
- Projekt 3: API Wrapper (6-8 godzin)
- Projekt 4: Chat Application (10-12 godzin)
- Projekt 5: Finance Tracker (10-12 godzin)

---

## Best Practices Podczas Nauki

### ✅ Rób:
1. **Pisz kod ręcznie** — nie copy-paste
2. **Eksperymentuj** — zmieniaj wartości, testuj edgecases
3. **Czytaj błędy** — nauczysz się więcej z błędów
4. **Rób notatki** — konspektuję to co naucz się
5. **Testuj** — dla każdego kodu napisz testy
6. **Commituj do git** — każde zadanie to commit

### ❌ Unikaj:
1. Copy-paste kodu bez rozumienia
2. Przeskakiwania modułów
3. Nieuruchamiania kodu
4. Zignorowania błędów
5. Złych nazw zmiennych

---

## Debugowanie & Pomoc

### Gdy nie rozumiesz:
1. **Czytaj error message** — Python mówi co jest źle
2. **Sprawdź type** — `type(variable)`
3. **Dodaj print()** — debuguj krok po kroku
4. **Użyj pdb** — `import pdb; pdb.set_trace()`
5. **Przeczytaj docs** — `help(function_name)`

### Gdy utknąłeś:
1. Weź przerwę (15 min spacer)
2. Przeczytaj teorię ponownie
3. Poszukaj w Google (taki sam error)
4. Spróbuj minimalnego przykładu (REPL)
5. Pisz jasne pytanie — gdzie utknąłeś?

---

## Tempo Nauki

**Szybko:** 4-5 tygodni (intensywnie, 10+ godzin/tydzień)  
**Normalnie:** 8-10 tygodni (5-6 godzin/tydzień)  
**Powoli:** 12-14 tygodni (3-4 godziny/tydzień)

Nie śpiesz się! Lepiej uczyć się solidnie niż szybko.

---

## Znaczniki Trudności

📗 **Łatwe** — podstawy, szybko zrozumiesz  
📙 **Średnie** — wymaga praktyki  
📕 **Trudne** — wróć jeśli nie rozumiesz  
🚀 **Zaawansowane** — dodatkowo dla zainteresowanych

---

## Przesłanie Końcowe

1. **Regularne nauka** > Sporadyczne maratony
2. **Hands-on prakyka** > Tylko czytanie
3. **Debugging** to najważniejsza umiejętność
4. **Projekty** to gdzie naprawdę się uczysz
5. **Nie bój się błędów** — to część procesu!

---

**Powodzenia w nauce! 🎉**

Jeśli masz pytania, wróć do konkretnego modułu lub zrób eksperyment w REPL.


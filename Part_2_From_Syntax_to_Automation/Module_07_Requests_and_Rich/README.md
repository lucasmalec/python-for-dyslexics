# Module 7: External Libraries (requests, rich, dotenv)

[🇬🇧 English](README.md) | [🇵🇱 Polski](README.pl.md)

---

## 🎯 About This Module
Integrate REST APIs via `requests`, build stunning terminal interfaces with `rich`, and manage secrets with `python-dotenv`.

- **Target Focus:** Real-world sysadmin & cloud automation practices.
- **Visual Standard:** Clean layout, predictable structure, max 88 columns.

---

## 📝 Hands-on Practical Tasks (15 tasks)

### Task 01: HTTP GET Request
- **Requirement (EN):** Install `requests` and fetch payload from `https://api.github.com`.
- **PL:** Zainstaluj `requests` i pobierz zawartość strony `https://api.github.com`.
### Task 02: Public API Profile Inspection
- **Requirement (EN):** Query GitHub user API endpoint and print public repository count.
- **PL:** Pobierz informacje o profilu GitHub i wypisz liczbę publicznych repozytoriów.
### Task 03: Iterate Repository Names
- **Requirement (EN):** Fetch repository list from public API and display names sequentially.
- **PL:** Pobierz listę repozytoriów i wypisz ich nazwy.
### Task 04: HTTP Status Code Check
- **Requirement (EN):** Inspect response status code and handle non-200 responses gracefully.
- **PL:** Sprawdź status odpowiedzi – jeśli nie 200, wypisz błąd.
### Task 05: Request Timeout Configuration
- **Requirement (EN):** Configure explicit timeout parameter (e.g. `timeout=5.0`) to avoid hanging sockets.
- **PL:** Dodaj timeout do requesta (np. `timeout=5`).
### Task 06: Rich Styled Console Print
- **Requirement (EN):** Install `rich` and print styled green success status notification.
- **PL:** Zainstaluj `rich` i wypisz kolorowy komunikat: `✅ Sukces!` na zielono.
### Task 07: Rich Formatted Table
- **Requirement (EN):** Render formatted terminal table displaying script names, statuses, and descriptions.
- **PL:** Stwórz tabelę używając `rich` z danymi skryptów serwerowych.
### Task 08: Rich Progress Bar Animation
- **Requirement (EN):** Implement `rich.progress.Progress` bar simulating batch site maintenance.
- **PL:** Dodaj pasek postępu (`Progress`) symulujący przetwarzanie 10 stron.
### Task 09: Rich Boxed Panel Display
- **Requirement (EN):** Render script diagnostic output inside a styled `rich.panel.Panel` border.
- **PL:** Użyj `rich.panel` do wyświetlenia wyniku skryptu w ramce.
### Task 10: Environment Variables via Dotenv
- **Requirement (EN):** Install `python-dotenv` and load environment variables from `.env`.
- **PL:** Zainstaluj `python-dotenv` i wczytaj zmienne środowiskowe z pliku `.env`.
### Task 11: Read Environment Variable
- **Requirement (EN):** Read system variable using `os.getenv('BACKUP_DIR', '/default/path')`.
- **PL:** Użyj `os.getenv()` do pobrania zmiennej.
### Task 12: Configure Retention via .env
- **Requirement (EN):** Define `RETENTION_DAYS=30` in `.env` and consume in Python application.
- **PL:** Stwórz plik `.env` z `RETENCJA_DNI=30` i wczytaj go w programie.
### Task 13: Webhook POST Simulation
- **Requirement (EN):** Dispatch HTTP POST request with JSON payload to simulated monitoring webhook.
- **PL:** Użyj `requests` do wysłania POST (np. do webhooka – symulacja).
### Task 14: Combined Process and Rich Box
- **Requirement (EN):** Execute status command via subprocess and wrap output inside a rich bordered panel.
- **PL:** Połącz `subprocess` i `rich` – uruchom polecenie i wyświetl w kolorowej ramce.
### Task 15: Periodic Uptime Ping Monitor
- **Requirement (EN):** Build periodic site uptime checker executing request every 5 seconds with status indicators.
- **PL:** Stwórz prosty monitoring – co 5 sekund sprawdza status strony i wyświetla ✅ lub ❌.

---
[Back to Part 2 Overview](../README.md)

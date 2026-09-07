# Moduł 7: Biblioteki Zewnętrzne (requests, rich, dotenv)

[🇬🇧 English](README.md) | [🇵🇱 Polski](README.pl.md)

---

## 🎯 O tym module
Integracja REST API przez `requests`, budowa nowoczesnego interfejsu w terminalu z `rich` i obsługa konfiguracji z `python-dotenv`.

- **Cel:** Praktyczna automatyzacja środowisk serwerowych i Cloud DevOps.
- **Standard wizualny:** Przejrzysty układ, przewidywalny rytm, limit 88 znaków.

---

## 📝 Zadania Praktyczne (15 zadań)

### Zadanie 01: HTTP GET Request
- **Wymaganie (PL):** Zainstaluj `requests` i pobierz zawartość strony `https://api.github.com`.
- **EN:** Install `requests` and fetch payload from `https://api.github.com`.
### Zadanie 02: Public API Profile Inspection
- **Wymaganie (PL):** Pobierz informacje o profilu GitHub i wypisz liczbę publicznych repozytoriów.
- **EN:** Query GitHub user API endpoint and print public repository count.
### Zadanie 03: Iterate Repository Names
- **Wymaganie (PL):** Pobierz listę repozytoriów i wypisz ich nazwy.
- **EN:** Fetch repository list from public API and display names sequentially.
### Zadanie 04: HTTP Status Code Check
- **Wymaganie (PL):** Sprawdź status odpowiedzi – jeśli nie 200, wypisz błąd.
- **EN:** Inspect response status code and handle non-200 responses gracefully.
### Zadanie 05: Request Timeout Configuration
- **Wymaganie (PL):** Dodaj timeout do requesta (np. `timeout=5`).
- **EN:** Configure explicit timeout parameter (e.g. `timeout=5.0`) to avoid hanging sockets.
### Zadanie 06: Rich Styled Console Print
- **Wymaganie (PL):** Zainstaluj `rich` i wypisz kolorowy komunikat: `✅ Sukces!` na zielono.
- **EN:** Install `rich` and print styled green success status notification.
### Zadanie 07: Rich Formatted Table
- **Wymaganie (PL):** Stwórz tabelę używając `rich` z danymi skryptów serwerowych.
- **EN:** Render formatted terminal table displaying script names, statuses, and descriptions.
### Zadanie 08: Rich Progress Bar Animation
- **Wymaganie (PL):** Dodaj pasek postępu (`Progress`) symulujący przetwarzanie 10 stron.
- **EN:** Implement `rich.progress.Progress` bar simulating batch site maintenance.
### Zadanie 09: Rich Boxed Panel Display
- **Wymaganie (PL):** Użyj `rich.panel` do wyświetlenia wyniku skryptu w ramce.
- **EN:** Render script diagnostic output inside a styled `rich.panel.Panel` border.
### Zadanie 10: Environment Variables via Dotenv
- **Wymaganie (PL):** Zainstaluj `python-dotenv` i wczytaj zmienne środowiskowe z pliku `.env`.
- **EN:** Install `python-dotenv` and load environment variables from `.env`.
### Zadanie 11: Read Environment Variable
- **Wymaganie (PL):** Użyj `os.getenv()` do pobrania zmiennej.
- **EN:** Read system variable using `os.getenv('BACKUP_DIR', '/default/path')`.
### Zadanie 12: Configure Retention via .env
- **Wymaganie (PL):** Stwórz plik `.env` z `RETENCJA_DNI=30` i wczytaj go w programie.
- **EN:** Define `RETENTION_DAYS=30` in `.env` and consume in Python application.
### Zadanie 13: Webhook POST Simulation
- **Wymaganie (PL):** Użyj `requests` do wysłania POST (np. do webhooka – symulacja).
- **EN:** Dispatch HTTP POST request with JSON payload to simulated monitoring webhook.
### Zadanie 14: Combined Process and Rich Box
- **Wymaganie (PL):** Połącz `subprocess` i `rich` – uruchom polecenie i wyświetl w kolorowej ramce.
- **EN:** Execute status command via subprocess and wrap output inside a rich bordered panel.
### Zadanie 15: Periodic Uptime Ping Monitor
- **Wymaganie (PL):** Stwórz prosty monitoring – co 5 sekund sprawdza status strony i wyświetla ✅ lub ❌.
- **EN:** Build periodic site uptime checker executing request every 5 seconds with status indicators.

---
[Powrót do Spisu Treści Części 2](../README.pl.md)

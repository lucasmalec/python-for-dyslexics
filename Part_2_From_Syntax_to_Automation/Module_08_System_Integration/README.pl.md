# Moduł 8: Zadania Integracyjne – Łączenie Wszystkiego

[🇬🇧 English](README.md) | [🇵🇱 Polski](README.pl.md)

---

## 🎯 O tym module
Synteza pracy z plikami, subprocess, JSON i siecią w kompletne demony automatyzacji dla systemów Linux.

- **Cel:** Praktyczna automatyzacja środowisk serwerowych i Cloud DevOps.
- **Standard wizualny:** Przejrzysty układ, przewidywalny rytm, limit 88 znaków.

---

## 📝 Zadania Praktyczne (10 zadań)

### Zadanie 01: Core Monitor Daemon
- **Wymaganie (PL):** Stwórz program `wsms_monitor.py` koordynujący sprawdzanie stanu systemu.
- **EN:** Build `server_monitor.py` coordinating disk, load, and service checks into a single report.
### Zadanie 02: Fleet Maintenance Inspector
- **Wymaganie (PL):** Rozszerz program o sprawdzanie, czy któraś strona wymaga aktualizacji.
- **EN:** Integrate site update checks into monitoring pipeline.
### Zadanie 03: Automatic Storage Purge Trigger
- **Wymaganie (PL):** Dodaj automatyczne czyszczenie backupów, jeśli dysk jest zapełniony w >80%.
- **EN:** Trigger automatic backup cleaning when partition disk usage exceeds 80%.
### Zadanie 04: Email Notification Dispatcher
- **Wymaganie (PL):** Dodaj wysyłanie raportu na email (symulacja – zapis do pliku `.email`).
- **EN:** Simulate alert notification dispatch to email file queue upon critical error.
### Zadanie 05: Scheduled Monitoring Loop
- **Wymaganie (PL):** Stwórz harmonogram zadań – program działa w pętli, co godzinę robi monitoring.
- **EN:** Implement recurring hourly monitoring execution loop with clean termination handler.
### Zadanie 06: INI Configuration Parser
- **Wymaganie (PL):** Dodaj plik konfiguracyjny `wsms_monitor.ini` (użyj `configparser`).
- **EN:** Read server settings from `monitor.ini` using Python standard `configparser`.
### Zadanie 07: Rotating File Log Handler
- **Wymaganie (PL):** Dodaj logowanie do pliku z rotacją (nowy plik dziennie).
- **EN:** Configure `logging.handlers.TimedRotatingFileHandler` generating daily log archives.
### Zadanie 08: Standard Packaging Setup
- **Wymaganie (PL):** Stwórz instalator Pythona (`pyproject.toml`), który instaluje zależności.
- **EN:** Create `pyproject.toml` declaring project metadata, dependencies, and entry scripts.
### Zadanie 09: Systemd Service Definition
- **Wymaganie (PL):** Przygotuj skrypt do uruchamiania jako usługa systemd (dla Ubuntu).
- **EN:** Craft a Linux systemd service unit file to manage the monitoring script as a background daemon.
### Zadanie 10: Production README Documentation
- **Wymaganie (PL):** Stwórz dokumentację w `README.md` z opisem instalacji i użycia.
- **EN:** Author complete deployment, configuration, and troubleshooting guide in `README.md`.

---
[Powrót do Spisu Treści Części 2](../README.pl.md)

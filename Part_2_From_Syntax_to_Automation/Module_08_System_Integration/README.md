# Module 8: Complete System Integration (Capstones)

[🇬🇧 English](README.md) | [🇵🇱 Polski](README.pl.md)

---

## 🎯 About This Module
Synthesize files, functions, subprocess, JSON, and network calls into enterprise-ready automation daemons.

- **Target Focus:** Real-world sysadmin & cloud automation practices.
- **Visual Standard:** Clean layout, predictable structure, max 88 columns.

---

## 📝 Hands-on Practical Tasks (10 tasks)

### Task 01: Core Monitor Daemon
- **Requirement (EN):** Build `server_monitor.py` coordinating disk, load, and service checks into a single report.
- **PL:** Stwórz program `wsms_monitor.py` koordynujący sprawdzanie stanu systemu.
### Task 02: Fleet Maintenance Inspector
- **Requirement (EN):** Integrate site update checks into monitoring pipeline.
- **PL:** Rozszerz program o sprawdzanie, czy któraś strona wymaga aktualizacji.
### Task 03: Automatic Storage Purge Trigger
- **Requirement (EN):** Trigger automatic backup cleaning when partition disk usage exceeds 80%.
- **PL:** Dodaj automatyczne czyszczenie backupów, jeśli dysk jest zapełniony w >80%.
### Task 04: Email Notification Dispatcher
- **Requirement (EN):** Simulate alert notification dispatch to email file queue upon critical error.
- **PL:** Dodaj wysyłanie raportu na email (symulacja – zapis do pliku `.email`).
### Task 05: Scheduled Monitoring Loop
- **Requirement (EN):** Implement recurring hourly monitoring execution loop with clean termination handler.
- **PL:** Stwórz harmonogram zadań – program działa w pętli, co godzinę robi monitoring.
### Task 06: INI Configuration Parser
- **Requirement (EN):** Read server settings from `monitor.ini` using Python standard `configparser`.
- **PL:** Dodaj plik konfiguracyjny `wsms_monitor.ini` (użyj `configparser`).
### Task 07: Rotating File Log Handler
- **Requirement (EN):** Configure `logging.handlers.TimedRotatingFileHandler` generating daily log archives.
- **PL:** Dodaj logowanie do pliku z rotacją (nowy plik dziennie).
### Task 08: Standard Packaging Setup
- **Requirement (EN):** Create `pyproject.toml` declaring project metadata, dependencies, and entry scripts.
- **PL:** Stwórz instalator Pythona (`pyproject.toml`), który instaluje zależności.
### Task 09: Systemd Service Definition
- **Requirement (EN):** Craft a Linux systemd service unit file to manage the monitoring script as a background daemon.
- **PL:** Przygotuj skrypt do uruchamiania jako usługa systemd (dla Ubuntu).
### Task 10: Production README Documentation
- **Requirement (EN):** Author complete deployment, configuration, and troubleshooting guide in `README.md`.
- **PL:** Stwórz dokumentację w `README.md` z opisem instalacji i użycia.

---
[Back to Part 2 Overview](../README.md)

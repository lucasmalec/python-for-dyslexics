"""
Task 12.08: Log Export Payload Simulator
EN: Simulate exporting user session data into formatted log entries.
PL: Symuluj zapis danych sesji do pliku dziennika.
Standard: PEP 8 (<= 88 characters)
"""

def export_session_log() -> None:
    session_id = "SES-2026-X9"
    user = input("Enter operator username: ").strip()
    status = "SUCCESS"

    payload = (
        f"[LOG ENTRY]\n"
        f"TIMESTAMP:  2026-09-07T12:00:00Z\n"
        f"SESSION_ID: {session_id}\n"
        f"OPERATOR:   {user}\n"
        f"STATUS:     {status}\n"
        f"[EOF]"
    )
    print("--- SIMULATED DISK WRITE ---")
    print(payload)


if __name__ == "__main__":
    export_session_log()

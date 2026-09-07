"""
Task 11.06: REPL Interactive Echo
EN: Prompt for name in REPL style and echo it immediately.
PL: Użyj `input()` w REPL, wpisz swoje imię i wyświetl je.
Standard: PEP 8 (<= 88 characters)
"""

name = input(">>> Enter name: ").strip()
print(f"=> '{name}'")

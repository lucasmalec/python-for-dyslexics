"""
Task 9.15: Direct Prompt Greeting F-String
EN: Combine input prompt and greeting interpolation cleanly.
PL: Połącz f-stringa z `input()` w jednej linii: zapytaj o imię i od razu
    wyświetl powitanie.
Standard: PEP 8 (<= 88 characters)
"""

print(f"Hello, {input('Enter your name: ').strip()}! Welcome to the course.")

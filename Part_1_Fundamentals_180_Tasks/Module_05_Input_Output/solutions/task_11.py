"""
Task 5.11: Birth Year to Age Calculator
EN: Prompt for birth year and calculate current age (reference year = 2026).
PL: Zapytaj o rok urodzenia i oblicz wiek (przyjmij bieżący rok = 2026).
Standard: PEP 8 (<= 88 characters)
"""

CURRENT_YEAR = 2026
birth_year = int(input("Enter your birth year: ").strip())
age = CURRENT_YEAR - birth_year

print(f"In {CURRENT_YEAR}, you are or will be approximately {age} years old.")

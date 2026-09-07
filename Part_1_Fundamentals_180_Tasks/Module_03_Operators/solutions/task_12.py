"""
Task 3.12: Even / Odd Number Check
EN: Ask user for an integer and determine whether it is even using `%`.
PL: Zapytaj użytkownika o liczbę i sprawdź, czy jest parzysta (użyj `%`).
Standard: PEP 8 (<= 88 characters)
"""

number = int(input("Enter an integer: ").strip())
is_even = (number % 2 == 0)

if is_even:
    print(f"{number} is an EVEN number.")
else:
    print(f"{number} is an ODD number.")

"""
Task 5.13: Name and Lucky Number
EN: Prompt for name and favorite number, display: 'Hello [name]! Your number is [number].'.
PL: Zapytaj o imię i liczbę, a następnie wyświetl: 'Cześć [imię]! Twoja liczba to [liczba].'.
Standard: PEP 8 (<= 88 characters)
"""

name = input("Enter your name: ").strip()
number = input("Enter your favorite number: ").strip()

print(f"Hello {name}! Your number is {number}.")

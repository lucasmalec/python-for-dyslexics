"""
Task 7.06: Exception Handling for Input Parsing
EN: Handle `ValueError` when converting age and number inputs.
PL: Dodaj obsługę `ValueError` przy konwersji wieku i liczby.
Standard: PEP 8 (<= 88 characters)
"""

try:
    age = int(input("Enter age: ").strip())
    number = int(input("Enter lucky number: ").strip())
    print(f"Age: {age}, Lucky Number: {number}")
except ValueError:
    print("Invalid input! Both age and lucky number must be integers.")

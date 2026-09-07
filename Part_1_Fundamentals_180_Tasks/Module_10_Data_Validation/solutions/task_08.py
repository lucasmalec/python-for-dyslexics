"""
Task 10.08: Alphabetic Only Name Check
EN: Prompt for text and verify it contains no numeric digits.
PL: Poproś o tekst i sprawdź, czy nie zawiera cyfr.
Standard: PEP 8 (<= 88 characters)
"""

name = input("Enter your name (no digits): ").strip()
contains_digits = any(char.isdigit() for char in name)

if contains_digits:
    print("Error: Names must not contain numerical digits.")
else:
    print(f"Name validated: {name}")

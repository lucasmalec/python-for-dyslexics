"""
Task 10.06: Age Range Assertion
EN: Prompt for age and verify it falls within bounds: 0 to 120.
PL: Poproś o wiek. Jeśli wiek nie mieści się w zakresie 0–120, wyświetl błąd.
Standard: PEP 8 (<= 88 characters)
"""

try:
    age = int(input("Enter age: ").strip())
    if 0 <= age <= 120:
        print(f"Valid age registered: {age}")
    else:
        print(f"Validation Error: Age {age} outside valid range (0-120).")
except ValueError:
    print("Error: Age must be an integer.")

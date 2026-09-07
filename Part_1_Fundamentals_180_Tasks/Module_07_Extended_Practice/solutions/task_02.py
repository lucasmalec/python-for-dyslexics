"""
Task 7.02: Explicit Type Conversions
EN: Add explicit int conversion for age and lucky number using `int()`.
PL: Dodaj konwersję wieku i liczby na `int` (użyj `int()`).
Standard: PEP 8 (<= 88 characters)
"""

raw_age = input("Enter age: ").strip()
raw_num = input("Enter favorite number: ").strip()

age = int(raw_age)
number = int(raw_num)

print(f"Parsed age: {age} ({type(age).__name__})")
print(f"Parsed number: {number} ({type(number).__name__})")

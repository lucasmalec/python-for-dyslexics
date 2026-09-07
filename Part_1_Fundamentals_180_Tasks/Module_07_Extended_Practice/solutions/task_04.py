"""
Task 7.04: Digit String Validation
EN: Add validation: check if age input contains only digits using `.isdigit()`.
PL: Dodaj walidację: jeśli użytkownik poda wiek niebędący liczbą,
    wyświetl komunikat błędu.
Standard: PEP 8 (<= 88 characters)
"""

raw_age = input("Enter your age: ").strip()

if raw_age.isdigit():
    age = int(raw_age)
    print(f"Valid age registered: {age}")
else:
    print(f"Error: '{raw_age}' is not a valid positive whole number.")

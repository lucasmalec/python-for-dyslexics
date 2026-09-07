"""
Task 7.12: Retry Loop on Parsing Errors
EN: Add a `while True` loop to continuously re-prompt until valid int is entered.
PL: Dodaj pętlę, aby program pytał ponownie w przypadku błędu.
Standard: PEP 8 (<= 88 characters)
"""

while True:
    try:
        age = int(input("Enter your age (whole number): ").strip())
        if 0 <= age <= 120:
            print(f"Accepted age: {age}")
            break
        print("Age must be between 0 and 120.")
    except ValueError:
        print("Invalid entry. Please enter digits only.")

"""
Task 7.15: Comprehensive Registration Engine
EN: Integrate validation, loops, math, f-strings, and error handling.
PL: Połącz wszystko: walidacja, f-stringi, konwersje, obliczenia i czytelne komunikaty.
Standard: PEP 8 (<= 88 characters)
"""

def register_user() -> None:
    # 1. Sanitized name
    name = input("Enter your full name: ").strip().title()
    while not name:
        name = input("Name cannot be empty. Enter full name: ").strip().title()

    # 2. Defensive age prompt
    while True:
        try:
            age = int(input("Enter your age: ").strip())
            if 1 <= age <= 120:
                break
            print("Age must be between 1 and 120.")
        except ValueError:
            print("Error: Age must be a valid integer.")

    # 3. Numeric calculations
    future_age = age + 10

    # 4. Formatted summary output
    print("\n" + "=" * 40)
    print(f"REGISTRATION SUCCESSFUL: {name}")
    print(f"Current Age: {age} years")
    print(f"Age in 2036: {future_age} years")
    print("=" * 40)


if __name__ == "__main__":
    register_user()

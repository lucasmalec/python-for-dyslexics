"""
Task 10.15: Multi-field Validation Pipeline
EN: Combine non-empty name check, bounded age (0-120), and lucky number.
PL: Połącz walidację imienia, wieku (0–120) i ulubionej liczby w jednym programie.
Standard: PEP 8 (<= 88 characters)
"""

def collect_user() -> None:
    # 1. Name check
    name = input("Enter name: ").strip()
    if not name or any(char.isdigit() for char in name):
        print("Invalid name: must be non-empty and have no digits.")
        return

    # 2. Age check
    try:
        age = int(input("Enter age (0-120): ").strip())
        if not (0 <= age <= 120):
            print("Invalid age: out of bounds.")
            return
    except ValueError:
        print("Invalid age: must be an integer.")
        return

    # 3. Lucky number
    try:
        lucky = int(input("Enter lucky number: ").strip())
    except ValueError:
        print("Invalid lucky number.")
        return

    print(f"Registration successful for {name} (Age: {age}, Lucky: {lucky}).")


if __name__ == "__main__":
    collect_user()

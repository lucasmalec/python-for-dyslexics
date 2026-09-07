"""
Task 12.04: User Registration System
EN: Collect name, email, age. Validate email contains '@' and age is integer.
PL: Stwórz program rejestracyjny z walidacją emaila i wieku.
Standard: PEP 8 (<= 88 characters)
"""

def register() -> None:
    name = input("Name: ").strip()
    email = input("Email: ").strip()
    age_raw = input("Age: ").strip()

    if not name:
        print("Registration rejected: Name cannot be empty.")
        return
    if "@" not in email or "." not in email:
        print("Registration rejected: Invalid email address.")
        return
    if not age_raw.isdigit() or not (1 <= int(age_raw) <= 120):
        print("Registration rejected: Age must be a positive integer <= 120.")
        return

    print(f"User '{name}' <{email}> registered successfully (Age: {age_raw}).")


if __name__ == "__main__":
    register()

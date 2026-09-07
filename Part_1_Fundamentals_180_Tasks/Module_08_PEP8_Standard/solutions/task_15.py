"""
Task 8.15: Main Entry Point Guard
EN: Add `if __name__ == '__main__':` guard and encapsulate workflow in `main()`.
PL: Dodaj konstrukcję `if __name__ == '__main__':` i umieść w niej wywołanie
    głównej funkcji.
Standard: PEP 8 (<= 88 characters)
"""

def main() -> None:
    """Main program execution workflow."""
    admin_name = "Jack"
    name = input("Enter your name: ").strip().capitalize()

    if name == admin_name:
        print(f"Welcome {name}, we share the same name!")
    else:
        print(f"Welcome, {name}!")


if __name__ == "__main__":
    main()

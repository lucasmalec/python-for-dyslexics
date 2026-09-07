"""
Task 12.10: Interactive Multi-Menu System
EN: Build a CLI menu: 1 - Calculator, 2 - Temp Converter, 3 - Exit.
PL: Program z menu opcji i obsługą wyboru.
Standard: PEP 8 (<= 88 characters)
"""

def show_menu() -> None:
    while True:
        print("\n=== MAIN MENU ===")
        print("1. Calculator preview")
        print("2. Temperature helper")
        print("3. Exit program")
        choice = input("Select option (1-3): ").strip()

        if choice == "1":
            print("Selected option 1: Calculator module ready.")
        elif choice == "2":
            print("Selected option 2: Temp module ready.")
        elif choice == "3":
            print("Exiting. Goodbye!")
            break
        else:
            print("Invalid option. Enter 1, 2, or 3.")


if __name__ == "__main__":
    show_menu()

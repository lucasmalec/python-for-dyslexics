"""
Task 5.01: User Greeting
EN: Ask user for name and display greeting: 'Hello, [name]!'.
PL: Zapytaj użytkownika o imię i przywitaj się komunikatem: 'Cześć, [imię]!'.
Standard: PEP 8 (<= 88 characters)
"""

user_name = input("Enter your name: ").strip()
print(f"Hello, {user_name}!")

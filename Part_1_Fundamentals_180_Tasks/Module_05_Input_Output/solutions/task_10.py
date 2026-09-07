"""
Task 5.10: Uppercase Transformation
EN: Ask user for text input and print it completely in UPPERCASE.
PL: Zapytaj o tekst i wyświetl go wielkimi literami.
Standard: PEP 8 (<= 88 characters)
"""

user_text = input("Enter a sentence: ").strip()
print(f"Uppercase: {user_text.upper()}")

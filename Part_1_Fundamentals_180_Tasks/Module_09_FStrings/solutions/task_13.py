"""
Task 9.13: Dictionary Field Interpolation
EN: Create dict `person = {'name': 'Eve', 'age': 28}` and format its contents.
PL: Utwórz słownik `osoba = {'imie': 'Ewa', 'wiek': 28}` i wyświetl jego zawartość
    za pomocą f-stringa.
Standard: PEP 8 (<= 88 characters)
"""

person = {"name": "Eve", "age": 28}
print(f"Member {person['name']} is {person['age']} years of age.")

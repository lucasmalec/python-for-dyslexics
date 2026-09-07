"""
Task 7.08: Favorite Color Integration
EN: Prompt for favorite color and seamlessly weave it into the user bio sentence.
PL: Dodaj pytanie o ulubiony kolor i wpleć go w zdanie.
Standard: PEP 8 (<= 88 characters)
"""

name = input("Enter name: ").strip()
color = input("Enter favorite color: ").strip().lower()

print(f"{name}'s digital workspace is themed in vibrant {color} accents.")

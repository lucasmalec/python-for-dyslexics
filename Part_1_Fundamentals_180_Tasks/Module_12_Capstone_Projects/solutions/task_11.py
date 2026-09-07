"""
Task 12.11: Dictionary Profile Record
EN: Store user data in a dictionary and display structured contents.
PL: Zapisz dane w słowniku i wyświetl zawartość.
Standard: PEP 8 (<= 88 characters)
"""

user_profile = {
    "name": "Jack Sparrow",
    "age": 35,
    "city": "Tortuga",
    "role": "Captain & Python Explorer",
}

print("Profile Contents:")
for key, val in user_profile.items():
    print(f"  {key.capitalize():<8}: {val}")

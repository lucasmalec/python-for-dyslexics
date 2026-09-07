"""
Task 6.02: IPO Pattern: User Profile Bio
EN: Prompt for name, age, city, process into bio record, and display.
PL: Napisz program, który pobiera imię, wiek i miasto, a następnie wyświetla
    zdanie z tymi danymi.
Standard: PEP 8 (<= 88 characters)
"""

# 1. INPUT
name = input("Enter name: ").strip().capitalize()
age = int(input("Enter age: ").strip())
city = input("Enter city: ").strip().capitalize()

# 2. PROCESS
bio = f"User {name} is {age} years old and resides in {city}."

# 3. OUTPUT
print(bio)

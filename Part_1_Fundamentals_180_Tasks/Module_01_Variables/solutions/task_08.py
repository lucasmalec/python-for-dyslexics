"""
Task 1.08: Dynamic Typing
EN: Create variable `number = 42`, then reassign it to string 'forty-two'.
    Print value and type.
PL: Utwórz zmienną `liczba = 42`, a następnie przypisz do niej napis 'czterdzieści dwa'.
    Wyświetl zmienną.
Standard: PEP 8 (<= 88 characters)
"""

number = 42
print(f"Value: {number} | Type: {type(number).__name__}")

number = "forty-two"
print(f"Value: {number} | Type: {type(number).__name__}")

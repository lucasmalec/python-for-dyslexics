"""
Task 1.13: Self-referential Arithmetic
EN: Create variable `temp = 15`, then overwrite it with `temp * 2 + 5`.
PL: Utwórz zmienną `temp = 15`, a następnie nadpisz ją wynikiem działania `temp * 2 + 5`.
Standard: PEP 8 (<= 88 characters)
"""

temp = 15
print(f"Initial temperature: {temp}")

temp = temp * 2 + 5
print(f"Updated temperature: {temp}")

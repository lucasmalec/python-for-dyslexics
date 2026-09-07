"""
Task 1.04: Overwriting Variables
EN: Overwrite variable `total_sum` with the product of `a` and `b`. Print the new value.
PL: Nadpisz zmienną `suma` wynikiem mnożenia `a` i `b`. Wyświetl nową wartość.
Standard: PEP 8 (<= 88 characters)
"""

a = 7
b = 3

total_sum = a + b
print(f"Initial sum: {total_sum}")

# Reassign variable with multiplication
total_sum = a * b
print(f"Product after reassignment: {total_sum}")

"""
Task 2.15: Implicit Type Coercion
EN: Create `result = 7 + 2.5`. Check which type is produced.
PL: Utwórz zmienną `wynik = 7 + 2.5`. Sprawdź, jakiego typu jest wynik.
Standard: PEP 8 (<= 88 characters)
"""

result = 7 + 2.5
print(f"7 + 2.5 = {result}")
print(f"Type of result: {type(result)} (int promoted to float)")

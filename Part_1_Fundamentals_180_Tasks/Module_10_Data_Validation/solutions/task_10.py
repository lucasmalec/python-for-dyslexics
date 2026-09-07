"""
Task 10.10: LBYL Defensive Division Guard
EN: Check denominator before division (Look Before You Leap pattern).
PL: Poproś o dwie liczby. Sprawdź, czy druga liczba nie jest zerem przed dzieleniem.
Standard: PEP 8 (<= 88 characters)
"""

a = float(input("Enter numerator: ").strip())
b = float(input("Enter denominator: ").strip())

if b == 0.0:
    print("Defensive Guard: Denominator is 0. Operation aborted safely.")
else:
    print(f"Result: {a / b:.4f}")

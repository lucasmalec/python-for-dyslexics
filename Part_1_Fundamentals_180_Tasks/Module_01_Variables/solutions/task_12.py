"""
Task 1.12: Case Sensitivity
EN: Create variables `personAge` and `person_age` with different values.
    Check if Python treats them as distinct.
PL: Utwórz zmienne `wiekOsoby` i `wiek_osoby` z różnymi wartościami.
    Sprawdź, czy Python traktuje je jako różne.
Standard: PEP 8 (<= 88 characters)
"""

personAge = 25
person_age = 42

print(f"personAge:  {personAge}")
print(f"person_age: {person_age}")
print(f"Distinct objects in memory? {personAge != person_age}")

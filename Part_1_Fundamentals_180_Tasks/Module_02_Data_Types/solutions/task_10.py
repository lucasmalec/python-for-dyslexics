"""
Task 2.10: String vs Boolean Trap
EN: Create `is_raining_str = 'False'`. Check its type and verify it is a string.
PL: Utwórz zmienną `czy_deszcz = 'False'`. Sprawdź jej typ – czy to wartość logiczna?
Standard: PEP 8 (<= 88 characters)
"""

is_raining_str = "False"
print(f"Value: {is_raining_str}")
print(f"Type:  {type(is_raining_str)}")
print(f"Notice: bool('False') evaluates to {bool(is_raining_str)} because string is non-empty!")

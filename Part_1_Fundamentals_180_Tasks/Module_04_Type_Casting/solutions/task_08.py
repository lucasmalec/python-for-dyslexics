"""
Task 4.08: String 'True' to Boolean Verification
EN: Convert string 'True' to bool and observe why all non-empty strings are truthy.
PL: Przekonwertuj napis 'True' na `bool` i wyświetl wynik.
Standard: PEP 8 (<= 88 characters)
"""

str_true = "True"
bool_val = bool(str_true)

print(f"bool('{str_true}'): {bool_val}")
print(f"Note: bool('False') is also {bool('False')} because the string length > 0.")

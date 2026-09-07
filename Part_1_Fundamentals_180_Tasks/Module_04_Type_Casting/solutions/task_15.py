"""
Task 4.15: None to String
EN: Convert `None` to string and display result.
PL: Zamień wartość `None` na napis i wyświetl.
Standard: PEP 8 (<= 88 characters)
"""

none_val = None
str_val = str(none_val)

print(f"Converted string: '{str_val}'")
print(f"Type: {type(str_val).__name__} | Length: {len(str_val)}")

"""
Task 8.12: Identity Check Against None
EN: Replace `if x == None` with idiomatic `if x is None`.
PL: Zamień `if x == None` na `if x is None`.
Standard: PEP 8 (<= 88 characters)
"""

user_token = None

# Correct PEP 8 identity comparison:
if user_token is None:
    print("Token is missing (is None check passed).")
else:
    print("Token present.")

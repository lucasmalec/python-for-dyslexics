"""
Task 8.11: Avoid Ambiguous Single-Letter Identifiers
EN: Avoid ambiguous variable names like `l` (lowercase L); use `length` instead.
PL: Unikaj używania `l` (małe L) jako nazwy zmiennej – zmień na `dlugosc`.
Standard: PEP 8 (<= 88 characters)
"""

# Ambiguous: l = 15 (looks like 1 or uppercase I in some fonts)
# Clean:
length = 15
print(f"Length: {length}")

"""
Task 1.07: Renaming Variables
EN: Rename variable `old_var` to `new_var` (assign `old_var` to `new_var`, then del `old_var`).
PL: Zmień nazwę zmiennej `stara` na `nowa` (przypisz wartość z `stara` do `nowa`,
    a `stara` usuń).
Standard: PEP 8 (<= 88 characters)
"""

old_var = "Legacy System Config"

# Step 1: Assign to new variable name
new_var = old_var

# Step 2: Delete the old reference
del old_var

print(f"new_var points to: {new_var}")

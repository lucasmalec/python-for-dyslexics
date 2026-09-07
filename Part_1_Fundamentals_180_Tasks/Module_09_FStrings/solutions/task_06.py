"""
Task 9.06: Column Alignment and Padding
EN: Display aligned table row using width padding.
PL: Wyświetl tabelkę: `| imię: Kacper | wiek: 25 |` z wyrównaniem do 10 znaków.
Standard: PEP 8 (<= 88 characters)
"""

name = "Casper"
age = 25

header = f"| {'Name':<12} | {'Age':<6} |"
row = f"| {name:<12} | {age:<6} |"

print(header)
print("-" * len(header))
print(row)

"""
Task 7.10: Dual Favorite Numbers Math
EN: Prompt for two numbers; display their sum, difference, and product.
PL: Zapytaj o dwie ulubione liczby, wyświetl ich sumę, różnicę i iloczyn.
Standard: PEP 8 (<= 88 characters)
"""

n1 = float(input("Enter first lucky number: ").strip())
n2 = float(input("Enter second lucky number: ").strip())

print(f"{n1} + {n2} = {n1 + n2}")
print(f"{n1} - {n2} = {n1 - n2}")
print(f"{n1} * {n2} = {n1 * n2}")

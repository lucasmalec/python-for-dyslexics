"""
Task 3.01: Four Basic Arithmetic Operations
EN: Ask user for two numbers, then display sum, difference, product, and quotient.
PL: Poproś użytkownika o dwie liczby, a następnie wyświetl ich sumę, różnicę,
    iloczyn i iloraz.
Standard: PEP 8 (<= 88 characters)
"""

num1 = float(input("Enter first number: ").strip())
num2 = float(input("Enter second number: ").strip())

print(f"Sum:        {num1 + num2}")
print(f"Difference: {num1 - num2}")
print(f"Product:    {num1 * num2}")
if num2 != 0:
    print(f"Quotient:   {num1 / num2}")
else:
    print("Quotient:   Undefined (division by zero)")

"""
Task 5.03: Two Numbers Sum
EN: Prompt user for two numbers, parse them, and print their sum.
PL: Poproś o dwie liczby, a następnie wyświetl ich sumę.
Standard: PEP 8 (<= 88 characters)
"""

num1 = float(input("Enter first number: ").strip())
num2 = float(input("Enter second number: ").strip())

total = num1 + num2
print(f"Sum: {total}")

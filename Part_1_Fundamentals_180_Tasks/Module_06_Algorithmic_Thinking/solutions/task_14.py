"""
Task 6.14: IPO Pattern: CLI Calculator
EN: Prompt for two numbers and operator (+, -, *, /), then evaluate.
PL: Napisz prosty kalkulator – pobiera dwie liczby i znak działania
    (+, -, *, /), wyświetla wynik.
Standard: PEP 8 (<= 88 characters)
"""

# 1. INPUT
a = float(input("Enter first number: ").strip())
op = input("Enter operator (+, -, *, /): ").strip()
b = float(input("Enter second number: ").strip())

# 2. PROCESS & 3. OUTPUT
if op == "+":
    print(f"Result: {a + b}")
elif op == "-":
    print(f"Result: {a - b}")
elif op == "*":
    print(f"Result: {a * b}")
elif op == "/":
    if b != 0:
        print(f"Result: {a / b}")
    else:
        print("Error: Cannot divide by zero.")
else:
    print(f"Error: Unknown operator '{op}'")

"""
Task 12.02: Defensive CLI Calculator
EN: Build a CLI calculator with input validation and zero division safeguards.
PL: Stwórz kalkulator z walidacją wejścia i obsługą błędów.
Standard: PEP 8 (<= 88 characters)
"""

def run_calculator() -> None:
    try:
        a = float(input("Enter first number: ").strip())
        op = input("Enter operator (+, -, *, /): ").strip()
        b = float(input("Enter second number: ").strip())

        if op == "+":
            res = a + b
        elif op == "-":
            res = a - b
        elif op == "*":
            res = a * b
        elif op == "/":
            if b == 0:
                print("Error: Cannot divide by zero.")
                return
            res = a / b
        else:
            print(f"Error: Unknown operator '{op}'")
            return

        print(f"Result: {a} {op} {b} = {res:.4f}")
    except ValueError:
        print("Error: Both inputs must be valid numeric values.")


if __name__ == "__main__":
    run_calculator()

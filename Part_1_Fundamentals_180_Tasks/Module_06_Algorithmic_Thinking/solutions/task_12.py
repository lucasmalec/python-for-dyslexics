"""
Task 6.12: IPO Pattern: Reverse Three Numbers
EN: Prompt for three numbers and display them in reverse order.
PL: Napisz program, który pobiera trzy liczby i wyświetla je w odwrotnej kolejności.
Standard: PEP 8 (<= 88 characters)
"""

# 1. INPUT
n1 = input("Enter first value: ").strip()
n2 = input("Enter second value: ").strip()
n3 = input("Enter third value: ").strip()

# 2. PROCESS
reversed_values = [n3, n2, n1]

# 3. OUTPUT
print(f"Reversed sequence: {', '.join(reversed_values)}")

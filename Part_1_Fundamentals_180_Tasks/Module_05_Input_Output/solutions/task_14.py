"""
Task 5.14: Sum Check on Three Inputs
EN: Prompt for three numbers and verify if the first equals the sum of the other two.
PL: Poproś o trzy liczby i sprawdź, czy pierwsza jest sumą dwóch kolejnych.
Standard: PEP 8 (<= 88 characters)
"""

n1 = float(input("Enter first number: ").strip())
n2 = float(input("Enter second number: ").strip())
n3 = float(input("Enter third number: ").strip())

is_sum = (n1 == n2 + n3)
print(f"Does {n1} == {n2} + {n3}? -> {is_sum}")

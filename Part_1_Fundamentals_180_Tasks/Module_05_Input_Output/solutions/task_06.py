"""
Task 5.06: Three Numbers Mean
EN: Prompt user for three numbers and calculate their arithmetic mean.
PL: Poproś o trzy liczby i oblicz ich średnią.
Standard: PEP 8 (<= 88 characters)
"""

a = float(input("Enter number 1: ").strip())
b = float(input("Enter number 2: ").strip())
c = float(input("Enter number 3: ").strip())

mean = (a + b + c) / 3
print(f"Arithmetic mean: {mean:.2f}")

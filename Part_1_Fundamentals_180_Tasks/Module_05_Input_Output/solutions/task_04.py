"""
Task 5.04: Number Squared
EN: Ask for a number and print its square.
PL: Poproś o liczbę i wyświetl jej kwadrat.
Standard: PEP 8 (<= 88 characters)
"""

num = float(input("Enter a number: ").strip())
squared = num ** 2

print(f"{num} squared is: {squared}")

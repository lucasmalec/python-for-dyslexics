"""
Task 5.08: Float Precision Formatter
EN: Prompt for a real number and display it formatted to 2 decimal places.
PL: Poproś o liczbę rzeczywistą i wyświetl ją z dokładnością do 2 miejsc po przecinku.
Standard: PEP 8 (<= 88 characters)
"""

number = float(input("Enter any decimal number: ").strip())
print(f"Formatted with 2 decimals: {number:.2f}")

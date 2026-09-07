"""
Task 5.09: Integer Division and Remainder
EN: Prompt for two integers, then display floor quotient and modulo remainder.
PL: Poproś o dwie liczby całkowite, a następnie wyświetl wynik dzielenia
    całkowitego i resztę.
Standard: PEP 8 (<= 88 characters)
"""

numerator = int(input("Enter numerator: ").strip())
denominator = int(input("Enter denominator: ").strip())

if denominator != 0:
    quotient = numerator // denominator
    remainder = numerator % denominator
    print(f"{numerator} // {denominator} = {quotient} (remainder: {remainder})")
else:
    print("Error: Denominator cannot be zero.")

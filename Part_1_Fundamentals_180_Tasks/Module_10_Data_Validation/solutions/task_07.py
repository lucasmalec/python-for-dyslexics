"""
Task 10.07: Strictly Positive Number Guard
EN: Prompt for positive number (> 0). Reject zero or negative inputs.
PL: Poproś o liczbę dodatnią. Jeśli użytkownik poda 0 lub ujemną, wyświetl komunikat.
Standard: PEP 8 (<= 88 characters)
"""

try:
    val = float(input("Enter positive number: ").strip())
    if val > 0:
        print(f"Accepted positive number: {val}")
    else:
        print(f"Rejected: {val} is not strictly positive (> 0).")
except ValueError:
    print("Error: Please provide a valid number.")

"""
Task 10.14: Divisibility Prime Check
EN: Check if an integer > 3 is divisible by 2 or 3 as a baseline primality check.
PL: Poproś o liczbę i sprawdź podzielność przez 2 i 3.
Standard: PEP 8 (<= 88 characters)
"""

num = int(input("Enter integer > 3: ").strip())

if num % 2 == 0 or num % 3 == 0:
    print(f"{num} is composite (divisible by 2 or 3).")
else:
    print(f"{num} passed initial divisibility checks for primality.")

"""
Task 6.07: IPO Pattern: Year to Day Counter
EN: Calculate number of days in given non-leap years (365 days/year).
PL: Napisz program obliczający liczbę dni w podanej liczbie lat (bez lat przestępnych).
Standard: PEP 8 (<= 88 characters)
"""

# 1. INPUT
years = int(input("Enter number of years: ").strip())

# 2. PROCESS
total_days = years * 365

# 3. OUTPUT
print(f"{years} standard years contain {total_days:,} days.")

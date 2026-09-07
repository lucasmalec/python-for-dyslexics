"""
Task 6.06: IPO Pattern: Time Conversion
EN: Convert hours into minutes and seconds.
PL: Napisz program zamieniający podaną liczbę godzin na minuty i sekundy.
Standard: PEP 8 (<= 88 characters)
"""

# 1. INPUT
hours = float(input("Enter duration in hours: ").strip())

# 2. PROCESS
minutes = hours * 60
seconds = minutes * 60

# 3. OUTPUT
print(f"{hours} hour(s) equals {minutes:g} minutes and {seconds:g} seconds.")

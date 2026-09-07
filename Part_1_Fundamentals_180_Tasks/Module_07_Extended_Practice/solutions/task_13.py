"""
Task 7.13: Date of Birth Age Resolution
EN: Prompt for birth day, month, year, and compute approximate age in 2026.
PL: Zapytaj o datę urodzenia (dzień, miesiąc, rok) i oblicz dokładny wiek.
Standard: PEP 8 (<= 88 characters)
"""

CURRENT_YEAR = 2026

day = int(input("Birth day (1-31): ").strip())
month = int(input("Birth month (1-12): ").strip())
year = int(input("Birth year (e.g. 1995): ").strip())

approx_age = CURRENT_YEAR - year
print(f"Born on {day:02d}-{month:02d}-{year:04d} -> Age in {CURRENT_YEAR}: ~{approx_age}")

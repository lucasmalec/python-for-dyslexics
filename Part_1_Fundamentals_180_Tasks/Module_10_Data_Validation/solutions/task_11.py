"""
Task 10.11: Year Range Validation
EN: Prompt for a year and verify it falls within range 1900 to 2026.
PL: Poproś o rok. Sprawdź, czy rok jest z zakresu 1900–2026.
Standard: PEP 8 (<= 88 characters)
"""

try:
    year = int(input("Enter year (1900-2026): ").strip())
    if 1900 <= year <= 2026:
        print(f"Valid year: {year}")
    else:
        print(f"Year {year} out of supported range (1900-2026).")
except ValueError:
    print("Invalid year format.")

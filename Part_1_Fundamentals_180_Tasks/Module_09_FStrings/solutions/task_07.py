"""
Task 9.07: Leading Zeros Date Formatting
EN: Display date in DD-MM-YYYY format with zero padding (e.g. 05-03-2026).
PL: Wyświetl datę w formacie `DD-MM-RRRR` z zerami wiodącymi (np. `05-03-2026`).
Standard: PEP 8 (<= 88 characters)
"""

# Approach 1: Formatted numeric integers (Preferred)
day = 5
month = 3
year = 2026

date_str = f"{day:02d}-{month:02d}-{year:04d}"
print(f"Formatted Date: {date_str}")

# Approach 2: String zfill
d_str = str(day).zfill(2)
m_str = str(month).zfill(2)
y_str = str(year).zfill(4)
print(f"Zfill Date:     {d_str}-{m_str}-{y_str}")

"""
Task 6.08: IPO Pattern: Currency Converter
EN: Convert amount from PLN to EUR using exchange rate 1 EUR = 4.30 PLN.
PL: Napisz program przeliczający kwotę w PLN na EUR (kurs: 1 EUR = 4.30 PLN).
Standard: PEP 8 (<= 88 characters)
"""

EXCHANGE_RATE_PLN_PER_EUR = 4.30

# 1. INPUT
amount_pln = float(input("Enter amount in PLN: ").strip())

# 2. PROCESS
amount_eur = amount_pln / EXCHANGE_RATE_PLN_PER_EUR

# 3. OUTPUT
print(f"{amount_pln:.2f} PLN = {amount_eur:.2f} EUR (rate: 4.30)")

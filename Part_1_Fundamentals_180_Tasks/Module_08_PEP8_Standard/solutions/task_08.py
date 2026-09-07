"""
Task 8.08: Blank Line Section Separation
EN: Use blank lines to separate logical stages: input, processing, and output.
PL: Oddziel w kodzie sekcje: wejście, przetwarzanie, wyjście – użyj pustych linii.
Standard: PEP 8 (<= 88 characters)
"""

# 1. Input stage
base_price = 120.0
tax_percent = 20.0

# 2. Processing stage
tax_rate = tax_percent / 100.0
total_price = base_price * (1.0 + tax_rate)

# 3. Output stage
print(f"Total: £{total_price:.2f}")

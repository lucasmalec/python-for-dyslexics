"""
Task 6.11: IPO Pattern: Discount Calculator
EN: Calculate final price after applying a 20% discount to an initial price.
PL: Napisz program obliczający cenę po rabacie 20% od podanej ceny.
Standard: PEP 8 (<= 88 characters)
"""

DISCOUNT_RATE = 0.20

# 1. INPUT
original_price = float(input("Enter original price (£): ").strip())

# 2. PROCESS
discount_amount = original_price * DISCOUNT_RATE
final_price = original_price - discount_amount

# 3. OUTPUT
print(f"Original price: £{original_price:.2f}")
print(f"20% discount:   -£{discount_amount:.2f}")
print(f"Final price:    £{final_price:.2f}")

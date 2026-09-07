"""
Task 4.10: Chained Float and Int Conversion
EN: Create `price_str = '49.99'`. Convert first to float, then to int.
PL: Utwórz zmienną `cena = '49.99'`. Zamień ją najpierw na `float`, a potem na `int`.
Standard: PEP 8 (<= 88 characters)
"""

price_str = "49.99"
price_float = float(price_str)
price_int = int(price_float)

print(f"Raw string:    '{price_str}'")
print(f"As float:      {price_float}")
print(f"Truncated int: {price_int}")

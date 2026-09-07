"""
Task 5.15: Product Invoice Summary
EN: Prompt for product name and net price; compute gross price using 23% VAT.
PL: Zapytaj o nazwę produktu i cenę netto, wyświetl cenę brutto (23% VAT).
Standard: PEP 8 (<= 88 characters)
"""

product = input("Enter product name: ").strip()
net_price = float(input("Enter net price (£): ").strip())

vat_rate = 0.23
gross_price = net_price * (1 + vat_rate)

print(f"Product:     {product}")
print(f"Net Price:   £{net_price:.2f}")
print(f"VAT (23%):   £{(net_price * vat_rate):.2f}")
print(f"Gross Price: £{gross_price:.2f}")

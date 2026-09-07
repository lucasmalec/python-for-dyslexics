"""
Task 1.06: Gross Price and VAT Calculation
EN: Create variables `net_price = 100` and `vat_rate = 0.23`. Calculate `gross_price`
    and display. Includes defensive negative VAT check and interactive inputs.
PL: Utwórz zmienną `cena_netto = 100` i `vat = 0.23`. Oblicz `cena_brutto` i wyświetl.
    Zawiera interaktywność i ochronę przed ujemnym VAT.
Standard: PEP 8 (<= 88 characters)
"""

# Defensive input with fallback
try:
    net_input = input("Enter net price (£) [default 100.0]: ").strip()
    net_price = float(net_input) if net_input else 100.0

    vat_input = input("Enter VAT percentage (%) [default 23]: ").strip()
    vat_percent = float(vat_input) if vat_input else 23.0
except ValueError:
    print("Invalid numeric input. Falling back to default values.")
    net_price = 100.0
    vat_percent = 23.0

# Convert percentage to decimal rate
vat_rate = vat_percent / 100.0

# Guard against negative VAT rate
if vat_rate < 0:
    vat_rate = 0.0
    print("Notice: Negative VAT was reset to 0.0%.")

gross_price = net_price + (net_price * vat_rate)

print(f"Net Price: £{net_price:.2f}")
print(f"VAT Rate:  {vat_percent:.1f}%")
print(f"Gross Price: £{gross_price:.2f}")

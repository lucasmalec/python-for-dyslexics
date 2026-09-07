"""
Task 8.09: Descriptive Identifier Names
EN: Replace cryptic variables `a` and `b` with descriptive `width` and `height`.
PL: Zmień nazwy zmiennych `a` i `b` na bardziej opisowe.
Standard: PEP 8 (<= 88 characters)
"""

# Avoid: a = 12; b = 8; c = a * b
# Descriptive PEP 8 naming:
box_width_cm = 12.0
box_height_cm = 8.0
cross_section_area = box_width_cm * box_height_cm

print(f"Cross section: {cross_section_area:.1f} cm^2")

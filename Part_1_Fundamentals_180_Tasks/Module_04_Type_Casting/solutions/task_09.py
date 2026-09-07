"""
Task 4.09: Whitespace Stripping Before Conversion
EN: Convert string '   99   ' to int using `strip()`.
PL: Zamień napis '   99   ' na `int` (użyj `strip()` przed konwersją).
Standard: PEP 8 (<= 88 characters)
"""

padded_text = "   99   "
clean_number = int(padded_text.strip())

print(f"Original: '{padded_text}' -> Parsed integer: {clean_number}")

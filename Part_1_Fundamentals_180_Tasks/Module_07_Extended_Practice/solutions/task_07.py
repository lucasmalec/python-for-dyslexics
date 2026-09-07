"""
Task 7.07: String Sanitization with strip
EN: Apply `.strip()` on inputs to eliminate accidental whitespace.
PL: Użyj `strip()` przed konwersją, aby usunąć przypadkowe spacje.
Standard: PEP 8 (<= 88 characters)
"""

raw_input_data = "   42   "
sanitized = raw_input_data.strip()
value = int(sanitized)

print(f"Raw input:       '{raw_input_data}'")
print(f"Sanitized input: '{sanitized}' -> Integer: {value}")

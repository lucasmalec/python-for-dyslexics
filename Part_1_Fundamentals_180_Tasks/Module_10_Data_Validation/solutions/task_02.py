"""
Task 10.02: Whitespace Sanitization Before Parse
EN: Prompt for number and use `.strip()` prior to conversion.
PL: Poproś o liczbę, użyj `strip()` przed konwersją, aby usunąć spacje.
Standard: PEP 8 (<= 88 characters)
"""

user_input = input("Enter a number with optional spaces: ")
clean_text = user_input.strip()

try:
    value = float(clean_text)
    print(f"Sanitized: '{clean_text}' -> Parsed: {value}")
except ValueError:
    print(f"Failed to parse '{clean_text}' as float.")

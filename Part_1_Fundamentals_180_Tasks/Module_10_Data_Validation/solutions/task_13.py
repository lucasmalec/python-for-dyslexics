"""
Task 10.13: Allowed Options Whitelist
EN: Prompt for color from whitelist: ['red', 'green', 'blue'].
PL: Poproś o kolor z listy: czerwony, zielony, niebieski.
Standard: PEP 8 (<= 88 characters)
"""

ALLOWED = ["red", "green", "blue"]
choice = input(f"Choose a color ({', '.join(ALLOWED)}): ").strip().lower()

if choice in ALLOWED:
    print(f"Valid color selection: {choice}")
else:
    print(f"Error: '{choice}' is not one of the allowed options.")

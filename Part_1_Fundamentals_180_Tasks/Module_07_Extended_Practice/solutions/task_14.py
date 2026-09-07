"""
Task 7.14: Color to HEX Code Lookup
EN: Ask for favorite color and look up its HEX color code using a dictionary.
PL: Zapytaj o ulubiony kolor i wyświetl jego kod HEX (użyj słownika).
Standard: PEP 8 (<= 88 characters)
"""

HEX_PALETTE = {
    "red": "#FF0000",
    "green": "#00FF00",
    "blue": "#0000FF",
    "yellow": "#FFFF00",
    "purple": "#800080",
    "cyan": "#00FFFF",
}

chosen_color = input("Choose a color (red, green, blue, yellow, purple): ").strip().lower()
hex_code = HEX_PALETTE.get(chosen_color, "#UNKNOWN")

print(f"Color: {chosen_color} -> HEX Code: {hex_code}")

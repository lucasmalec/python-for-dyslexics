"""
Task 5.07: Location Formatter
EN: Ask user for city and country, then print: 'You live in [city], [country].'.
PL: Zapytaj o miasto i kraj, a następnie wyświetl: 'Mieszkasz w [miasto], [kraj].'.
Standard: PEP 8 (<= 88 characters)
"""

city = input("Enter your city: ").strip()
country = input("Enter your country: ").strip()

print(f"You live in {city}, {country}.")

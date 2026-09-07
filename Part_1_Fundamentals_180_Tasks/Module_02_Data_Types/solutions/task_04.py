"""
Task 2.04: String Concatenation Fix
EN: Combine string 'I am ' with number 30 and ' years old' using string conversion.
PL: Połącz napis 'Mam ' z liczbą 30 i napisem ' lat' – napraw błąd używając
    konwersji na tekst.
Standard: PEP 8 (<= 88 characters)
"""

age = 30
# Correct: convert integer to string explicitly
message = "I am " + str(age) + " years old."

print(message)

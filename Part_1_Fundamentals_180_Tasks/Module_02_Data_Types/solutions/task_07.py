"""
Task 2.07: Float Truncation
EN: Create `temperature = 36.6`. Cast it to int and print. Observe truncation behavior.
PL: Utwórz zmienną `temperatura = 36.6`. Przekonwertuj ją na `int` i wyświetl.
    Co się stało?
Standard: PEP 8 (<= 88 characters)
"""

temperature = 36.6
truncated_temp = int(temperature)

print(f"Original float: {temperature}")
print(f"Truncated int:  {truncated_temp} (decimal portion discarded, not rounded)")

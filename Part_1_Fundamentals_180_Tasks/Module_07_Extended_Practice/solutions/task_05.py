"""
Task 7.05: Decimal Precision Display
EN: Calculate future age and format it with two decimal places (e.g. 30.00).
PL: Oblicz wiek za 10 lat i wyświetl go z dwoma miejscami po przecinku (np. 30.00).
Standard: PEP 8 (<= 88 characters)
"""

age = 25.5
future_age = age + 10.0

print(f"Future age formatted to 2 decimals: {future_age:.2f}")

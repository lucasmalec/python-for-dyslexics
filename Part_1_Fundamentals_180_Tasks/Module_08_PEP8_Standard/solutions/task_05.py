"""
Task 8.05: Function snake_case Naming
EN: Define function `calculate_rectangle_area` following snake_case convention.
PL: Napisz funkcję `pole_prostokata` używając `snake_case`.
Standard: PEP 8 (<= 88 characters)
"""

def calculate_rectangle_area(width: float, height: float) -> float:
    return width * height


print(f"Area: {calculate_rectangle_area(6.0, 4.0)}")

"""
Task 12.03: Circle Geometry Engine
EN: Calculate circle area and circumference formatted to 2 decimal places.
PL: Napisz program obliczający pole i obwód koła z f-stringami (2 miejsca).
Standard: PEP 8 (<= 88 characters)
"""

import math

def calculate_circle() -> None:
    try:
        r = float(input("Enter circle radius: ").strip())
        if r < 0:
            print("Radius cannot be negative.")
            return

        area = math.pi * (r ** 2)
        circumference = 2 * math.pi * r

        print(f"Radius:        {r:.2f}")
        print(f"Area:          {area:.2f}")
        print(f"Circumference: {circumference:.2f}")
    except ValueError:
        print("Invalid radius.")


if __name__ == "__main__":
    calculate_circle()

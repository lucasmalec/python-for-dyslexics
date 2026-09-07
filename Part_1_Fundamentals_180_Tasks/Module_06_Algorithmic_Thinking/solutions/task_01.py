"""
Task 6.01: IPO Pattern: Rectangle Area
EN: Calculate rectangle area dividing code explicitly into: Input, Process, Output.
PL: Napisz program obliczający pole prostokąta. Podziel kod na trzy sekcje:
    wejście, przetwarzanie, wyjście.
Standard: PEP 8 (<= 88 characters)
"""

# 1. INPUT
width = float(input("Enter rectangle width: ").strip())
height = float(input("Enter rectangle height: ").strip())

# 2. PROCESS
area = width * height

# 3. OUTPUT
print(f"Calculated rectangle area: {area:.2f}")

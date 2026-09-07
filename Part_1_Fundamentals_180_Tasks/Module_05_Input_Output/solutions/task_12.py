"""
Task 5.12: Rectangle Geometry
EN: Prompt for rectangle length and width, then compute and print area and perimeter.
PL: Poproś o długość i szerokość prostokąta, wyświetl pole i obwód.
Standard: PEP 8 (<= 88 characters)
"""

length = float(input("Enter length: ").strip())
width = float(input("Enter width: ").strip())

area = length * width
perimeter = 2 * (length + width)

print(f"Area:      {area:.2f}")
print(f"Perimeter: {perimeter:.2f}")

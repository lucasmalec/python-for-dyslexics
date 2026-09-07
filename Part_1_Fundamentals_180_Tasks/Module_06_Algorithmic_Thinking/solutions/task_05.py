"""
Task 6.05: IPO Pattern: Academic Grade Average
EN: Prompt for three grades (1 to 6) and compute arithmetic average.
PL: Napisz program, który pobiera trzy oceny (1–6) i oblicza średnią arytmetyczną.
Standard: PEP 8 (<= 88 characters)
"""

# 1. INPUT
g1 = float(input("Enter grade 1: ").strip())
g2 = float(input("Enter grade 2: ").strip())
g3 = float(input("Enter grade 3: ").strip())

# 2. PROCESS
average = (g1 + g2 + g3) / 3

# 3. OUTPUT
print(f"Grade average: {average:.2f}")

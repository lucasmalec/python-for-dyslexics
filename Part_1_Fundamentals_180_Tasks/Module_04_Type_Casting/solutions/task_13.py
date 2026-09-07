"""
Task 4.13: Float to Int Truncation Analysis
EN: Cast number 7.99 to int and inspect what happened to the decimal fraction.
PL: Zamień liczbę 7.99 na `int` i wyświetl. Co się stało z częścią ułamkową?
Standard: PEP 8 (<= 88 characters)
"""

original = 7.99
truncated = int(original)

print(f"Float value:    {original}")
print(f"Integer cast:   {truncated}")
print("Notice: int() strictly truncates toward zero; it does not round.")

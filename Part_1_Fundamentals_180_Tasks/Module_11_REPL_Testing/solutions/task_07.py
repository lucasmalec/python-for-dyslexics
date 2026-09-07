"""
Task 11.07: Padded Integer Parse
EN: Test how `int('   50   ')` handles leading and trailing spaces.
PL: Sprawdź działanie `int('   50   ')`.
Standard: PEP 8 (<= 88 characters)
"""

parsed = int("   50   ")
print(f"int('   50   ') = {parsed} (Built-in int() ignores surrounding spaces)")

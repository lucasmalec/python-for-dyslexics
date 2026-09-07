"""
Task 2.09: Chained Conversions
EN: Create `num_str = '456'`. Convert first to int, then to float.
PL: Utwórz zmienną `napis = '456'`. Przekonwertuj ją najpierw na `int`, a potem na `float`.
Standard: PEP 8 (<= 88 characters)
"""

num_str = "456"
as_int = int(num_str)
as_float = float(as_int)

print(f"String: {num_str} ({type(num_str).__name__})")
print(f"Int:    {as_int} ({type(as_int).__name__})")
print(f"Float:  {as_float} ({type(as_float).__name__})")

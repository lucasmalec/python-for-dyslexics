"""
Task 3.05: Augmented Assignment Operators
EN: Create `x = 10`. Apply `+=`, `-=`, `*=`, `/=` and display `x` after each step.
PL: Utwórz zmienną `x = 10`. Użyj operatorów `+=`, `-=`, `*=`, `/=` i po każdej
    operacji wyświetl `x`.
Standard: PEP 8 (<= 88 characters)
"""

x = 10
print(f"Initial: x = {x}")

x += 5
print(f"After x += 5:  {x}")

x -= 3
print(f"After x -= 3:  {x}")

x *= 2
print(f"After x *= 2:  {x}")

x /= 4
print(f"After x /= 4:  {x}")

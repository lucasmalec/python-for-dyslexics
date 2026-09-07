"""
Task 11.05: Function Rapid Testing
EN: Define `square(n) -> n * n` and test it with 7.
PL: Zdefiniuj funkcję `kwadrat(n)` zwracającą `n * n` i przetestuj dla 7.
Standard: PEP 8 (<= 88 characters)
"""

def square(n: int | float) -> int | float:
    return n * n


test_val = 7
print(f"square({test_val}) = {square(test_val)}")

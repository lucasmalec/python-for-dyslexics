"""
Task 10.05: Looping Integer Validator
EN: Write function `get_integer(prompt)` that loops until valid integer is entered.
PL: Napisz funkcję `pobierz_int()`, która pyta aż do podania poprawnej
    liczby całkowitej.
Standard: PEP 8 (<= 88 characters)
"""

def get_integer(prompt: str = "Enter integer: ") -> int:
    while True:
        try:
            return int(input(prompt).strip())
        except ValueError:
            print("Invalid input. Please try again.")


result = get_integer("Please enter port number: ")
print(f"Configured port: {result}")

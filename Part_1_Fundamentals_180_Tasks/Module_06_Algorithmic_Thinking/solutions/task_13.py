"""
Task 6.13: IPO Pattern: Text Multiplier
EN: Prompt for text and integer n, then repeat the text n times.
PL: Napisz program, który pobiera tekst i liczbę `n`, a następnie wyświetla tekst `n` razy.
Standard: PEP 8 (<= 88 characters)
"""

# 1. INPUT
user_text = input("Enter string to repeat: ").strip()
multiplier = int(input("Enter repetition count: ").strip())

# 2. PROCESS
repeated = (user_text + " ") * multiplier

# 3. OUTPUT
print(f"Result: {repeated.strip()}")

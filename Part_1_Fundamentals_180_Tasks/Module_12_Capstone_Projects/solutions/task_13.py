"""
Task 12.13: Continuous Loop Until Exit
EN: Loop continuously requesting numbers and squaring them until 'exit'.
PL: Pętla pytająca o liczbę i licząca kwadrat aż do wpisania 'exit'.
Standard: PEP 8 (<= 88 characters)
"""

def square_loop() -> None:
    print("Enter numbers to square (type 'exit' to terminate):")
    while True:
        entry = input("Number > ").strip()
        if entry.lower() == "exit":
            print("Terminating loop. Bye!")
            break
        try:
            num = float(entry)
            print(f"{num} squared = {num ** 2}")
        except ValueError:
            print("Invalid input. Enter a number or 'exit'.")


if __name__ == "__main__":
    square_loop()

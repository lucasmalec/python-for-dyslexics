"""
Task 12.07: Number Guessing Game
EN: Secret number guessing game with higher/lower hints.
PL: Zgadywanie liczby 1–10 z podpowiedziami za dużo/za mało.
Standard: PEP 8 (<= 88 characters)
"""

def guess_game() -> None:
    secret = 7  # Pre-set or random.randint(1, 10)
    attempts = 0

    while True:
        try:
            guess = int(input("Guess a number between 1 and 10: ").strip())
            attempts += 1
            if guess == secret:
                print(f"Congratulations! You found {secret} in {attempts} attempt(s)!")
                break
            elif guess < secret:
                print("Too low! Try higher.")
            else:
                print("Too high! Try lower.")
        except ValueError:
            print("Please enter a valid integer.")


if __name__ == "__main__":
    guess_game()

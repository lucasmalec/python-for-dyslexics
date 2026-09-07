"""
Task 12.06: Interactive 3-Question Quiz
EN: Build a 3-question quiz with score tracking and summary feedback.
PL: Stwórz prosty quiz: 3 pytania z punktacją.
Standard: PEP 8 (<= 88 characters)
"""

def run_quiz() -> None:
    score = 0
    questions = [
        ("What is the capital of Poland? ", "warsaw"),
        ("What is 2 + 2 * 2? ", "6"),
        ("Is Python interpreted? (yes/no) ", "yes"),
    ]

    for q, expected in questions:
        answer = input(q).strip().lower()
        if answer == expected:
            print("Correct! +1 point")
            score += 1
        else:
            print(f"Wrong. Expected: {expected}")

    print(f"Final Score: {score}/{len(questions)}")


if __name__ == "__main__":
    run_quiz()

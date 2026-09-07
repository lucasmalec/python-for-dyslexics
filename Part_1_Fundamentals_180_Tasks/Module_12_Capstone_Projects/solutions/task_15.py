"""
Task 12.15: Production Grade Student Assessment Engine
EN: Complete production application combining PEP 8, validation, f-strings.
PL: Kompletny program zgodny z PEP 8, z f-stringami, walidacją i architekturą.
Standard: PEP 8 (<= 88 characters)
"""

from typing import Dict, List


def get_student_record() -> Dict[str, object] | None:
    name = input("Enter student name: ").strip().title()
    if not name:
        print("Error: Student name cannot be empty.")
        return None

    grades: List[float] = []
    print("Enter 3 examination scores (0.0 - 100.0):")
    for i in range(1, 4):
        while True:
            try:
                score = float(input(f"  Score {i}: ").strip())
                if 0.0 <= score <= 100.0:
                    grades.append(score)
                    break
                print("Score must be between 0.0 and 100.0.")
            except ValueError:
                print("Invalid format. Please enter a valid number.")

    average = sum(grades) / len(grades)
    letter = "A" if average >= 90 else "B" if average >= 75 else "C"

    return {
        "name": name,
        "grades": grades,
        "average": average,
        "grade_letter": letter,
    }


def main() -> None:
    print("=== STUDENT ASSESSMENT PORTAL ===")
    record = get_student_record()
    if record:
        print("\n" + "=" * 40)
        print(f"OFFICIAL TRANSCRIPT: {record['name']}")
        print(f"Scores Recorded: {record['grades']}")
        print(f"Grade Average:   {record['average']:.2f}%")
        print(f"Final Standing:  Grade {record['grade_letter']}")
        print("=" * 40)


if __name__ == "__main__":
    main()

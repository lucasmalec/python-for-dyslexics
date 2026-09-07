"""
Task 12.12: Student Grade Report Generator
EN: Prompt for name and 3 grades, calculate average, and print report card.
PL: Generuj raport ucznia: imię, 3 oceny, średnia i wynik końcowy.
Standard: PEP 8 (<= 88 characters)
"""

def generate_report() -> None:
    name = input("Student name: ").strip().title()
    g1 = float(input("Grade 1: ").strip())
    g2 = float(input("Grade 2: ").strip())
    g3 = float(input("Grade 3: ").strip())

    avg = (g1 + g2 + g3) / 3
    status = "HONORS" if avg >= 4.5 else "PASS"

    print("\n" + "=" * 32)
    print(f"STUDENT REPORT: {name}")
    print(f"Average: {avg:.2f} | Status: {status}")
    print("=" * 32)


if __name__ == "__main__":
    generate_report()

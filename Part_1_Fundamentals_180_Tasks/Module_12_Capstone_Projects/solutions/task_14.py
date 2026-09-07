"""
Task 12.14: Structured Three-Function Architecture
EN: Modularize program: fetch_data(), process_data(), display_result().
PL: Podziel program na funkcje: wejście, przetwarzanie, wyjście.
Standard: PEP 8 (<= 88 characters)
"""

def fetch_data() -> float:
    return float(input("Enter measurement value (cm): ").strip())


def process_data(cm: float) -> float:
    return cm / 2.54  # Convert cm to inches


def display_result(cm: float, inches: float) -> None:
    print(f"{cm:.2f} cm equals {inches:.2f} inches.")


def main() -> None:
    val = fetch_data()
    result = process_data(val)
    display_result(val, result)


if __name__ == "__main__":
    main()

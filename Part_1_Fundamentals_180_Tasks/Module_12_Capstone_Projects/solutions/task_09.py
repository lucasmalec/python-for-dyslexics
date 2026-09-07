"""
Task 12.09: ASCII Data Table Formatter
EN: Display multiple records in an aligned ASCII terminal table.
PL: Wyświetl wprowadzone dane w formie prostej tabeli ASCII.
Standard: PEP 8 (<= 88 characters)
"""

def print_table() -> None:
    records = [
        ("Alice", 28, "Engineer"),
        ("Bob", 34, "Architect"),
        ("Charlie", 22, "Analyst"),
    ]

    print(f"+{'-'*12}+{'-'*6}+{'-'*14}+")
    print(f"| {'Name':<10} | {'Age':<4} | {'Role':<12} |")
    print(f"+{'-'*12}+{'-'*6}+{'-'*14}+")
    for name, age, role in records:
        print(f"| {name:<10} | {age:<4} | {role:<12} |")
    print(f"+{'-'*12}+{'-'*6}+{'-'*14}+")


if __name__ == "__main__":
    print_table()

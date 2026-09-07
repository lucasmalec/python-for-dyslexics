"""
Task 12.01: Four Primitive Types Showcase
EN: Demonstrate int, float, str, and bool with descriptions.
PL: Napisz program, który używa typów: int, float, str, bool – wyświetl z opisem.
Standard: PEP 8 (<= 88 characters)
"""

def show_primitives() -> None:
    count: int = 42
    ratio: float = 3.14159
    label: str = "Production Cluster"
    is_online: bool = True

    print(f"1. Integer: {count} ({type(count).__name__}) - whole numbers")
    print(f"2. Float:   {ratio} ({type(ratio).__name__}) - decimals")
    print(f"3. String:  '{label}' ({type(label).__name__}) - textual data")
    print(f"4. Boolean: {is_online} ({type(is_online).__name__}) - binary state")


if __name__ == "__main__":
    show_primitives()

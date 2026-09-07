"""
Task 8.02: Four Spaces Indentation
EN: Standardize indentation: ensure 4 spaces per indent level instead of tabs.
PL: Popraw wcięcia w kodzie: zastąp tabulatory 4 spacjami.
Standard: PEP 8 (<= 88 characters)
"""

def demonstrate_indentation(is_active: bool) -> None:
    # 4 spaces indentation:
    if is_active:
        print("System is operational.")
    else:
        print("System is idle.")


demonstrate_indentation(True)

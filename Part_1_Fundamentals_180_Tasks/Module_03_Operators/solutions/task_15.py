"""
Task 3.15: Case Sensitive String Equality
EN: Compare strings 'Python' and 'python' – verify if they are equal.
PL: Porównaj napisy 'Python' i 'python' – czy są równe? Wyświetl wynik.
Standard: PEP 8 (<= 88 characters)
"""

str1 = "Python"
str2 = "python"

are_equal = (str1 == str2)
print(f"Comparing '{str1}' == '{str2}': {are_equal}")
print(f"Comparing lowercase '{str1.lower()}' == '{str2.lower()}': {str1.lower() == str2.lower()}")

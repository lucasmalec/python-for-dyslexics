"""
Task 7.03: F-String Formatting Integration
EN: Format results cleanly using modern Python f-strings.
PL: Sformatuj wynik za pomocą f-stringa.
Standard: PEP 8 (<= 88 characters)
"""

user_name = "Alex"
current_age = 28
future_age = current_age + 10

formatted_summary = (
    f"Profile Summary:\n"
    f"  - User:       {user_name}\n"
    f"  - Age Now:    {current_age}\n"
    f"  - In 10 Yrs:  {future_age}"
)
print(formatted_summary)

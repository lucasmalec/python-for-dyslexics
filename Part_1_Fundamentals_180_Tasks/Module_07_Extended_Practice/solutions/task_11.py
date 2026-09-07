"""
Task 7.11: Unified Multi-line F-String
EN: Display all gathered user attributes in a single, well-structured f-string.
PL: Wyświetl wszystkie dane w jednym zdaniu z użyciem jednego f-stringa.
Standard: PEP 8 (<= 88 characters)
"""

user = "Jordan"
age = 32
color = "emerald"
lucky_sum = 144

summary = (
    f"Hello {user}! You are currently {age} years old, your favorite aesthetic "
    f"is {color}, and your calculated lucky sum reaches {lucky_sum}."
)
print(summary)

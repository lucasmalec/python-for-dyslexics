"""
Task 7.01: Basic User Profile Interaction
EN: Prompt for name, age, lucky number. Display future age in 10 years and number * 3.
PL: Podstawowa wersja: poproś o imię, wiek, ulubioną liczbę. Wyświetl:
    'Cześć [imię]! Za 10 lat będziesz mieć [wiek+10] lat, a Twoja liczba razy 3 to [liczba*3].'
Standard: PEP 8 (<= 88 characters)
"""

name = input("Enter your name: ").strip()
age = int(input("Enter your age: ").strip())
lucky_number = int(input("Enter your lucky number: ").strip())

future_age = age + 10
scaled_number = lucky_number * 3

print(
    f"Hello {name}! In 10 years you will be {future_age} years old, "
    f"and your lucky number multiplied by 3 is {scaled_number}."
)

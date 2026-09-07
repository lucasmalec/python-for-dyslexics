"""
Task 10.03: Empty String Guard
EN: Prompt for text. If empty, notify user: 'No text provided.'.
PL: Poproś o tekst. Jeśli użytkownik nic nie wpisze, wyświetl: 'Nie podano tekstu.'
Standard: PEP 8 (<= 88 characters)
"""

text = input("Enter message: ").strip()

if not text:
    print("No text provided.")
else:
    print(f"Received message: {text}")

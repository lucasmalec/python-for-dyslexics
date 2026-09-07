"""
Task 12.05: Bidirectional Temperature Converter
EN: Convert temperature between Celsius and Fahrenheit based on user choice.
PL: Konwertuj temperaturę z °C na °F i odwrotnie.
Standard: PEP 8 (<= 88 characters)
"""

def convert_temp() -> None:
    choice = input("Convert from (C)elsius or (F)ahrenheit? ").strip().upper()
    try:
        temp = float(input("Enter temperature value: ").strip())
        if choice == "C":
            converted = (temp * 9 / 5) + 32
            print(f"{temp:.1f}°C = {converted:.1f}°F")
        elif choice == "F":
            converted = (temp - 32) * 5 / 9
            print(f"{temp:.1f}°F = {converted:.1f}°C")
        else:
            print("Invalid choice. Please select C or F.")
    except ValueError:
        print("Temperature value must be a number.")


if __name__ == "__main__":
    convert_temp()

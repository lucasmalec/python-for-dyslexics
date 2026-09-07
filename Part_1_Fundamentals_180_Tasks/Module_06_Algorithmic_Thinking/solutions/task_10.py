"""
Task 6.10: IPO Pattern: Speed and Distance
EN: Prompt for speed (km/h) and time (h), then compute travelled distance.
PL: Napisz program, który pobiera prędkość (km/h) i czas (h), a następnie
    oblicza dystans.
Standard: PEP 8 (<= 88 characters)
"""

# 1. INPUT
speed_kmh = float(input("Enter speed (km/h): ").strip())
time_hours = float(input("Enter travel time (hours): ").strip())

# 2. PROCESS
distance_km = speed_kmh * time_hours

# 3. OUTPUT
print(f"Total distance covered: {distance_km:.2f} km")

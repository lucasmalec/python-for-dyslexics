"""
Task 8.04: 88-Character Visual Line Limit
EN: Break a long line exceeding limits into clean, readable wrapped lines.
PL: Skróć długą linię dzieląc ją na kilka linii.
Standard: PEP 8 (<= 88 characters)
"""

# Long text wrapped smoothly within 88 columns:
announcement = (
    "This is a long announcement message designed to remain completely readable "
    "without requiring any horizontal scrolling on standard terminal displays."
)

print(announcement)

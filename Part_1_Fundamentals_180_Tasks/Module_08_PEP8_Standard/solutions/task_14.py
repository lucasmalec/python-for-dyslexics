"""
Task 8.14: Top-Level Imports Ordering
EN: Organize imports at the top of the file: standard library first.
PL: Umieść wszystkie importy na górze pliku.
Standard: PEP 8 (<= 88 characters)
"""

import math
import sys

print(f"Math pi constant: {math.pi:.4f}")
print(f"Python version: {sys.version.split()[0]}")

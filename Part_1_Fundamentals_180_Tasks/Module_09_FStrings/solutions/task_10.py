"""
Task 9.10: Function Invocation in Expressions
EN: Call `len('Python')` directly inside f-string interpolation braces `{}`.
PL: W f-stringu wywołaj funkcję `len('Python')` wewnątrz `{}`.
Standard: PEP 8 (<= 88 characters)
"""

keyword = "Python"
print(f"The string '{keyword}' has exactly {len(keyword)} characters.")

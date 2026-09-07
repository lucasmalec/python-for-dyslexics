"""
Task 11.15: Built-in Docstring Help
EN: Inspect docstring of `print` function using `print.__doc__`.
PL: Wpisz `help(print)` i przeczytaj dokumentację.
Standard: PEP 8 (<= 88 characters)
"""

# In terminal REPL: help(print)
# Programmatic inspection:
first_doc_line = print.__doc__.strip().splitlines()[0]
print(f"print docstring overview: {first_doc_line}")

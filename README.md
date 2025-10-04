Number System Converter (Base Translator) 🔢
A robust and reliable Python module for converting whole numbers between any two base systems, ranging from Base 2 (Binary) to Base 36 (using 0-9 and A-Z).

⚡ Quick Start
1. Setup
Save your code as a Python file (e.g., translator.py).

Import the main function, notation_(), into your script.

2. Basic Usage
Use the main function notation_(number, notation1, notation2). Remember to always pass the number as a string.

Python

# Import your module (assuming the file is named translator.py)
import translator 

# Example 1: Convert Hex F3 (Base 16) to Binary (Base 2)
result_binary = translator.notation_("F3", 16, 2)
print(f"F3 (16) -> {result_binary} (2)")
# Output: F3 (16) -> 11110011 (2)

# Example 2: Convert Binary 11100 (Base 2) to Decimal (Base 10)
result_decimal = translator.notation_("11100", 2, 10)
print(f"11100 (2) -> {result_decimal} (10)")
# Output: 11100 (2) -> 28 (10)

# Example 3: Handling lowercase input (auto-converts 'f' to 'F')
result_lower = translator.notation_("f", 16, 10)
print(f"f (16) -> {result_lower} (10)")
# Output: f (16) -> 15 (10)
🛠️ API Reference
notation_(number, notation1, notation2)
This is the primary function for performing all conversions.

Parameter	Type	Description
number	str	The whole number to be converted. Always pass as a string. Lowercase letters are automatically converted to uppercase.
notation1	int	The source base (must be between 2 and 36).
notation2	int	The target base (must be between 2 and 36).

Return Value
The function returns the converted number as a string. If the target base is 10, the result is still returned as a string (e.g., '28') for consistency.

🛑 Specific Error Handling
This module provides highly specific error messages to help the user immediately diagnose and fix input problems. If an error is detected, the function returns a string containing the specific error message.

Error Condition	Example Input	Returned Message (string)
Invalid Base Type	notation_("10", 'a', 10)	number system error: Bases must be integers (INT).
Invalid Base Range	notation_("10", 10, 0)	number system error: Bases must be between 2 and 36.
Invalid Character	notation_("A", 8, 10)	number system error: The character A is not valid in base 8 numbers.

⚙️ Project Structure
The conversion logic is separated into three clear functions:

notation_(): The main function. It performs all checks for Base Type and Base Range, handles the conversion flow, and returns the final result.

error_detection(): A utility that strictly checks if an individual character (e.g., 'A') is valid for the given source base (notation1). This is where the specific character error is generated.

translation_letters(): A helper function that handles the bi-directional mapping between numeric values (10-35) and their corresponding uppercase character representations ('A'-'Z').

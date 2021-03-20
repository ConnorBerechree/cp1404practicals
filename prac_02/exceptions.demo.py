"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur? A value error will occur when a non number is entered.
2. When will a ZeroDivisionError occur? A ZeroDivisionError will occur when a 0 is entered.
3. Could you change the code to avoid the possibility of a ZeroDivisionError? Unsure i believe all you could do Is change the outcome.
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")
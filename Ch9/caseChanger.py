"""
ChangeCase.py - This program converts a string to lowercase and uppercase.
Input:  Interactive
Output:  Uppercase and lowercase versions of the user-entered string.
"""

sample = input("Enter a string or done when you want to quit: ")

while sample != "done":
    # Call the lower method here and print the result.
    result=sample.lower()

    print("Lowercase: " + result)
    # Call upper method here and print the result.
    
    result = sample.upper()
    print("Uppercase: " + result)
    sample = input("Enter a string or done when you want to quit: ")
"""
Reverse.py - This program reverses numbers stored in an array.
Input: Interactive.
Output: Original contents of array and the reversed contents of the array.
"""


# Write reverseArray function here.
def rev(x):
        y=[]
        while x:
                 y.append(x.pop(len(x)-1))
        return y


x = [9, 8, 7, 6, 5]

# Print contents of array.
print("Original contents of array:",x)
# Call reverseArray function here.
y=rev(x)
# Print contents of reversed array.
print("Reversed contents of array:",y)


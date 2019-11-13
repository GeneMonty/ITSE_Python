"""
SumAndProduct.py - This program computes sums and products.
Input:  Interactive.
Output:  Computed sum and product.
"""


# Write sums() function here.
def sums(x):
        num = 1
        while x > 1:
                num = num + x
                x = x - 1
        print(num)

# Write products() function here.
def products(x):
        num = 1
        while x >= 1:
                num = num * x 
                x = x - 1 
        print(num)

numberString = input("Enter a positive integer or 0 to quit: ")
x = int(numberString)

while x != 0:
    # Call sums() function here.
    sums(x)

    # Call products() function here.
    products(x)

    numberString = input("Enter a positive integer or 0 to quit: ")
    x = int(numberString)



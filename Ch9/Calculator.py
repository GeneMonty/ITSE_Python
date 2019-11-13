# Calculator.py - This program performs arithmetic, ( +. -, *. / ) on two numbers.
# Input:  Interactive
# Output:  Result of arithmetic operation

# Write performOperation function here

def performOperation(a,b,op):
        if op == '+':
                result = a + b
                return result
        elif op == '-':
                result = a - b
                return result
        elif op == '*':
                result = a * b
                return result
        elif op == '/':
                result = a / b
                return result



if __name__ == '__main__':
        a = int(input("Enter the first number: "))
        b = int(input("Enter the second number: "))
        op = input("Enter an operator (+ - * /): ")

    # Call performOperation method here and store the value in "result"
    
        result = performOperation(a,b,op) # get the return value 

        print(str(a) + " " + op + " " + str(b) + " = " + str(result))

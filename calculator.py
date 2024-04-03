num1 = float(input("Enter first number: "))
op = input("Enter Operator: ")
num2 = float(input("Enter second number: "))

if op == '+':
    print("Sum of is: " ,(num1 + num2))
elif op == '-':
    print("Difference of is: ",(num1 - num2))
elif op == '/' and num2 !=0:
    print("quotient  is: " ,(num1 / num2))
elif op == '*':
    print("Multiplication  is: " ,(num1 * num2))
else:
    print("Invalid Operation")
# X Ask the user for the first number.
# X Ask the user for the second number.
# X Ask the user for an operation to perform.
# X Perform the operation on the two numbers.
# X Print the result to the terminal

print('Welcome to the Calculator!')

result = 0

print('Please enter the first number')
num1 = input()

print('Please enter the second number')
num2 = input()

print('Please select the operation that you want to perform \n' \
      '1) Add 2) Subtract 3) Multiply and 4) Division')

operation = input()

if operation == "1": # user has selected Addition
    result = int(num1) + int(num2)
elif operation == "2": # user has selected Subtraction
    result = int(num1) - int(num2)
elif operation == "3": # user has select Multiplication
    result = int(num1) * int(num2)
elif operation == "4": # user has selected Division
    result = int(num1) / int(num2)

print(f'The result is {result}')


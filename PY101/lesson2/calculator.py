# X Ask the user for the first number.
# X Ask the user for the second number.
# X Ask the user for an operation to perform.
# X Perform the operation on the two numbers.
# X Print the result to the terminal

def prompt(message):
    print(f"==> {message}")

def invalid_number(number_str):
    try:
        int(number_str)
    except ValueError:
        return True

    return False 




prompt('Welcome to the Calculator!')


prompt('Please enter the first number')
num1 = input()

while invalid_number(num1):
    prompt("Hmm... that doesn't look like a valid number.")
    num1 = input()


prompt('Please enter the second number')
num2 = input()

while invalid_number(num2):
    prompt("Hmm... that doesn't look like a valid number.")
    num2 = input()


prompt('Please select the operation that you want to perform \n' \
      '1) Add 2) Subtract 3) Multiply and 4) Division')

operation = input()

while operation not in ["1", "2", "3", "4"]:
    prompt('You must choose 1, 2, 3, or 4')
    operation = input()

match operation:

    case "1": # user has selected Addition
        output = int(num1) + int(num2)
    case "2": # user has selected Subtraction
        output = int(num1) - int(num2)
    case "3": # user has select Multiplication
        output = int(num1) * int(num2)
    case "4": # user has selected Division
        output = int(num1) / int(num2)

prompt(f'The result is {output}')


def calculate(first, second, operator):
    match operator:
        case '+': return first + second
        case '-': return first - second
        case '*': return first * second
        case '/': return first/ second
        case '//': return first // second
        case '%': return first % second
        case '**': return first ** second

first_float = float(input("==> Enter the first number:\n"))
second_float = float(input("==> Enter the second number:\n"))
for operator in ['+', '-', '*', '/', '//', '%', '**']:
    operation = f"{first_float} {operator} {second_float}"
    result = calculate(first_float, second_float, operator)
    print(f"==> {operation} = {result}")
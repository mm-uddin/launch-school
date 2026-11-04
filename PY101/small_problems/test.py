def multiply(num1, num2):
    return num1 * num2


def power_of_num(num, power):
    result = 1 
    for i in range(power):
        result = multiply(result, num)
    return result

print(power_of_num(3, 3) == 27)
print(power_of_num(5, 0) == 1)
print(power_of_num(5, 1) == 5)
print(power_of_num(-2, 3) == -8)
print(power_of_num(-2, 4) == 16)
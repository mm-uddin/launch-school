def factors(number):
    divisor = number
    result = []
    while divisor > 0:
        if number % divisor == 0:
            result.append(number // divisor)
        divisor -= 1
    return result

'''
The purpose of "number % divisor == 0" is to determine
whether number is divisible by divisor. Because if it
is divisible and there is no remainder, then it is
a factor of the number.

'''
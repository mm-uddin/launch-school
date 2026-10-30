'''
Print all odd numbers from 1 to 99, inclusive, 
with each number on a separate line.

Bonus Question: 
Can you solve the problem by iterating over just the odd numbers?

'''

# Version using for loop

# def display_odd():
#     for i in range(100):
#         if i % 2 == 1:
#             print(i)

# display_odd()



# using while loop


# def display_odd():
#     num = 1
#     while num < 100:
#         if num % 2 == 1:
#             print(num)
#         num += 2

# display_odd()


# for num in range(1, 100, 2):
#     print(num)


#  Further exploration

# Consider adding a way for the user to specify the starting 
# and ending values of the odd numbers printed.

print("Welcome to Printing Odds")
print("This program prints all " \

"the add numbers within a range given by you!")
print("What is the starting odd number?")
num1 = input()

print("What is the ending odd number?")
num2 = input()
print("Here are the results")

for num in range(int(num1), int(num2)+1, 2):
    print(num)
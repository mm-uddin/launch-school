'''
Print all even numbers from 1 to 99, inclusive, 
with each number on a separate line.

Bonus Question: 
Can you solve the problem by iterating over just the even numbers?
'''

# def display_even_nums():
#     for i in range(1, 99):
#         if i % 2 == 0:
#             print(i)


def display_even_nums():
    for i in range(2, 99, 2):
        print(i)


display_even_nums()
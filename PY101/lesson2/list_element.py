# Problem:
# a function that takes a list of integers, 
# and returns a new list with every other element from the original list, 
# starting with the first element

"""
Pseudocode:
- Take a list of integer as an argument
- Create a new list by taking every other integer from the list starting 
  from the first integer in the list.
- Return the new list

Formal Pseudocode:

START

# Given a list of integers called int_list

SET new_list = []
SET iterator = 0

WHILE iterator < length of int_list
    SET current_integer = value within int_list at space "iterator"
    SET new_list = new_list + current_integer
    SET iterator = iterator + 2

PRINT new_list  

"""
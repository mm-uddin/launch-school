# Problem: a function that takes two lists of numbers and returns 
# the result of merging the lists. The elements of the first list 
# should become the elements at the even indexes of the returned list, 
# while the elements of the second list should become the elements at the
# odd indexes. 
# For instance: merge([1, 2, 3], [4, 5, 6]) # => [1, 4, 2, 5, 3, 6]

"""
Pseudocode:
- take two list of numbers as arguments

- Create a new merged list with adding 
  numbers from two list maintaining
  the numbers from first go to the odd
  indexes of merged list and numbers from the second
  list go to the even indexes of the merged list 

  - Return the merged list

Formal Pseudocode:

START:

# # Given the two list of numbers are called list1 and list2

SET iterator = 0
SET merged_list = []

WHILE iterator is less than length of list1
    SET current_item_list1 = value within list1 at space "iterator"
    SET current_item_list2 = value within list2 at space "iterator"
    APPEND current_item_list1 to merged_list
    APPEND current_item_list2 to merged_list

PRINT merged_list

"""

def merged_list(list1, list2):
    final_list = []
    for n in range(len(list1)):
        final_list.append(list1[n])
        final_list.append(list2[n])
    return final_list

print(merged_list([1, 2, 3], [4, 5, 6]))

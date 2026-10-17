# Problem: 
# a function that takes a list of strings, and returns 
# a string that is all those strings concatenated together

"""
Pseudocode:
- Take a list of strings as arguments
- Concatenate the strings into a single string
- Return the concatenated string


Formal Pseudocode:

START

# Given the list of strings is called str_list

SET concatenated_string = ""
SET iterator = 0

WHILE iterator < length of str_list:
    SET current_string = value within str_list at space "iterator"
    SET concatenated_string = concatenated_string + current_string
    SET iterator = iterator + 1

PRINT concatenated_string (i.e returns the concatenated string)

END

"""
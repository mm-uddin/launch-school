# Problem:
# a function that determines the index of the 3rd occurrence
# of a given character in a string.
# For instance, if the given character is 'x' and the string
# is 'axbxcdxex', the function should  return 6 (the index of the 3rd 'x').
# If the given character does not occur at least 3 times, return None.


"""
Pseudocode:

- Take a character and a string as arguments.
- Check and compare each character in the string with the given character.
- Return the index of the character in the string that matches
  3rd time  with the given character.
- If three matches is not found and checking of
  every character in the string is done return none.


Formal Pseudocode:

START

# given the character is called my_char and the string is called target_string

SET iterator = 0
SET number_of_occurence = 0

WHILE iterator < length of target_string
    SET current_char = value within target_string at space "iterator"
    IF current_char == my_char
        SET number_of_occurence = number_of_occurence + 1
    SET iterator = iterator +1

    IF number_of_occurence == 3
        return iterator

IF number_of_occurence < 3
    return None
         
 END 

"""

"""
Module third_occurence.py

This modules find a character's third time occurence positiion
in a given string

"""

def  thrd_occurence(spcl_chr, mssg):
    number_of_occurence = 0
    for n in range(len(mssg)):
        if mssg[n] == spcl_chr:
            number_of_occurence += 1
        if number_of_occurence == 3:
            return n

    if number_of_occurence < 3:
        return None



print(thrd_occurence('x', 'abcd'))

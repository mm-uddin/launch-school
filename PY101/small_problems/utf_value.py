'''

Problem Statement:
------------------
Write a function that determines and returns the UTF-16 string value of a 
string passed in as an argument. The UTF-16 string value is the sum of the 
UTF-16 values of every character in the string. 
(You may use ord to determine the UTF-16 value of a character.)


// Step 1. Understanding the problem:
We have to come up with a function that takes a string as an argument
and returns utf-16 value of the string which is sum of utf16 string value 
of each individual character.

// Step 2. Examples:

Example 1:

utf16_value('Four score') will return 984
utf16_value('a') will return 97

// Step 3. Data Structure:
input:
- a string
output:
- a string

// Step 4. Algorithm:
1. create a variable called total_string_value and assign 0 to it
2. Loop through each character in the string
3. get the utf16 value of each character using ord() function
4. Add it to the total_string_value and update the value of total_string_value
5. return total_string_value


'''

def utf16_value(str):
    total_string_value = 0
    for char in str:
        total_string_value += ord(char)
    return total_string_value

# These examples should all print True
print(utf16_value('Four score') == 984)
print(utf16_value('Launch School') == 1251)
print(utf16_value('a') == 97)
print(utf16_value('') == 0)

OMEGA = "\u03A9"              # UTF-16 character 'Ω' (omega)
print(utf16_value(OMEGA) == 937)
print(utf16_value(OMEGA + OMEGA + OMEGA) == 2811)
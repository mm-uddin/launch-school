'''
Write a function that takes two strings as arguments, determines the length 
of the two strings, and then returns the result of concatenating the shorter 
string, the longer string, and the shorter string once again. 
You may assume that the strings are of different lengths.

//Step 1: understand the problem
- input: two strings
- output: short_string + long_string + short_string

// Step 2: Example:

- print(short_long_short('abc', 'defgh'))/ 
  will print'abcdefghabc'

- print(short_long_short('abcdef', 'fgh'))/
  will print 'fghabcdeffgh'


// Step 3: Data Structure:
- input is string
- output is string too

// Step 4: Algorithm

- 1. get length of the two strings
- 2. store them two variable : length_str1 and length_str2
- 3. if length_str1 < length_str2 
     then print length_str1 + length_str2 + length_str1
     else:
     print length_str2 + length_str1 + length_str2

'''
def short_long_short(str1, str2):
    length_str1 = len(str1)
    length_str2 = len(str2)
    if length_str1 < length_str2:
        return (str1 + str2 + str1)
    else:
        return (str2 + str1 + str2)

print(short_long_short('abc', 'defgh') == "abcdefghabc")
print(short_long_short('abcde', 'fgh') == "fghabcdefgh")
print(short_long_short('', 'xyz') == "xyz")
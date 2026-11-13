'''
Problem Statement:
------------------
Write a function that takes a string argument and returns a new string 
that contains the value of the original string with all consecutive 
duplicate characters collapsed into a single character.

'''

def crunch(text):
    if not text:
        return text
    new_str = text[0]
    length_str = len(text)
    for i in range(1, length_str):
        if text[i] != text[i-1]:
            new_str += text[i]
    return new_str

# These examples should all print True
print(crunch('ddaaiillyy ddoouubbllee') == 'daily double')
print(crunch('4444abcabccba') == '4abcabcba')
print(crunch('ggggggggggggggg') == 'g')
print(crunch('abc') == 'abc')
print(crunch('a') == 'a')
print(crunch('') == '')
'''
Problem Statement:
------------------
Write a function that takes a short line of text and prints it within a box.

print_in_box('To boldly go where no one has gone before.')

+--------------------------------------------+
|                                            |
| To boldly go where no one has gone before. |
|                                            |
+--------------------------------------------+

'''

def print_in_box(text, max_length = 0):
    length_text = len(text)
    if max_length!=0 and length_text > max_length:
        length_text = max_length
    
    plus_line = f"+{(length_text+2) * '-'}+"
    empty_line = f"| {length_text * ' '} |"
    print(plus_line)
    print(empty_line)
    print(f"| {text[:length_text]} |")
    print(empty_line)
    print(plus_line)

print_in_box('To boldly go where no one has gone before. I am here to stay', 50)
print_in_box('', 20)

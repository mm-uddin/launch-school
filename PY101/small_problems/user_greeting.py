'''
Problem Statement:
-----------------
Write a program that asks for user's name, then greets the user. 
If the user appends a ! to their name, the computer will yell 
the greeting (print it using all uppercase).

'''
print('What is your name?')
name = input()

if name.endswith("!"):
    print(f"HELLO {name.upper()} WHY ARE WE YELLING?")
else:
    print(f"Hello {name}!")
'''
Problem Statements:
-------------------
Create a function that takes 2 arguments, a list and a dictionary. 
The list will contain 2 or more elements that, when joined with spaces, 
will produce a person's name. The dictionary will contain two keys, "title" 
and "occupation", and the appropriate values. Your function should return a 
greeting that uses the person's full name, and mentions the person's title.


// Step 1. Understanding the problem.

- We have to create a function that takes a list and a dictionary
as arguments
- The list will contain two or more elements, joining of which with
spaces will give us a name 
- The dictionary will contain two keys 'title' and 'occupation' along
with their values,
- The function will return person's full name and title

// Step 2. Examples:

greetings(
    ["John", "Q", "Doe"],
    {"title": "Master", "occupation": "Plumber"},
) 

will return # Hello, John Q Doe! Nice to have a Master Plumber around

// Step 3. Data structures
- Input:
    - a list with two or more elements
    - a dictionary with with two keys and values
- Output:
    - a string

// Step 4. Algorithm

1. join the elements in the list and assign the value to name variable
2. return string with name and  given_dictionary['title'] 
   and given_dictionary['occupation']

'''

 
def greetings(name_list, title_dict):
    name = " ".join(name_list)
    # print(name)
    print(f"Hello {name}! So you are a {title_dict['title']} {title_dict['occupation']!}")
    # print(title_dict['title'])
greetings(
    ["John", "Q", "Doe"],
    {"title": "Master", "occupation": "Plumber"},
)

# Hello, John Q Doe! Nice to have a Master Plumber around.
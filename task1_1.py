'''
Task №1
In this task you will create a function 
that takes a list of non-negative integers and strings 
and returns a new list with the strings filtered out.
'''

def filter_list(b):
    new_list = []
    for el in b:
        if type(el) == int:
            new_list.append(el)


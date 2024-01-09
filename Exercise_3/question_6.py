"""
Write a program that accepts two lists of integers and prints a new list containing all 
elements of the first list followed by all elements of the second.
"""

def combine_list(list1, list2):
    result = list1 + list2
    print(result)
a = [1,2,3,4]
b= [5,6,7,8]
combine_list(a, b)
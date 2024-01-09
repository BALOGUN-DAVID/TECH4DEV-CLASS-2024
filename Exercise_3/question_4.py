"""
    Write a program that accepts two lists of integers and prints true if each element in the first 
    list is less than the element at the same index in the second list. Your program should print 
    false if the lists are not the same length. 
"""

def compare_list(List1, List2):
    if len(List1) != len(List2):
        return False
    for i in range(len(List1)):
        if List1[i] > List2[i]:
            return False
    return True
a = [2,4,6]
b = [8,10,12]
compare_list(a, b)
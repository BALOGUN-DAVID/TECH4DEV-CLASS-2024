#!/usr/bin/env python
# coding: utf-8

# ### 1. Write a program that finds the maximum value of the given list, assuming that the list
# contains at least one element.

# In[1]:


def Minimumvalue():
    user = []
    question = int(input("How many numbers do you want to enter? "))
    prompt = 0
    while question > 0:
        prompt = prompt + 1
        num = int(input(f"Number{prompt} = "))
        user.append(num)
        if question == prompt:
            break
    import numpy as np
    min = np.min(user)
    print(f'The minimum number is  = {min}')
    


      
Minimumvalue()


# ### 2. Write a program that calculates the average value of the given list

# In[4]:


def Averagevalue():
    user = []
    question = int(input("How many numbers do you want to enter? "))
    prompt = 0
    while question > 0:
        prompt = prompt + 1
        num = int(input(f"Number{prompt} = "))
        user.append(num)
        if question == prompt:
            break
    import numpy as np
    avg = np.mean(user)
    print(f'The Average value is  = {avg}')
    


      
Averagevalue()


# Write a program that prints the given list of integers in reverse order.
# Try your program with the following list
# 2 6 7 45 23 53 14 45 89 5

# In[12]:


# Input list of integers
input_list = list(map(int, input("Enter a list of integers (space-separated): ").split()))

# Print the list in reverse order
reversed_list = input_list[::-1]
print("Reversed list:", reversed_list)


# Write a program that accepts two lists of integers and prints true if each element in the first list is less than the element at the same index in the second list. Your program should print false if the lists are not the same length.

# In[11]:


def compare_lists(list1, list2):
    if len(list1) != len(list2):
        return False

    
    for i in range(len(list1)):
        if list1[i] >= list2[i]:
            return False

    return True


list1 = list(map(int, input("Enter the first list of integers (space-separated): ").split()))
list2 = list(map(int, input("Enter the second list of integers (space-separated): ").split()))


result = compare_lists(list1, list2)
print(result)


# Write a program that accepts a list of integers and two indexes and swaps the elements at 
# those indexes

# In[ ]:


def swap_elements(lst, index1, index2):
    
    if 0 <= index1 < len(lst) and 0 <= index2 < len(lst):
        # Swap the elements
        lst[index1], lst[index2] = lst[index2], lst[index1]
        return True
    else:
        return False


input_list = list(map(int, input("Enter a list of integers (space-separated): ").split()))


index1 = int(input("Enter the first index to swap: "))
index2 = int(input("Enter the second index to swap: "))


success = swap_elements(input_list, index1, index2)

if success:
    print("List after swapping elements:", input_list)
else:
    print("Invalid indexes. Swap failed.")


# Write a program that accepts two lists of integers and prints a new list containing all elements of the first list followed by all elements of the second.

# In[ ]:


def concatenate_lists(list1, list2):
    # Concatenate the two lists
    result_list = list1 + list2
    return result_list

# Input lists
list1 = list(map(int, input("Enter the first list of integers (space-separated): ").split()))
list2 = list(map(int, input("Enter the second list of integers (space-separated): ").split()))

# Concatenate the lists and print the result
result = concatenate_lists(list1, list2)
print("Concatenated list:", result)


# Write a program that accepts a list of integers and an integer value as its parameters and 
# prints the last index at which the value occurs in the list. The program should print –1 if the 
# value is not found. For example, in the list [74, 85, 102, 99, 101, 85, 56], the last index of the 
# value 85 is 5

# In[ ]:


def last_index_of_value(lst, value):
    # Check if the value is present in the list
    if value in lst:
        # Find the last index of the value using list comprehension
        last_index = max([i for i, x in enumerate(lst) if x == value])
        return last_index
    else:
        return -1

# Input list of integers
input_list = list(map(int, input("Enter a list of integers (space-separated): ").split()))

# Input integer value to search
search_value = int(input("Enter the value to find the last index: "))

# Find and print the last index of the value
result = last_index_of_value(input_list, search_value)
print("Last index of {} in the list: {}".format(search_value, result))


# Write a program that prints the range of values in a list of integers. The range is defined as 1 
# more than the difference between the maximum and minimum values in the list. For 
# example, if a list contains the values [36, 12, 25, 19, 46, 31, 22], the program should return 
# 35. You may assume that the list has at least one element

# In[ ]:


def calculate_range(lst):
    # Find the minimum and maximum values in the list
    min_value = min(lst)
    max_value = max(lst)

    # Calculate the range
    range_value = max_value - min_value + 1

    return range_value

# Input list of integers
input_list = list(map(int, input("Enter a list of integers (space-separated): ").split()))

# Calculate and print the range of values in the list
result = calculate_range(input_list)
print("Range of values in the list:", result)


# Write a program that accepts a list of integers, a minimum value, and a maximum value and 
# prints the count of how many elements from the list fall between the minimum and 
# maximum (inclusive). For example, in the list [14, 1, 22, 17, 36, 7, -43, 5], for minimum value 
# 4 and maximum value 17, there are four elements whose values fall between 4 and 17

# In[ ]:


def count_elements_between(lst, min_val, max_val):
    # Filter the elements that fall between the minimum and maximum values
    filtered_elements = [x for x in lst if min_val <= x <= max_val]

    # Count the number of elements in the filtered list
    count = len(filtered_elements)

    return count

# Input list of integers
input_list = list(map(int, input("Enter a list of integers (space-separated): ").split()))

# Input minimum and maximum values
min_value = int(input("Enter the minimum value: "))
max_value = int(input("Enter the maximum value: "))

# Count and print the number of elements between the specified range
result = count_elements_between(input_list, min_value, max_value)
print("Number of elements between {} and {}: {}".format(min_value, max_value, result))


# . Write a program that accepts a list of real numbers and prints true if the list is in sorted 
# (nondecreasing) order and false otherwise. For example, if lists named list1 and list2 store 
# [16.1, 12.3, 22.2, 14.4] and [1.5, 4.3, 7.0, 19.5, 25.1, 46.2] respectively, the program should 
# print false for list1 and true for list2 respectively. Assume the list has at least one element. A 
# one-element list is sorted

# In[ ]:


def is_sorted(lst):
    # Check if the list is in sorted (non-decreasing) order
    return all(lst[i] <= lst[i+1] for i in range(len(lst)-1))

# Input list of real numbers
input_list = list(map(float, input("Enter a list of real numbers (space-separated): ").split()))

# Check and print whether the list is in sorted order
result = is_sorted(input_list)
print(result)


#!/usr/bin/env python
# coding: utf-8

# 1. Write a program that finds the maximum value of the given list, assuming that the list
# contains at least one element.
# Try your program with the following array
# 2 4 7 4 23 5 1 4 8 9

# In[5]:


def find_max_value(numb):
     
    max_value = numb[0]

    for n in numb:
        if n > max_value:
            max_value = n

    return max_value

# the array
array = [2, 4, 7, 4, 23, 5, 1, 4, 8, 9]

# Find and print the maximum value
max_value = find_max_value(array)
print(f"The maximum value in the list is: {max_value}")


# 2. Write a program that calculates the average value of the given list.
# Try your program with the following list
# 4 7 1 5 11 53 12 46 84 23

# In[1]:


def calculate_average(nums):
    # Ensure the list is not empty
    if not nums:
        return 0  # Return 0 for an empty list

    # Calculate the average
    average = sum(nums) / len(nums)

    return average

# Example list
my_list = [4, 7, 1, 5, 11, 53, 12, 46, 84, 23]

# Calculate and print the average value
average_value = calculate_average(my_list)
print(f"The average value of the list is: {average_value}")


# 3.Write a program that prints the given list of integers in reverse order.
# Try your program with the following list
# 2 6 7 45 23 53 14 45 89 5

# In[2]:


def print_reverse(numb):
    # Print the list in reverse order
    for num in reversed(numb):
        print(num, end=" ")

# Example
array = [2, 6, 7, 45, 23, 53, 14, 45, 89, 5]

# Print the list in reverse order
print_reverse(array)


# 4.Write a program that accepts two lists of integers and prints true if each element in the first
# list is less than the element at the same index in the second list. Your program should print
# false if the lists are not the same length.

# In[3]:


def compare_lists(list1, list2):
    # Check if the lists are of the same length
    if len(list1) != len(list2):
        return False  # Lists are not the same length

    # Check if each element in list1 is less than the corresponding element in list2
    for i in range(len(list1)):
        if list1[i] >= list2[i]:
            return False  # Condition not met for at least one pair of elements

    return True  # All pairs of elements satisfy the condition

# Example array
arrayA = [2, 6, 7, 45, 23, 53, 14, 45, 89, 5]
arrayB = [3, 8, 10, 50, 30, 60, 20, 50, 90, 10]

# Check and print the result
result = compare_lists(arrayA, arrayB)
print(f"Result: {result}")


# In[4]:


def compare_lists(list1, list2):
    # Check if the lists are of the same length
    if len(list1) != len(list2):
        return False  # Lists are not the same length

    # Check if each element in list1 is less than the corresponding element in list2
    for i in range(len(list1)):
        if list1[i] >= list2[i]:
            return False  # Condition not met for at least one pair of elements

    return True  # All pairs of elements satisfy the condition

# Example array
arrayA = [2, 6, 7, 45, 23, 53, 14, 45, 89, ]
arrayB = [3, 8, 10, 50, 30, 60, 20, 50, 90, 10]
#the array lengths are not the same, it would print false

# Check and print the result
result = compare_lists(arrayA, arrayB)
print(f"Result: {result}")


# 5.Write a program that accepts a list of integers and two indexes and swaps the elements at
# those indexes

# In[5]:


def swap_elements(array, index1, index2):
    # Check if the indexes are valid
    if 0 <= index1 < len(array) and 0 <= index2 < len(array):
        # Swap elements at the specified indexes
        array[index1], array[index2] = array[index2], array[index1]
        return True  # Swap successful
    else:
        return False  # Invalid indexes

# Example array
my_array = [2, 6, 7, 45, 23, 53, 14, 45, 89, 5]

# Example indexes to swap
index_to_swap1 = 1 #6
index_to_swap2 = 7 #45

# Check and print the result
result = swap_elements(my_array, index_to_swap1, index_to_swap2)

if result:
    print(f"Swapped elements at indexes {index_to_swap1} and {index_to_swap2}: {my_array}")
else:
    print("Invalid indexes, swap unsuccessful.")


# 6.Write a program that accepts two lists of integers and prints a new list containing all
# elements of the first list followed by all elements of the second.

# In[6]:


def concatenate_lists(list1, list2):
    # Concatenate the two lists
    result_list = Age_group1 + Age_group2
    return result_list

# Example lists
Age_group1 = [56, 55, 50]
Age_group2 = [20, 30, 35]

# Concatenate lists and print the result
result = concatenate_lists(Age_group1, Age_group2)
print("Concatenated List:", result)


# 7.Write a program that accepts a list of integers and an integer value as its parameters and
# prints the last index at which the value occurs in the list. The program should print –1 if the
# value is not found. For example, in the list [74, 85, 102, 99, 101, 85, 56], the last index of the
# value 85 is 5.

# In[7]:


def last_index_of_value(lst, value):
    # Check if the value is present in the list
    if value in lst:
        # Find the last index of the value using the reversed list
        last_index = len(lst) - 1 - lst[::-1].index(value)
        return last_index
    else:
        return -1

# Example list
my_list = [74, 85, 102, 99, 101, 85, 56]

# Example value
search_value = 85

# Find the last index of the value and print the result
result = last_index_of_value(my_list, search_value)
print(f"The last index of {search_value} is: {result}")


# In[8]:


def last_index_of_value(lst, value):
    # Check if the value is present in the list
    if value in lst:
        # Find the last index of the value using the reversed list
        last_index = len(lst) - 1 - lst[::-1].index(value)
        return last_index
    else:
        return -1

# Example list
my_list = [7, 5, 12, 9, 11, 5, 5]

# Example value
search_value = 85

# Find the last index of the value and print the result
result = last_index_of_value(my_list, search_value)
print(f"The last index of {search_value} is: {result}")


# In[9]:


def last_index_of_value(lst, value):
    # Check if the value is present in the list
    if value in lst:
        # Find the last index of the value using the reversed list
        last_index = len(lst) - 1 - lst[::-1].index(value)
        return last_index
    else:
        return -1

# Example list
my_list = [7, 5, 12, 9, 11, 5, 5]

# Example value
search_value = 12

# Find the last index of the value and print the result
result = last_index_of_value(my_list, search_value)
print(f"The last index of {search_value} is: {result}")


# 8.Write a program that prints the range of values in a list of integers. The range is defined as 1
# more than the difference between the maximum and minimum values in the list. For
# example, if a list contains the values [36, 12, 25, 19, 46, 31, 22], the program should return
# 35.You may assume that the list has at least one element.

# In[11]:


def calculate_range(lst):
    # Calculate the range as 1 more than the difference between the max and min values
    range_value = max(lst) - min(lst) + 1
    return range_value

# let's run this
default_list = [36, 12, 25, 19, 46, 31, 22]

# Calculate and print the range of values in the list
result = calculate_range(default_list)
print(f"The range of values in the list is: {result}")


# In[12]:


def calculate_range(lst):
    # Calculate the range as 1 more than the difference between the max and min values
    range_value = max(lst) - min(lst) + 1
    return range_value

# let's run this
default_list = [150, 110, 80, 100, 10, 31, 22]

# Calculate and print the range of values in the list
result = calculate_range(default_list)
print(f"The range of values in the list is: {result}")


# 9.Write a program that accepts a list of integers, a minimum value, and a maximum value and
# prints the count of how many elements from the list fall between the minimum and
# maximum (inclusive). For example, in the list [14, 1, 22, 17, 36, 7, -43, 5], for minimum value
# 4 and maximum value 17, there are four elements whose values fall between 4 and 17.

# In[13]:


def count_elements_in_range(lst, min_val, max_val):
    # Filter the elements that fall between the minimum and maximum values
    elements_in_range = [element for element in lst if min_val <= element <= max_val]
    
    # Count the number of elements in the range
    count = len(elements_in_range)
    
    return count

# Example list
my_list = [14, 1, 22, 17, 36, 7, -43, 5]

# Minimum and maximum values
min_value = 4
max_value = 17

# Count and print the number of elements in the specified range
result = count_elements_in_range(my_list, min_value, max_value)
print(f"The number of elements between {min_value} and {max_value} (inclusive) is: {result}")


# In[15]:


def count_elements_in_range(lst, min_val, max_val):
    # Filter the elements that fall between the minimum and maximum values
    elements_in_range = [element for element in lst if min_val <= element <= max_val]
    
    # Count the number of elements in the range
    count = len(elements_in_range)
    
    return count

# Example list
my_list = [14, 1, 22, 17, 36, 7, -43, 5,150, 110, 80, 100, 10, 31, 22]

# Minimum and maximum values
min_value = 20
max_value = 80

# Count and print the number of elements in the specified range
result = count_elements_in_range(my_list, min_value, max_value)
print(f"The number of elements between {min_value} and {max_value} (inclusive) is: {result}")


# 10.Write a program that accepts a list of real numbers and prints true if the list is in sorted
# (nondecreasing) order and false otherwise. For example, if lists named list1 and list2 store
# [16.1, 12.3, 22.2, 14.4] and [1.5, 4.3, 7.0, 19.5, 25.1, 46.2] respectively, the program should
# print false for list1 and true for list2 respectively. Assume the list has at least one element. A
# one-element list is sorted.

# In[16]:


def is_sorted(lst):
    # Check if the list is sorted in non-decreasing order
    return all(lst[i] <= lst[i + 1] for i in range(len(lst) - 1))

# Example lists
list1 = [16.1, 12.3, 22.2, 14.4]
list2 = [1.5, 4.3, 7.0, 19.5, 25.1, 46.2]

# Check and print if list1 is sorted
result_list1 = is_sorted(list1)
print(f"Is list1 sorted? {result_list1}")

# Check and print if list2 is sorted
result_list2 = is_sorted(list2)
print(f"Is list2 sorted? {result_list2}")


# In[18]:


def is_sorted(lst):
    # Check if the list is sorted in non-decreasing order
    return all(lst[i] <= lst[i + 1] for i in range(len(lst) - 1))

# Example lists
list1 = [25, 12, 2, 1]
list2 = [11, 10, 9, 8, 7, 6]
list3 = [10,20,30,40,50,60,80,96]

# Check and print if list1 is sorted
result_list3 = is_sorted(list3)
print(f"Is list3 sorted? {result_list3}")

# Check and print if list2 is sorted
result_list2 = is_sorted(list2)
print(f"Is list2 sorted? {result_list2}")


# # CLASS WORK

# 1)Print the First 10 natural numbers

# In[19]:


print(1,2,3,4,5,6,7,8,9,10)


# 2)print("====The First 10 Natural Numbers====")

# In[20]:


print("====The First 10 Natural Numbers====")


# 3)Count the total number of digits in a number

# In[24]:


number=1122334455566789
count=0
while number!=0:
    number=number//10
    count=count+1
print('Digit Total:',count)
    


# In[41]:


n=int(input('enter n:'))
ct=0
while n!=0:
    n=n//10
    #// is float division
    ct+=1
print('number of digits:',ct)


# 4)Write a program to display all prime numbers within a range

# In[42]:


def is_prime(num):
    # Function to check if a number is prime
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def display_primes_in_range(start, end):
    # Function to display prime numbers within a range
    primes = [num for num in range(start, end + 1) if is_prime(num)]
    return primes

# Example usage
start_range = 5
end_range = 30

prime_numbers = display_primes_in_range(start_range, end_range)
print(f"Prime numbers between {start_range} and {end_range}: {prime_numbers}")


# 5)Write a program to print a multiplication table of a given number

# In[44]:


def multiplication_table(number, start=1, end=12):
    # Function to print a multiplication table for a given number
    print(f"Multiplication Table for {number} (from {start} to {end}):")
    for i in range(start, end + 1):
        result = number * i
        print(f"{number} x {i} = {result}")

# Example
given_number = 2
multiplication_table(given_number)


# In[47]:


#lets have some fun here
print('\t\t\tMultiplication Tables\n')

for a in range (1,13):
    print(a)
#this prints vertically,we ain't done. Let's continue


# In[48]:


#lets have some fun here
print('\t\t\tMultiplication Tables\n')

for a in range (1,13):
    print(a,end='\t')
#we added the \t


# In[59]:


print('\t\t\t\tMultiplication Tables\n')

for a in range (1,13):
    print(a,end='\t')
print() #print space
print('___________________________________________________________________________________________\n')#print a line

for b in range (1,13):
    for c in range(1,13):
        print(b*c,end='\t')
    print('\n')
    


# In[ ]:





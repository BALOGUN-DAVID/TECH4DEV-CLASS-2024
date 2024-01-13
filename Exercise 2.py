#Exercise 2 

#1
"""   Write a program that finds the maximum value of the given list, assuming that the list
contains at least one element."""

# Define the list
numbers = [2, 4, 7, 4, 23, 5, 1, 4, 8, 9]

# Find the maximum value in the list using the max() function
max_value = max(numbers)

# Display the maximum value
print("The maximum value in the list is:", max_value)

#2
""""" Write a python program that calculates the average value of the given list.
Try your program with the following list
4 7 1 5 11 53 12 46 84 23"""

# Define the list
numbers = [4, 7, 1, 5, 11, 53, 12, 46, 84, 23]

# Calculate the average value
average = sum(numbers) / len(numbers)

# Display the average value
print("The average value of the list is:", average)

#3
""" Write a program that prints the given list of integers in reverse order.
Try your program with the following list
2 6 7 45 23 53 14 45 89 5 """

# Define the list
numbers = [2, 6, 7, 45, 23, 53, 14, 45, 89, 5]

# Print the list in reverse order
print("Original list:", numbers)
print("List in reverse order:", numbers[::-1])

#4
"""Write a program that accepts two lists of integers and prints true if each element in the first 
list is less than the element at the same index in the second list. Your program should print 
false if the lists are not the same length."""
def compare_lists(list1, list2):
    # Check if the lists are of the same length
    if len(list1) != len(list2):
        return False  # Lists are not of the same length, return False
    
    # Iterate through the lists and compare elements at the same index
    for i in range(len(list1)):
        if list1[i] >= list2[i]:
            return False  # If any element in list1 is not less than or equal to the element at the same index in list2, return False
    
    return True  # All elements in list1 are less than the elements at the corresponding indices in list2

# Accept two lists of integers from the user
list1 = list(map(int, input("Enter elements of the first list separated by space: ").split()))
list2 = list(map(int, input("Enter elements of the second list separated by space: ").split()))

# Call the function and print the result
result = compare_lists(list1, list2)
print("Result:", result)

#5
""" Write a program that accepts a list of integers and two indexes and swaps the elements at 
those indexes """
def swap_elements(lst, index1, index2):
    # Check if the indexes are within the range of the list
    if 0 <= index1 < len(lst) and 0 <= index2 < len(lst):
        # Swap the elements at the specified indexes
        lst[index1], lst[index2] = lst[index2], lst[index1]
        print("Elements swapped successfully.")
    else:
        print("Invalid indexes. Indexes should be within the range of the list.")

# Accept a list of integers from the user
numbers = list(map(int, input("Enter elements of the list separated by space: ").split()))

# Accept two indexes from the user
index1 = int(input("Enter the first index to swap: "))
index2 = int(input("Enter the second index to swap: "))

# Call the function to swap elements at the specified indexes
swap_elements(numbers, index1, index2)

# Display the updated list after swapping
print("Updated list:", numbers)

#6
"""Write a program that accepts two lists of integers and prints a new list containing all 
elements of the first list followed by all elements of the second."""
def merge_lists(list1, list2):
    # Concatenate the two lists using the '+' operator
    merged_list = list1 + list2
    return merged_list

# Accept two lists of integers from the user
list1 = list(map(int, input("Enter elements of the first list separated by space: ").split()))
list2 = list(map(int, input("Enter elements of the second list separated by space: ").split()))

# Call the function to merge the lists
result_list = merge_lists(list1, list2)

# Display the merged list
print("Merged list:", result_list)

#7
"""Write a program that accepts a list of integers and an integer value as its parameters and 
prints the last index at which the value occurs in the list. The program should print –1 if the 
value is not found. For example, in the list [74, 85, 102, 99, 101, 85, 56], the last index of the 
value 85 is 5"""
def find_last_index(lst, value):
    # Reverse the list and find the index of the value
    reversed_list = lst[::-1]
    if value in reversed_list:
        last_index = len(lst) - 1 - reversed_list.index(value)
        return last_index
    else:
        return -1  # Value not found in the list

# Accept a list of integers from the user
numbers = list(map(int, input("Enter elements of the list separated by space: ").split()))

# Accept an integer value to search
search_value = int(input("Enter the value to find its last index: "))

# Call the function to find the last index of the value
last_index = find_last_index(numbers, search_value)

# Display the last index of the value in the list
print(f"The last index of {search_value} is {last_index}")

#8
""" Write a program that prints the range of values in a list of integers. The range is defined as 1 
more than the difference between the maximum and minimum values in the list. For 
example, if a list contains the values [36, 12, 25, 19, 46, 31, 22], the program should return 
35. You may assume that the list has at least one element"""

def find_last_index(lst, value):
    # Reverse the list and find the index of the value
    reversed_list = lst[::-1]
    if value in reversed_list:
        last_index = len(lst) - 1 - reversed_list.index(value)
        return last_index
    else:
        return -1  # Value not found in the list

# Accept a list of integers from the user
numbers = list(map(int, input("Enter elements of the list separated by space: ").split()))

# Accept an integer value to search
search_value = int(input("Enter the value to find its last index: "))

# Call the function to find the last index of the value
last_index = find_last_index(numbers, search_value)

# Display the last index of the value in the list
print(f"The last index of {search_value} is {last_index}")

#9
"""Write a program that accepts a list of integers, a minimum value, and a maximum value and 
prints the count of how many elements from the list fall between the minimum and 
maximum (inclusive). For example, in the list [14, 1, 22, 17, 36, 7, -43, 5], for minimum value 
4 and maximum value 17, there are four elements whose values fall between 4 and 17."""

def count_elements_within_range(lst, min_val, max_val):
    count = sum(1 for num in lst if min_val <= num <= max_val)
    return count

# Example list of integers
numbers = [14, 1, 22, 17, 36, 7, -43, 5]

# Minimum and maximum values for the range
minimum_value = 4
maximum_value = 17

# Count elements within the specified range
count_elements = count_elements_within_range(numbers, minimum_value, maximum_value)

# Print the count of elements within the range
print(f"There are {count_elements} elements between {minimum_value} and {maximum_value} (inclusive) in the list.")

#10
"""Write a program that accepts a list of real numbers and prints true if the list is in sorted 
(nondecreasing) order and false otherwise. For example, if lists named list1 and list2 store 
[16.1, 12.3, 22.2, 14.4] and [1.5, 4.3, 7.0, 19.5, 25.1, 46.2] respectively, the program should 
print false for list1 and true for list2 respectively. Assume the list has at least one element. A 
one-element list is sorted"""

def is_sorted(lst):
    # Check if the list is in non-decreasing order
    return all(lst[i] <= lst[i + 1] for i in range(len(lst) - 1))

# Example lists of real numbers
list1 = [16.1, 12.3, 22.2, 14.4]
list2 = [1.5, 4.3, 7.0, 19.5, 25.1, 46.2]

# Check if list1 is sorted and print the result
result_list1 = is_sorted(list1)
print("Is list1 sorted?", result_list1)

# Check if list2 is sorted and print the result
result_list2 = is_sorted(list2)
print("Is list2 sorted?", result_list2)






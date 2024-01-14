#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# print("\ta\tb\tc") 


# In[2]:


print("\\\\")


# In[3]:


print("'")


# In[2]:


print("\"\"\"")


# In[5]:


print("C:\nin\the downward spiral")


# In[6]:


print(print("/ \\ // \\\\ /// \\\\\\")
)


# In[8]:


print('''This quote is from Irish poet Oscar Wilde:
"Music makes one feel so romantic

- at least it always gets on one's nerves – which is the same thing nowadays."''')


# In[11]:


(print('A "quoted" String is \'much\' better if you learn\nthe rules of "escape sequences." Also, "" represents an empty String. Don\'t forget: use \\" instead of " ! \'\' is not the same as "')
)


# In[13]:



9 / 5


# In[14]:



695 % 20


# In[15]:


7 + 6 * 5


# In[16]:


7 * 6 + 5


# In[17]:


248 % 100 / 5


# In[18]:


6 * 3 - 9 / 4


# In[19]:


(5 - 7) * 4


# In[20]:


6 + (18 % (17 - 12))


# In[32]:


# Number of rows for the pattern
num_rows = 8

# Loop to print the pattern
for i in range(num_rows):
    if i == 0 or i == num_rows - 1:
        print("+----+")
    else:
        if i % 2 == 1:
            print("\\ /")
        else:
            print("/ \\")


# In[3]:


def print_pattern(rows, columns):
    for i in range(rows):
        for j in range(columns):
            print("*", end="")
        print()  # Move to the next line after printing each row

# Set the values for rows and columns
rows = 5
columns = 10

# Call the function to print the pattern
print_pattern(rows, columns)


# In[4]:


for i in range(1, 7):
    # your code here
    a = i
    b = i * 2
    c = i * 11 - 7
    d = 10 - i * 2
    e = 2 * i - 1
    f = 93 + i
    g = 12 - i * 2

    print(f"{a} {b} {c} {d} {e} {f} {g}")


# In[6]:


class NumberPyramid:
    NUM_LINES = 7

    @classmethod
    def print_pyramid(cls):
        for i in range(1, cls.NUM_LINES + 1):
            line = str(i) * i
            print(line)

# Call the method to print the pyramid
NumberPyramid.print_pyramid()


# In[7]:


def pay(hourly_rate, hours_worked):
    normal_hours = 8
    overtime_multiplier = 1.5

    if hours_worked <= normal_hours:
        total_pay = hourly_rate * hours_worked
    else:
        normal_pay = hourly_rate * normal_hours
        overtime_pay = hourly_rate * overtime_multiplier * (hours_worked - normal_hours)
        total_pay = normal_pay + overtime_pay

    return total_pay

# Example usage:
salary = pay(5.50, 6)
print(salary)  # Output: 33.0

salary_overtime = pay(4.00, 11)
print(salary_overtime)  # Output: 50.0


# In[8]:


import math

# Function to calculate the area of a circle
def area(radius):
    return math.pi * radius ** 2

# Example usage:
radius = 2.0
circle_area = area(radius)
print(circle_area)


# In[9]:


low = int(input("low? "))
high = int(input("high? "))
sum = 0

for i in range(low, high):
    sum += i

print("sum =", sum)


# In[11]:


low = int(input("low? "))
high = int(input("high? "))
sum = 0

for i in range(low, high):
    sum += i

print("sum =", sum)


# def printRange(start, end):
#     if start < end:
#         # Increasing sequence
#         for num in range(start, end + 1):
#             print(num, end=" ")
#     elif start > end:
#         # Decreasing sequence
#         for num in range(start, end - 1, -1):
#             print(num, end=" ")
#     else:
#         # Numbers are the same
#         print(start)
# 
# # Example calls to printRange
# printRange(2, 7)
# printRange(19, 11)
# printRange(5, 5)
# 

# In[14]:


def smallestLargest():
    # Ask the user for the number of numbers to enter
    num_of_numbers = int(input("How many numbers do you want to enter? "))

    # Initialize variables for smallest and largest
    smallest = float('inf')  # Set to positive infinity initially
    largest = float('-inf')  # Set to negative infinity initially

    # Loop to get user input for each number
    for i in range(1, num_of_numbers + 1):
        num = float(input(f"Number {i}: "))
        smallest = min(smallest, num)
        largest = max(largest, num)

    # Output the smallest and largest numbers
    print(f"Smallest = {smallest}")
    print(f"Largest = {largest}")

# Call the method
smallestLargest()


# In[15]:


def printAverage():
    total = 0.0
    count = 0

    while True:
        num = float(input("Type a number: "))

        if num < 0:
            break  # Exit the loop if a negative number is entered

        total += num
        count += 1

    if count > 0:
        average = total / count
        print(f"Average was {average:.1f}")
    else:
        print("No nonnegative numbers were entered.")

# Call the method
printAverage()


# In[16]:


def numUnique(num1, num2, num3):
    unique_numbers = {num1, num2, num3}
    return len(unique_numbers)

# Example usage:
result1 = numUnique(18, 3, 4)
print(result1)  # Output: 3

result2 = numUnique(6, 7, 6)
print(result2)  # Output: 2


# In[17]:


import random

def roll_dice():
    return random.randint(1, 6)

def main():
    target_sum = 7
    tries = 0

    while True:
        dice1 = roll_dice()
        dice2 = roll_dice()

        total = dice1 + dice2
        tries += 1

        print(f"{dice1} + {dice2} = {total}")

        if total == target_sum:
            print(f"You won after {tries} tries!")
            break

if __name__ == "__main__":
    main()


# In[18]:


# Given list
numbers = [2, 4, 7, 4, 23, 5, 1, 4, 8, 9]

# Find the maximum value in the list
max_value = max(numbers)

# Print the result
print("The maximum value is:", max_value)


# In[21]:


# Given list
numbers = [4, 7, 1, 5, 11, 53, 12, 46, 84, 23]

# Calculate the average value
average_value = sum(numbers) / len(numbers)

# Print the result
print("The average value is:", average_value)



# In[22]:


# Given list
numbers = [2, 6, 7, 45, 23, 53, 14, 45, 89, 5]

# Print the reversed list
print("Original list:", numbers)
print("Reversed list:", numbers[::-1])


# In[23]:


def compare_lists(list1, list2):
    if len(list1) != len(list2):
        print("False (Lists are not the same length)")
    else:
        result = all(x < y for x, y in zip(list1, list2))
        print(result)

# Example usage:
list_a = [2, 6, 7, 4, 9]
list_b = [5, 8, 10, 6, 12]
compare_lists(list_a, list_b)

list_c = [2, 6, 7, 4, 9]
list_d = [5, 8, 10, 6, 12, 15]
compare_lists(list_c, list_d)


# In[1]:


def swap_elements(lst, index1, index2):
    if 0 <= index1 < len(lst) and 0 <= index2 < len(lst):
        lst[index1], lst[index2] = lst[index2], lst[index1]
        print("List after swapping:", lst)
    else:
        print("Invalid indexes")

# Example usage:
try:
    # Accept a list of integers from the user
    my_list = [int(x) for x in input("Enter a list of integers separated by space: ").split()]

    # Accept two indexes from the user
    index1 = int(input("Enter the first index: "))
    index2 = int(input("Enter the second index: "))

    # Swap elements at the provided indexes
    swap_elements(my_list, index1, index2)

except ValueError:
    print("Invalid input. Please enter valid integers.")


# In[33]:


def last_index_of_value(lst, value):
    try:
        last_index = len(lst) - 1 - lst[::-1].index(value)
        print(f"The last index of {value} is:", last_index)
    except ValueError:
        print(f"{value} is not found in the list. The last index is -1.")

my_list = [74, 85, 102, 99, 101, 85, 56]
search_value = 85

# Find the last index of the value
last_index_of_value(my_list, search_value)


# In[34]:


def calculate_range(lst):
    min_value = min(lst)
    max_value = max(lst)
    value_range = max_value - min_value + 1
    print("The range of values in the list is:", value_range)

my_list = [36, 12, 25, 19, 46, 31, 22]

# Calculate and print the range
calculate_range(my_list)


# In[35]:


def count_elements_between(lst, min_value, max_value):
    count = sum(1 for num in lst if min_value <= num <= max_value)
    print(f"The count of elements between {min_value} and {max_value} is:", count)

my_list = [14, 1, 22, 17, 36, 7, -43, 5]
min_value = 4
max_value = 17

# Count and print the elements between min and max
count_elements_between(my_list, min_value, max_value)


# In[36]:


def is_sorted(lst):
    sorted_order = all(lst[i] <= lst[i+1] for i in range(len(lst)-1))
    print("The list is in sorted order:", sorted_order)

list1 = [16.1, 12.3, 22.2, 14.4]
list2 = [1.5, 4.3, 7.0, 19.5, 25.1, 46.2]

# Check and print if the lists are in sorted order
is_sorted(list1)
is_sorted(list2)


# In[ ]:





# 

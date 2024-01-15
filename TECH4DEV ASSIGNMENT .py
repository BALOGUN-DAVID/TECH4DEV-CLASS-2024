#!/usr/bin/env python
# coding: utf-8

# # EXERCISE 1
# 

# #### QUESTION 1

# In[2]:


print (" \ta\tb\tc")


# In[3]:


print("\\\\")


# In[4]:


print("'")


# In[5]:


print("\"\"\"")


# In[6]:


print("C:\nin\the downward spiral")


# #### QUESTION 2 

# In[67]:


print ("/ " "\\ " "// " "\\\\ " "/// " "\\\\\\") 


# #### QUESTION 3

# In[68]:


print ("""

This quote is from \nIrish poet Oscar Wilde: \n"Music makes one feel so romantic
- at least it always gets on one's nerves - \nwhich is the same thing nowadays."

""")


# #### QUESTION 4 

# In[47]:


print ("""
A "quoted" String is \n'much' better if you learn \nthe rules of "escape sequences." 
Also, "" represents an empty String. \nDon't forget: use \" instead of " ! \n'' is not the same as "

""")


# #### QUESTION 5 

# In[48]:


print (9 / 5)


# In[49]:


print (695 % 20)


# In[50]:


print (7 + 6 * 5)


# In[51]:


print (7 * 6 + 5)


# In[52]:


print (248 % 100 / 5)


# In[53]:


print (6 * 3 - 9 / 4)


# In[54]:


print ((5 - 7) * 4)


# In[55]:


print (6 + (18 % (17 - 12)))


# # EXERCISE 2
# 

# #### QUESTION 1 

# In[2]:


numbers = [2, 4, 7, 4, 23, 5, 1, 4, 8, 9]

# to get the maximum value
maximum_value = max (numbers)

print (maximum_value)


# #### QUESTION 2 

# In[10]:


values = [4, 7, 1, 5, 11, 53, 12, 46, 84, 23]

# to get the average value
average_value = sum (values) / len (values)

print (average_value)

# to round to whole number

whole_average_value = round(average_value)

print (whole_average_value)


# #### QUESTION 3 

# In[270]:


values =  [2, 6, 7, 45, 23, 53, 14, 45, 89, 5]

values.reverse()

values


# #### QUESTION 4 

# In[ ]:


# Get input from the user as a string
input_string_1 = input("Enter a list of numbers separated by spaces: ")
input_string_2 = input("Enter a list of numbers separated by spaces: ")

# Convert the input string to a list of numbers
list_1 = [int(num) for num in input_string_1.split()]
list_2 = [int(num) for num in input_string_2.split()]

print (list_1, list_2)

# to check if list 1 is less than list 2
if len(list_1) != len (list_2):
        print ("False")
else:
    for i in range(len(list_2)):
        if list_1[i] <= list_2[i]:
            print ("True")
        else:
            print ("False")

        


# #### QUESTION 5 

# In[435]:


input_string = input("Enter a list of integers separated by spaces: ")

# Convert the input string to a list of numbers
list_of_numbers = [int(num) for num in input_string.split()]

# to get the indexes to swap
index1 = int(input("Enter the first index: "))
index2 = int(input("Enter the second index: "))

# to check if indices are valid
if 0 <= index1 < len(user_list) and 0 <= index2 < len(user_list):
    # swap the elements at index1 and index2
    list_of_numbers[index1], list_of_numbers[index2] = list_of_numbers[index2], list_of_numbers[index1]
    print(f"List after swapping indices {index1} and {index2}: {list_of_numbers}")
else:
    print("Invalid input. Please try again.")


# #### QUESTION 6

# In[436]:


input_string_1 = input("Number 1: Enter a list of numbers separated by spaces: ")
input_string_2 = input("Number 2: Enter a list of numbers separated by spaces: ")

# Convert the input string to a list of numbers
list_number_1 = [float(num) for num in input_string_1.split()]
list_number_2 = [float(num) for num in input_string_2.split()]

# to join both lists
new_list = list_number_1 + list_number_2
print (f"The new list is: {new_list}")


# #### QUESTION 7

# In[446]:


input_string = input("Enter a list of integers separated by spaces: ")
numbers = [int(num) for num in input_string.split()]

# to get the value to search for in the list
search_value = int(input("Enter the value to find: "))

last_index = -1  

# to find the last index of the specified value
for i in range(len(numbers)):
    if numbers[i] == search_value:
        last_index = i

if last_index != -1:
    print(f"The last index of {search_value} is: {last_index}")
else:
    print("-1")



# #### QUESTION 8

# In[356]:


input_string = input(" Enter a list of numbers separated by spaces: ")

# Convert the input string to a list of numbers
list_value = [float(num) for num in input_string.split()]
print (list_value)

# to get the range of the list
range_of_list = (max (list_value) - min (list_value)) + 1
print (range_of_list)


# #### QUESTION 9

# In[392]:


input_string = input(" Enter a list of numbers separated by spaces: ")

maximum_value = int(input("Enter the maximum value: "))

minimum_value = int(input("Enter the minimum value: "))

# Convert the input string to a list of numbers
list_of_integers = [int(num) for num in input_string.split()]
print (list_of_integers)

# to count the values
count_values = 0

# to check for numbers that fall under the range of minimum and maximum value
for num in list_of_integers:
    if num >= minimum_value and num <= maximum_value:
        num 
        print (num)
        count_values += 1
        
print ("Elements that falls under the minimum and maximum value are:", count_values)


# #### QUESTION 10

# In[427]:


input_string = input(" Enter a list of numbers separated by spaces: ")

numbers = [float(num) for num in input_string.split()]

is_ascending = True 

# to check the list if it is ascending / descending 
for i in range(len(numbers) - 1):
    if numbers[i] > numbers[i + 1]:
        is_ascending = False
        break 

print (is_ascending)
        


# # EXERCISE 3

# #### QUESTION 1

# In[12]:


for i in range (0, 8):
    if i == 0 or i == 7:
        print ("+----+")
    elif i == 1 or i == 3 or i == 5:
        print ("\  /")
    elif i == 2 or i == 4 or i == 6:
        print ("/  \\")
               
               
            


# #### QUESTION 2 

# In[13]:


for i in range (0,7):
    print ("**********")


# #### QUESTION 3 

# In[14]:


for i in range (1, 7):
    i += 0
    print (i)


# In[18]:


for i in range (1, 7):
    i *= 2
    print (i)


# In[19]:


for i in range (1, 7):
    i *= 4
    print (i)


# In[47]:


x = 40
j = 10
for i in range (1, 7):
    x-=j
    print (x)


# In[52]:


x = -11
j = -4
for i in range (1, 7):
    x-=j
    print (x)


# In[56]:


x = 100
j = 3
for i in range (1, 7):
    x-=j
    print (x)


# In[76]:


x = -4

for i in range (1, 7):
    print (x)
    x += (18)
   
    
    


# #### QUESTION 4

# In[77]:


for i in range (0, 8):
    for j in range (i):
        print (i, end = " ")
    print ()


# #### QUESTION 5 

# In[134]:


class pay:
    def multiply (self, num_1, num_2):
        if num_2 > 8:
            payment = (num_1 * (1.5) * (num_2 - 8) + (num_1 * 8))
            print (payment)
        else:
            payment = (num_1 * num_2)
            print (payment)


x = pay()
y = x.multiply(4, 11)
print (y)


# #### QUESTION 6

# In[129]:


import math 

class area:
    def calculate_area (self, radius):
        return math.pi * (radius ** 2)

x = area()
y = x.calculate_area(2)
print (y)


# #### QUESTION 7 

# In[119]:


low = int(input("Enter the value? "))
high = int(input("Enter the value? "))
sum = 0
for i in range(low, high):
    sum += i
    
print ("sum = ", sum)


# #### QUESTION 8

# In[246]:


total_sum = 0
user_input = None

while user_input != 0:
    user_input = int(input("Enter a number: "))
    total_sum += user_input

print(f"The sum of the entered numbers is: {total_sum}")


# #### QUESTION 9 

# In[247]:


total_sum = 0
user_input = None

while user_input != -1:
    user_input = int(input("Enter a number: "))
    total_sum += user_input

print(f"The sum of the entered numbers is: {total_sum}")


# #### QUESTION 10

# In[249]:


def repl (string, number):
    if number > 0:
        x = string * number
        print (x)
    else:
        print ()

repl ("hello", 5)


# #### QUESTION 11

# In[ ]:


def printRange(num_1, num_2):
    if num_1 < num_2:
        for x in range(num_1, num_2 + 1):
            print(x, end=" ")
    elif num_1 > num_2:
        for x in range(num_1, num_2 - 1, -1):
            print(x, end=" ")
    elif num_1 == num_2:
            print (num_1)


printRange(19, 11)


# #### QUESTION 12

# In[311]:


def get_smallest_and_largest():
    num_of_numbers = int(input("Enter the number of numbers you want to input: "))
    while num_of_numbers <= 0:
        print("Please enter a valid number greater than 0.")
        num_of_numbers = int(input("Enter the number of numbers you want to input: "))

    smallest = float('inf') 
    largest = float('-inf')  
    
   
    for i in range(num_of_numbers):
        current_number = float(input("Enter a number: "))
        smallest = min(smallest, current_number)
        largest = max(largest, current_number)

    print("smallest:", smallest)
    print("largest:", largest)


get_smallest_and_largest()
    


# #### QUESTION 13

# In[266]:


def printAverage (prompt="Enter a number"):

    total_sum = 0
    count = 0
    user_input = 1

    while user_input >= 0:  
        user_input = float(input("Enter a number : "))
    
    
        if user_input >= 0:
            total_sum += user_input 
            count += 1

    average = total_sum / count    
    print (average)
    
printAverage()


# #### QUESTION 14

# In[ ]:


def numUnique (num_1, num_2, num_3):
    if num_1 == num_2 and num_2 == num_3 and num_3 == num_1:
        print (0)
    elif num_1 == num_2 and num_1 != num_3:
            print (2)
    elif num_1 != num_2 and num_1 == num_3:
        print (2)
    elif num_1 != num_2 and num_2 == num_3:
        print (2)
    elif num_1 != num_2 and num_2 != num_3 and num_3 != num_1:
        print (3)
        
numUnique (6, 4, 6)


# #### QUESTION 15

# In[451]:


import random

def dice_rolling():
    return random.randint(1, 6)

def simulate_dice_rolling():
    rolls_count = 0

    while True:
        dice1 = roll_dice()
        dice2 = roll_dice()
        total = dice1 + dice2

        print(f"Roll {rolls_count + 1}: {dice1} + {dice2} = {total}")

        if total == 7:
            break

        rolls_count += 1

    print(f"It took {rolls_count + 1} rolls to get a sum of 7.")

# Run the simulation
simulate_dice_rolling()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





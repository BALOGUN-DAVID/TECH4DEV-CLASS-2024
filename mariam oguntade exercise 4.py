#!/usr/bin/env python
# coding: utf-8

# Write a program to produce the following output using for loop
# +----+
# \ /
# / \
# \ /
# / \
# \ /
# / \
# +----+

# In[93]:


# Number of iterations for the for loop
iterations = 5

# Print the top of the box
print("+----+")

# Use a for loop to print the pattern inside the box
for _ in range(iterations):
    print("\\ /")
    print("/ \\")

# Print the bottom of the box
print("+----+")


# Write a program to produce the following output using for loop
# ""**********
# **********
# **********
# **********
# *********""

# In[94]:


for i in range (5):
    print('**********')


# Complete the code for the following for loop:
# for in range(1,7):
#  //your code here
# so that it prints the following numbers, one per line

# In[10]:


for i in range(1,7):
    print(i)


# In[11]:


for i in range(1,7):
    print(i*2)


# In[16]:


for i in range(4,80,15):
    print(i)


# In[31]:


for i in range(30,-21,-10):
    print(i)


# In[32]:


for i in range(-7,14,4):
    print(i)


# In[39]:


for i in range(97,80,-3):
    print(i)


# In[40]:


for i in range(-4,86,18):
    print(i)


# Write a program to produce the following output using for loops. Then 
# use a class constant to make it possible to change the number of lines in 
# the figure.
# 1
# 22
# 333
# 4444
# 55555
# 666666
# 7777777

# In[ ]:


class NumberTriangle:
    # Class constant to define the number of lines
    LINES = 7

    def print_triangle(self):
        for i in range(1, self.LINES + 1):
            for j in range(i):
                print(i, end="")
            print()

# Create an instance of the class and print the triangle
triangle = NumberTriangle()
triangle.print_triangle()


# Write a method named pay that accepts two parameters: a real number 
# for a TA's salary, and an integer for the number of hours the TA worked 
# this week. The method should return how much money to pay the TA. 
# For example, the call 
# pay(5.50, 6)
# should return 
# 33.0. 
# The TA should receive "overtime" pay of 1 ½ normal salary for any hours 
# above 8. For example, the call pay(4.00, 11) should return (4.00 * 
# 8) + (6.00 * 3) or 50.0.

# In[56]:


def pay(salary, hours):
    if hours <= 8:
        reward = salary*hours
    else:
        overtime = (salary*hours) + (1.5*salary)
        return overtime
    return reward
pay(4.0,9)


# Consider the following method for converting milliseconds into days:
# // converts milliseconds to days
# def toDays(millis):
#  return millis / 1000.0 / 60.0 / 60.0 / 24.0
# Write a similar method named area that takes as a parameter the radius of 
# a circle and that returns the area of the circle. For example, the call 
# area(2.0);
# should return 
# 12.566370614359172. 
# Recall that area can be computed as π times the radius squared and that 
# Python has a constant called math.pi

# In[63]:


def area(radius):
    import math
    result = math.pi * (radius**2)
    return result

area(2.0)
    


# Copy and paste the following code into pythons IDLE script 
# environment.
#  low = 1
#  high = 1001
#  sum = 0
#  for i in range(low,high):
#  sum += i
#  
#  print("sum = " , sum)
#  
# Modify the code to use a input to prompt the user for the values of low
# and high. Below is a sample execution in which the user asks for the same 
# values as in the original program (1 through 1000):
# low? 1
# high? 1001
# sum = 500500
# Below is an execution with different values for low and high:
# low? 300
# high? 5298
# sum = 13986903
# You should exactly reproduce this format

# In[ ]:


low = int(input("low? "))
high = int(input("high? "))
sum = 0

for i in range(low, high):
    sum += i

print("sum =", sum)


# Write a program using while loop that prompts the user for numbers until 
# the user types 0, then outputs their sum

# In[90]:


# Initialize sum and get the first input
sum_of_numbers = 0
number = int(input("Enter a number (0 to stop): "))

# Continue the loop until the user enters 0
while number != 0:
    sum_of_numbers += number
    number = int(input("Enter a number (0 to stop): "))

# Print the sum of the entered numbers
print("Sum of the entered numbers:", sum_of_numbers)


# Write a program using while loop that prompts the user for numbers until 
# the user types -1, then outputs their sum.

# In[ ]:


# Initialize sum and get the first input
sum_of_numbers = 0
number = int(input("Enter a number (-1 to stop): "))

# Continue the loop until the user enters -1
while number != -1:
    sum_of_numbers += number
    number = int(input("Enter a number (-1 to stop): "))

# Print the sum of the entered numbers
print("Sum of the entered numbers:", sum_of_numbers)


# Write a method named repl that accepts a String and a number of 
# repetitions as parameters and returns the String concatenated that many 
# times. For example, the call repl("hello", 3) returns "hellohellohello". 
# If the number of repetitions is 0 or less, an empty string is returned.

# In[ ]:


def rep1(string,no):
    result = string * no
    if no <= 0:
        return ""
    return result

rep1('hello', 3)


# Write a method called printRange that accepts two integers as arguments and 
# prints the sequence of numbers between the two arguments, separated by 
# spaces. Print an increasing sequence if the first argument is smaller than 
# the second; otherwise, print a decreasing sequence. If the two numbers 
# are the same, that number should be printed by itself. Here are some 
# sample calls to printRange: 
# printRange(2, 7)
# printRange(19, 11)
# printRange(5, 5)
# The output produced should be the following: 
# 2 3 4 5 6 7 
# 19 18 17 16 15 14 13 12 11 
# 5

# In[ ]:


def printRange(num1, num2):
    if num1 < num2:
        for i in range (num1, num2+1):
            print(i)
    elif num1 > num2:
        for i in range (num1, num2-1, -1):
            print(i)
    elif num1 == num2:
        print(num1)
            
printRange(10,10)
            


# Write a method named smallestLargest that asks the user to enter numbers, 
# then prints the smallest and largest of all the numbers typed in by the 
# user. You may assume the user enters a valid number greater than 0 for 
# the number of numbers to read. Here is an example dialogue: 
# How many numbers do you want to enter? 4
# Number 1: 5
# Number 2: 11
# Number 3: -2
# Number 4: 3
# Smallest = -2
# Largest = 11

# In[155]:


def smallestLargest():
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
    max = np.max(user)
    print(f'Smallest = {min}')
    print(f'Largest = {max}')

      
smallestLargest()


# Write a method called printAverage that uses a sentinel loop to 
# repeatedly prompt the user for numbers. Once the user types any number 
# less than zero, the method should display the average of all nonnegative 
# numbers typed. Display the average as a double. Here is a sample 
# dialogue with the user:
# Type a number: 7
# Type a number: 4
# Type a number: 16
# Type a number: –4
# Average was 9.0
# If the first number that the user types is negative, do not print an average:
# Type a number: –2

# In[4]:


def printAverage():
    import numpy as np
    user = []
    prompt = 1
    while prompt > 0:
        num = int(input(f"Type a number "))
        if num > 1:
            user.append(num)
            prompt = prompt + 1
        elif num < 0:
            prompt = 0
            
            
            
        if prompt == 0:    
            avg = np.mean(user)
            print('The average is ',avg)

            
        
printAverage()


# Write a method named numUnique that takes three integers as parameters 
# and returns the number of unique integers among the three. For example, 
# the call numUnique(18, 3, 4) should return 3 because the parameters 
# have three different values. By contrast, the call numUnique(6, 7, 6)
# should return 2 because there are only two unique numbers among the 
# three parameters: 6 and 7

# In[6]:


def numUnique(num1, num2, num3):
    unique_numbers = set([num1, num2, num3])
    return len(unique_numbers)

# Example :
result = numUnique(18, 3, 4)
print(result)  

result = numUnique(6, 7, 6)
print(result)  


# .A Random object generates pseudo-random numbers. Find out how to 
# use the Random class and write a program that simulates rolling of two 6-
# sided dice until their combined result comes up as 7. One possible output 
# can be seen as below:
#  2 + 4 = 6
# 3 + 5 = 8
# 5 + 6 = 11
# 1 + 1 = 2
# 4 + 3 = 7
# You won after 5 tries

# In[7]:


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
            print(f"You won after {tries} tries")
            break

if __name__ == "__main__":
    main()


# In[8]:


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
            print(f"You won after {tries} tries")
            break

if __name__ == "__main__":
    main()


# In[ ]:





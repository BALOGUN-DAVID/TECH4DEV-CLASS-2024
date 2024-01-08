#!/usr/bin/env python
# coding: utf-8

# # EXERCISE 1

# 1.What is the output of the following print statements?
# a) print("\ta\tb\tc")

# In[1]:


print("\ta\tb\tc") #'\t' means tab on your computer keyboard


# b)print("\\\\")

# In[2]:


print("\\\\")


# c)print("'")

# In[3]:


print("'")


# d)print("\"\"\"")

# In[4]:


print("\"\"\"") #the '\' is an 'escape charater',used to tell the program that you statement still continues


# e)print("C:\nin\the downward spiral")

# In[5]:


print("C:\nin\the downward spiral") #'\n' means 'NEW LINE',i.e, you are inserting an new line


# 2.Write a print statement to produce this output:
# / \ // \\ /// \\\
# 

# In[21]:


print('/ \\ // \\\\ /// \\\\\\') #each "\" 'escape character' goes with another \ to produce the other, so three \\\, goes with six \\\\\\ to produce the three\\\"


# 3.What print statements will generate this output?
# This quote is from 
# Irish poet Oscar 
# Wilde:
# "Music makes one feel so romantic
# - at least it always gets on one's nerves – 
# which is the same thing nowadays."
# 

# In[63]:


print('This quote is from \nIrish poet Oscar\nWilde:\n"Music makes one feel so romantic\n- at least it always gets on one\'s nerves -\nwhich is the same thing nowadays."')
#here, we apply the new line function and escape character


# 4.What print statements will generate this output?
# A "quoted" String is 
# 'much' better if you 
# learn
# the rules of "escape sequences." 
# Also, "" represents an empty String. 
# Don't forget: use \" instead of " ! 
# '' is not the same as "
# 

# In[70]:


print('A "quoted" String is\n\'much\' better if you\nlearn\nthe rules of "escape sequences."\nAlso,"" represents an empty String.\nDon\'t forget: use \\" instead of " !\n\'\'is not the same as "')


# 5.What values result from the following expressions?
# –	9 / 5
# –	695 % 20 
# –	7 + 6 * 5
# –	7 * 6 + 5
# –	248 % 100 / 5
# –	6 * 3 - 9 / 4
# –	(5 - 7) * 4
# –	6 + (18 % (17 - 12))

# In[54]:


9/5


# In[55]:


698%20 #What is the remainder when 698 is divided by 20


# In[57]:


7+6*5 #python uses BODMAS for mathematical expressions


# In[58]:


7*6+5


# In[59]:


248%100/5 


# In[60]:


6*3-9/4


# In[61]:


(5-7)*4


# In[62]:


6+(18%(17-12))


# # EXCERCISE 4.1

# 1. Write a program to produce the following output using for loop
# +----+
# \ /
# / \
# \ /
# / \
# \ /
# / \
# +----+

# In[76]:


print('+-------+')
for number in range(3):
    print('\n\\\t/\n\n/\t\\\n')
print('+-------+')
    


# 2. Write a program to produce the following output using for loop
# **********
# **********
# **********
# **********
# **********

# In[80]:


for number in range(5):
    print('**********')


# 3. Complete the code for the following for loop:
# for in range(1,7):
#       //your code here
# so that it prints the following numbers, one per line:
# 
# a) 1 b) 2 c) 4 d) 30 e) -7 f) 97 g) -4
#    2    4    19   20    -3    94    14
#    3    6    34   10     1    91    32
#    4    8    49   0      5    88    50
#    5    10   64  -10     9    85    68
#    6    12   79  -20    13    82    86

# In[73]:


print('\t\t\n')
for a in range (1,7):
    print(a,end='\t')
    
print('\t\t\n')
for b in range(2,13,2):
    print(b,end='\t')
    
print('\t\t\n')
for c in range(4,80,15):
    print(c,end='\t')
    
print('\t\t\n')
for d in range(30,-21,-10):
    print(d,end='\t')
    
print('\t\t\n')
for e in range(-7,14,4):
    print(e,end='\t')
    
print('\t\t\n')
for f in range(97,80,-3):
    print(f,end='\t')
    
print('\t\t\n')
for g in range(-4,87,18):
    print(g,end='\t')


# 4.Write a program to produce the following output using for loops. Then  use a class constant to make it possible to change the number of lines in  the figure. 
# 1 
# 22 
# 333 
# 4444 
# 55555 
# 666666 
# 7777777
# 

# In[95]:


for a in range(1,8):
    for b in range(1,a+1):
        print(a, end=" ")
    print()


# 5.Write a method named pay that accepts two parameters: a real number  for a TA's salary, and an integer for the number of hours the TA worked  this week. The method should return how much money to pay the TA.  For example, the call  
# pay(5.50, 6) 
# should return  
# 33.0.  
# The TA should receive "overtime" pay of 1 ½ normal salary for any hours  above 8. For example, the call pay(4.00, 11) should return (4.00 *  8) + (6.00 * 3) or 50.0. 
# 

# In[1]:


def pay(salary, hours_worked):
    regular_hours = min(8, hours_worked)
    overtime_hours = max(0, hours_worked - 8)

    regular_pay = salary * regular_hours
    overtime_pay = salary * 1.5 * overtime_hours

    total_pay = regular_pay + overtime_pay
    return total_pay

# Example
output = pay(5.50, 6)
print(output)  # Output: 33.0

output1 = pay(4.00, 11)
print(output1)  # Output: 50.0


# 6.Consider the following method for converting milliseconds into days: 
# // converts milliseconds to days 
# def toDays(millis): 
#  return millis / 1000.0 / 60.0 / 60.0 / 24.0 
# Write a similar method named area that takes as a parameter the radius of  a circle and that returns the area of the circle. For example, the call  
# area(2.0); 
# should return  
# 12.566370614359172.  
# Recall that area can be computed as π times the radius squared and that  Python has a constant called math.pi 

# In[3]:


import math

def area(radius):
    return math.pi * radius**2

#let call area 2.0
result = area(2.0)
print(result)


# 7.Copy and paste the following code into pythons IDLE script  environment. 
#  low = 1 
#  high = 1001 
#  sum = 0 
#  for i in range(low,high): 
#  sum += i 
#   
#  print("sum = " , sum) 
#   
# Modify the code to use a input to prompt the user for the values of low and high. Below is a sample execution in which the user asks for the same  values as in the original program (1 through 1000): 
# low? 1 
# high? 1001 
# sum = 500500 
# Below is an execution with different values for low and high: 
# low? 300 
# high? 5298 
# sum = 13986903 
# You should exactly reproduce this format. 
# 

# In[4]:


low = int(input("low? "))
high = int(input("high? "))
sum_result = 0

for i in range(low, high):
    sum_result += i

print(f"sum = {sum_result}")


# 8.Write a program using while loop that prompts the user for numbers until  the user types 0, then outputs their sum.
# 

# In[5]:


# Initialize sum to 0
sum_result = 0

# Keep prompting for numbers until the user types 0
while True:
    number = int(input("Enter a number (type 0 to exit): "))
    
    if number == 0:
        break  # Exit the loop if the user types 0
    
    sum_result += number

# Output the sum
print(f"The sum of the entered numbers is: {sum_result}")


# 9.Write a program using while loop that prompts the user for numbers until  the user types -1, then outputs their sum. 
# 

# In[6]:


# Initialize sum to 0
sum_result = 0

# Keep prompting for numbers until the user types -1
while True:
    number = int(input("Enter a number (type -1 to exit): "))
    
    if number == -1:
        break  # Exit the loop if the user types -1
    
    sum_result += number

# Output the sum
print(f"The sum of the entered numbers is: {sum_result}")


# 10.Write a method named repl that accepts a String and a number of  repetitions as parameters and returns the String concatenated that many  times. For example, the call repl("hello", 3) returns "hellohellohello".  If the number of repetitions is 0 or less, an empty string is returned. 

# In[7]:


def repl(s, repetitions):
    if repetitions <= 0:
        return ""  # Return an empty string for 0 or negative repetitions
    else:
        return s * repetitions

# Example
result = repl("hello", 3)
print(result)  # Output: hellohellohello


# In[19]:


def repl(s, repetitions):
    if repetitions <= 0:
        return ""  # Return an empty string for 0 or negative repetitions
    else:
        return s * repetitions

# Example
result=repl("we are here",10)
print(result)  # Output: wearehere


# 11.Write a method called printRange that accepts two integers as arguments and  prints the sequence of numbers between the two arguments, separated by  spaces. Print an increasing sequence if the first argument is smaller than  the second; otherwise, print a decreasing sequence. If the two numbers  are the same, that number should be printed by itself. Here are some  sample calls to printRange:  
# printRange(2, 7) 
# printRange(19, 11) 
# printRange(5, 5) 
# The output produced should be the following:  
# 2 3 4 5 6 7  
# 19 18 17 16 15 14 13 12 11  
# 5 
# 

# In[20]:


def printRange(start, end):
    if start < end:
        # Print increasing sequence
        for num in range(start, end + 1):
            print(num, end=" ")
    elif start > end:
        # Print decreasing sequence
        for num in range(start, end - 1, -1):
            print(num, end=" ")
    else:
        # The two numbers are the same, print the single number
        print(start)

# Example calls:
printRange(2, 7)
printRange(19, 11)
printRange(5, 5)


# In[21]:


def printRange(start, end):
    if start < end:
        # Print increasing sequence
        for num in range(start, end + 1):
            print(num, end=" ")
    elif start > end:
        # Print decreasing sequence
        for num in range(start, end - 1, -1):
            print(num, end=" ")
    else:
        # The two numbers are the same, print the single number
        print(start)

# Example calls:
printRange(5, 9)
printRange(20, 20)
printRange(5, 5)


# 12.Write a method named smallestLargest that asks the user to enter numbers,  then prints the smallest and largest of all the numbers typed in by the  user. You may assume the user enters a valid number greater than 0 for  the number of numbers to read. Here is an example dialogue:  
# How many numbers do you want to enter? 4 Number 1: 5 
# Number 2: 11 
# Number 3: -2 
# Number 4: 3 
# Smallest = -2
# Largest = 11
# 

# In[109]:


def smallestLargest():
    num_count = int(input("How many numbers do you want to enter? "))
    
    if num_count <= 0:
        print("Invalid input. Please enter a valid number greater than 0.")
        return

    numbers = []

    for i in range(1, num_count + 1):
        number = float(input(f"Number {i}: "))
        numbers.append(number)

    if numbers:
        smallest = min(numbers)
        largest = max(numbers)
        print(f"Smallest = {smallest}")
        print(f"Largest = {largest}")
    else:
        print("No numbers entered.")

# Run the method
smallestLargest()


# 13.Write a method called printAverage that uses a sentinel loop to repeatedly prompt the user for numbers. Once the user types any number less than zero, the method should display the average of all nonnegative numbers typed. Display the average as a double. Here is a sample dialogue with the user: Type a number: 7 Type a number: 4 Type a number: 16 Type a number: –4 Average was 9.0 If the first number that the user types is negative, do not print an average: Type a number: –2

# In[2]:


def printAverage():
    total = 0
    count = 0

    while True:
        number = float(input("Type a number: "))
        
        if number < 0:
            break  # Exit the loop if a negative number is entered

        total += number
        count += 1

    if count > 0:
        average = total / count
        print(f"Average was {average:.1f}")
    else:
        print("No nonnegative numbers entered.")

# lets run the method
printAverage()


# 14.Write a method named numUnique that takes three integers as parameters  and returns the number of unique integers among the three. For example,  the call numUnique(18, 3, 4) should return 3 because the parameters  have three different values. By contrast, the call numUnique(6, 7, 6) 
# should return 2 because there are only two unique numbers among the  three parameters: 6 and 7

# In[105]:


numbers=[3,4,3]
numUnique=[]
for a in numbers:
    if a not in numUnique:
        numUnique.append(a)
print(numUnique)



# 15. A Random object generates pseudo-random numbers. Find out how to  use the Random class and write a program that simulates rolling of two 6- sided dice until their combined result comes up as 7. One possible output  can be seen as below: 
#  2 + 4 = 6 
# 3 + 5 = 8 
# 5 + 6 = 11 
# 1 + 1 = 2 
# 4 + 3 = 7 
# You won after 5 tries!
# 

# In[96]:


import random

def roll_dice():
    return random.randint(1, 6)

def simulate_dice_rolls():
    total = 0
    count = 0

    while total != 7:
        die1 = roll_dice()
        die2 = roll_dice()

        total = die1 + die2
        count += 1

        print(f"{die1} + {die2} = {total}")

    print(f"It took {count} rolls to get a total of 7.")

# lets run the simulation
simulate_dice_rolls()


# In[ ]:





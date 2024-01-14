#!/usr/bin/env python
# coding: utf-8

# In[1]:


b = """+----+

\\    /

/    \\

\\    /

/    \\

\\    /

/    \\

+----+"""
for x in b:
    pass
print(b)


# In[2]:


a ="""**********

**********

**********

**********

**********"""
for x in a:
    pass
print(a)


# In[12]:


#Question 3
for x in range(1,7):
  print(x)
for x in range(2,14,2):
  print(x)
for x in range(4,80,15):
  print
for x in range(30,-30,-10):
  print(x)
for x in range(-7,14,4):
  print(x)
for x in range(97,81,-3):
  print(x)
for x in range(-4,87,18):
  print(x)


# In[4]:


#Question 4
class Constant:
    line_num = 7
for i in range(1, Constant.line_num + 1):
    for j in range(i):
        print(i, end="")
    print()


# In[6]:


#Question 6
import math 

def area_of_circle(radius):
    return math.pi * radius * radius
radius = float(input("Enter the value of the radius "))
answer = area_of_circle(radius)
print("The area is", answer)


# In[8]:


#Question 8
i = []

while True:
    value = int(input("Enter your values, end at 0 when satisfied "))
    if value == 0:
        break
    i.append(value)

answer = sum(i)
print("The sum of your values is", answer)


# In[9]:


#Question 9
i = []

while True:
    value = int(input("Enter your values, end at -1 when satisfied "))
    if value == -1:
        break
    i.append(value)

answer = sum(i)
print("The sum of your values is", answer)


# In[10]:


#Question 10
def repl(String, number):
    return String * number
String = str(input("Enter the word"))
number = int(input("Enter the iterator"))
answer = repl(String, number)
print (answer)


# In[11]:


#Question 14
def numUnique(a, b, c):
    if a == b or a == c or b ==c:
        print("There are 2 unique numbers")
    elif a == b == c:
        print("There is 1 unique number")
    else:
        print("There are 3 unique numbers")
        
a = int(input("Enter the first integer"))
b = int(input("Enter the second integer"))
c = int(input("Enter the third integer"))

numUnique(a, b, c)


# In[13]:


#Question 12
def smallestLargest ():
    count = int(input("How many numbers do you want to enter? "))
    values = [int(input(f"Number {i}:")) for i in range(1, count + 1)]
    print(f"smallest = {min(values)}")
    print(f"Largest = {max(values)}")
smallestLargest()


# In[8]:


#Question 5
def pay(salary, hours_worked):
    regular_hours = 8  
    overtime_multiplier = 1.5  

    if hours_worked <= regular_hours:
        total_pay = salary * hours_worked 
    else:
        regular_pay = salary * regular_hours  
        overtime_pay = salary * overtime_multiplier * (hours_worked - regular_hours) 
        total_pay = regular_pay + overtime_pay  # Calculate total pay including overtime

    return total_pay
print(pay(5.50, 6))
print()
print (pay(4.00, 11))


# In[3]:


#Question7
low = int(input("low? "))  
high = int(input("high? "))  
sum_result = 0

for i in range(low, high):
    sum_result += i

print("sum = ", sum_result)


# In[4]:


#Question11
def printRange(start, end):
        if start < end:
             for i in range(start, end + 1):
                 print(i, end=" ")
        elif start > end:
              for i in range(start, end - 1, -1):
                 print(i, end=" ")
        else:
            print(start)
printRange(2, 7)
print() 
printRange(19, 11)
print() 
printRange(5, 5)


# In[6]:


#Question 13
def printAverage():
    total = 0.0
    count = 0

    while True:
        num = float(input("Type a number: "))
        if num < 0:
            if count > 0:
                average = total / count
                print(f"Average was {average:.1f}")
            else:
                print("No non-negative numbers were entered.")
            break
        else:
            total += num
            count += 1


printAverage()


# In[7]:


#Question 15
import random

def roll_dice():
    return random.randint(1, 6)  

def main():
    tries = 0
    while True:
        dice1 = roll_dice()
        dice2 = roll_dice()
        total = dice1 + dice2
        print(f"{dice1} + {dice2} = {total}")
        tries += 1
        if total == 7:
            print(f"You won after {tries} tries!")
            break

if __name__ == "__main__":
    main()


# In[ ]:





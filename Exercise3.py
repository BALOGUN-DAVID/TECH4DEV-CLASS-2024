#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Question1
values = input("Enter the values separated by spaces: ").split()
values = list(map(int, values))
print(max(values))


# In[3]:


#Question2
value = input("Enter your values with commas")
values = value.split(",")
num = 0
for i in values:
    num = num + int(i)
print ("The average is ", num / len(values))


# In[4]:


#Question3
value = input("Enter your values")
values = value.split(",")
values.reverse()
print("The reversed list is ",values)


# In[5]:


#Question4
def compare_lists(list1, list2):
    values = list1.split(",")
    values2 = list2.split(",")

    if len(values) != len(values2):
        return False

    for i in range(len(values)):
        if values[i] >= values2[i]:
            return False
    return True

input_list1 = input("Enter your values separated by commas for the first list: ")
input_list2 = input("Enter your values separated by commas for the second list: ")
result = compare_lists(input_list1, input_list2)
print("The result is:", result)


# In[6]:


#Question5
def indexswapper(liist, index1, index2):
    if 0 <= index1 < len(liist) and 0 <= index2 < len(liist):
        liist[index1], liist[index2] = liist[index2], liist[index1]
    else:
        print("Try another index")

value = input("Enter the values separated by spaces: ")
values = list(map(int, value.split()))
index1 = int(input("Enter the first index: "))
index2 = int(input("Enter the second index: "))

print("Original list is", values)
indexswapper(values, index1, index2)
print("List with swapped indexes:", values)


# In[7]:


#Question6
list1 = [2, 4, 5, 7, 8]
list2 = [6, 11, 8, 1, 3]
list1.extend(list2)
print(list1)

list1 = input("Enter the values: ").split()
list2 = input("Enter the values: ").split()
list1.extend(list2)
print(list1)


# In[8]:


#Question8
def calculate_range():
    values = input("Enter your values, separated by spaces: ")
    A = list(map(int, values.split()))
    range_value = 1 + (max(A) - min(A))
    return range_value

result = calculate_range()
print("The range is", result)


# In[9]:


#Question9
def Counter(minimum, maximum, values):
    count = 0
    for num in values:
        if minimum <= num <= maximum:
            count += 1
    return count
value = input("Enter the values separated by spaces ")
values = list(map(int, value.split()))
minimum = int(input("Enter the minimum value "))
maximum = int(input("Enter the maximum value "))
answer = Counter(minimum, maximum, values)
print("The count between min and max is", answer)


# In[10]:


#Question10
def IsListSorted(values):
    for i in range(len(values)-1):
        if values[i] > values[i + 1]:
            return False
    return True
value = input("enter your values separated by spaces")
values = list(map(float, value.split()))
x = IsListSorted(values)
print (x)


# In[ ]:





#!/usr/bin/env python
# coding: utf-8

# # QUESTION 1

# In[3]:


# list of elements
list1 = [2,4,7,4,23,5,1,4,8,9]
# sorting the list
list1.sort()
# printing the MAXIMUM VALUE
print("Maximum Value:", list1[-1])


# # QUESTION 2

# In[14]:


# Get average of a list 
def Average(list2): 
    return sum(list2) / len(list2)

# list of elements
list2=[4,7,1,5,11,53,12,46,84,23]
average = Average(list2)

    # Printing the average
print("Average =", round(average, 2))


# # QUESTION 3

# In[16]:


# Reversing a list 
def Reverse(list3):
   new_list3 = list3[::-1]
   return new_list3
# Printing reverse list 
my_list3 = [2,6,7,45,23,53,14,45,89,5]
print(Reverse(my_list3))


# # QUESTION 4

# In[4]:


def compare_lists(list1, list2):
    if len(list1) != len(list2):
        return False
    for i in range(len(list1)):
        if list1[i] >= list2[i]:
            return False
    return True

# Testing the function
list1 = [1, 2, 3]
list2 = [2, 3, 4]
print(compare_lists(list1, list2)) 


# # QUESTION 5
# 

# In[6]:


def swap_elements(list5, index1, index2):
    if not (0 <= index1 < len(list5) and 0 <= index2 < len(list5)):
        return "Invalid index"
    list5[index1], list5[index2] = list5[index2], list5[index1]
    return list5

# Testing the  output
print(swap_elements([1, 2, 3, 4, 5], 1, 3)) 


# # QUESTION 6

# In[7]:


def combine_lists(list1, list2):
    return list1 + list2

# Testing the  output
print(combine_lists([10,12, 14], [16, 18, 20]))  


# # QUESTION 7

# In[11]:


def find_last_index(list7, value):
    try:
        return len(list7) - 1 - list7[::-1].index(value)
    except ValueError:
        return -1

# Testing the  output
print(find_last_index([74, 85, 102, 99, 101, 85, 56], 85))  


# # QUESTION 8

# In[12]:


def print_range(list8):
    if not list8:
        return "List is empty"
    range_value = max(list8) - min(list8) + 1
    return range_value

# Testing the  output
print(print_range([36, 12, 25, 19, 46, 31, 22])) 


# # QUESTION 9

# In[13]:


def count_elements_in_range(list9, min_value, max_value):
    return len([i for i in list9 if min_value <= i <= max_value])

# Testing the  output
print(count_elements_in_range([14, 1, 22, 17, 36, 7, -43, 5], 4, 17))  


# # QUESTION 10

# In[5]:


def is_sorted(list10):
    return all(list10[i] <= list10[i+1] for i in range(len(list10)-1))

# Testing the  output
numbers = [16.1, 12.3, 22.2, 14.4]
print(is_sorted(numbers))  

numbers = [1.5, 4.3, 7.0, 19.5, 25.1, 46.2]
print(is_sorted(numbers)) 


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





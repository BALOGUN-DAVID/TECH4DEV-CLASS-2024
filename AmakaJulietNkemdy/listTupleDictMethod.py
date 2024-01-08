#!/usr/bin/env python
# coding: utf-8

# 10 LIST METHODS
# [] are used to define a list

# # 1 APPEND: This appends the specified element to the end of the list.

# In[5]:


Nigeria=['Abia','Imo','Lagos','Kano']
Nigeria.append('Kwara')
print(Nigeria)


# # 2 CLEAR: This empties or removes the fields in the list

# In[6]:


Nigeria.clear()


# In[8]:


print(Nigeria)


# # 3 COPY:This returns a shallow copy of the list

# In[17]:


Nigeria=['Abia','Imo','Lagos','Kano']
copy_Nigeria=Nigeria.copy() 
copy_Nigeria.remove('Lagos')
print(Nigeria)
print(copy_Nigeria)


# # 4 COUNT: This returns the number of occurences of the elemets in thr list

# In[23]:


Nigeria=['Abia', 'Imo', 'Lagos', 'Kano','Abia']
print (Nigeria)
Nigeria.count('Abia') 


# # 5 EXTEND:This extends the list by appending the elements from the iterable

# In[34]:


Nigeria=['Abuja','Lagos']
Nigeria2=['Imo','Jigawa']
Nigeria.extend(Nigeria2)
print(Nigeria)


# In[35]:


Nigeria.extend([Nigeria2])
print(Nigeria)


# # 6 INDEX:Finds the location of the element

# In[39]:


print(Nigeria.index('Abuja'))
print(Nigeria.index('Imo'))
print(Nigeria.index('Lagos'))


# # 7 INSERT:Inserts the specified element at the specified index location

# In[53]:


Nigeria=['Lagos','Abuja']
Nigeria.insert(1,'Niger')
print(Nigeria)


# # 8 REMOVE:Removes the element from the array

# In[59]:


Nigeria=['Lagos','Abuja','Benue']
Nigeria.pop() #pops out the last element on the list
print(Nigeria)


# In[60]:


Nigeria=['Lagos','Abuja','Benue']
Nigeria.pop(1) #pops out 'Abuja'
print(Nigeria)


# Similarly, we can use 'remove'

# In[62]:


Nigeria=['Lagos','Abuja','Benue']
Nigeria.remove('Abuja')
print(Nigeria)


# # 9 REVERSE: Reverses the element of the list in place

# In[65]:


Nigeria=['Lagos','Abuja','Benue']
Nigeria.reverse()
print(Nigeria)


# # 10 SORT: Sorts the list according to a specified 'key'

# In[67]:


Nigeria.sort()
print(Nigeria)
#automtically sorts in alphabetical order


# In[89]:


Nigeria=['Zamfara','zamfara','abuja','Abuja','lagos']
Nigeria.sort()
print(Nigeria)
#it prints the Uppercase before the lowercases, all in alphabetical order


# In[93]:


#let's provide a 'key'
Nigeria=['Benue','Zamfara','abuja','lagos']
Nigeria.sort(key=lambda name:name.lower())
print(Nigeria)
#the key prints in alphabetical order, regardless of the case


# In[95]:


Nigeria=['Taraba','Lagos','Abuja','Benue','Abia','Imo']
Nigeria.sort(key=lambda name:len(name))
print(Nigeria)
#this returns the each element by the length of their name


# In[101]:


#Let's reverse the list according to len, regardless of cases
Nigeria=['Taraba','Lagos','Kano','Adamawa','Abuja','benue','Abia','imo']
Nigeria.sort(key=lambda name:len(name),reverse =True)
print(Nigeria)


# In[102]:


Nigeria=['Taraba','Lagos','Kano','Adamawa','Abuja','benue','Abia','imo']
Nigeria.sort(key=lambda name:len(name),reverse=False)
print(Nigeria)


# In[103]:


#alphabetically,regarding the cases
Nigeria=['Taraba','Lagos','Kano','Adamawa','Abuja','benue','Abia','imo']
Nigeria.sort(reverse=False)
print(Nigeria)


# In[104]:


#alphabetically,regarding the cases
Nigeria=['Taraba','Lagos','Kano','Adamawa','Abuja','benue','Abia','imo']
Nigeria.sort(reverse=True)
print(Nigeria)


# 5 TUPLES METHODS
# ()represents Tuples and are Immuntable.ie, once a tuple is created, one cannot modify the content.

# # 1 COUNT:returns the number of occurences of the specified element in the tuple 

# In[115]:


Siblings=('Dede','Amaka','Nonso','Mezu','Amara','Dera')
Siblings.count('Amaka')
#Amaka occurs once


# # 2 LEN: Returns the number of elements in the tuple
# 

# In[117]:


#How many Siblings are there?
len(Siblings)


# # 3 MAX: Returns the largest element in the tuple

# In[123]:


Age=(28,25,24,22,19,17)
max(Age)


# # 4 MIN: Returns the smallest element in the tuple

# In[124]:


Age=(28,25,24,22,19,17)
min(Age)


# # 5 REPETITION: Repeats the specified element in a tuple

# In[127]:


print(('Amaka',)*3)
print(('Dede',)*5)


# 5 DICTIONARY METHODS
# {}represents Dict

# # 1 VALUES: Grabs each of the values from the Dictionary

# In[129]:


#let's create a sample dict that holds telcom.
#networks in Nigeria and their IDs
TelcomN:dict={0:'Mtn',1:'Glo',2:'9mobile',3:'Airtel'}
print(TelcomN.values())
    


# # 2 COPY:returs a shallow copy of the dict

# In[130]:


Nigeria:dict={0:['North','East'],1:['West','South']}
my_copy:dict=Nigeria.copy()
print(Nigeria)
print(my_copy)


# # 3 GET:returns the value for the specified key. If the key is bot found, it returns the default value'None', if not provided.

# In[133]:


#Get a value from the dict without raising an exception
TelcomN:dict={0:'Mtn',1:'Glo',2:'9mobile',3:'Airtel'}
print(TelcomN.get(3))
print(TelcomN.get(100))
print(TelcomN.get(2))
print(TelcomN.get(100,'missing'))


# # 4 CLEAR:Clears the values you have in a dict

# In[134]:


TelcomN:dict={0:'Mtn',1:'Glo',2:'9mobile',3:'Airtel'}
TelcomN.clear()
print (TelcomN)


# # 5 FROMKEYS:Returns a new dict with specified keys and the same default value for all keys

# In[136]:


Network=['Mtn','Glo','9mobile','Airtel']
TelcomN:dict=dict.fromkeys(Network)
print(TelcomN)
#we did not specify any key to be returned,hence'none' as default key 


# In[139]:


Network=['Mtn','Glo','9mobile','Airtel']
TelcomN:dict=dict.fromkeys(Network,'working')
print(TelcomN)
#show'working'as default key using the 'fromkeys' function in a dict.


# In[145]:


numbers=[4,7,1,5,11,53,12,45,84,23]
sum = 0
for s in numbers:
    sum += s
print(f'sum:{sum}')
print(f'count:{len(numbers)}')
print(f'average:{sum/len(numbers)}')


# In[ ]:


numbers=[2,4,7,4,23,5,1,4,8,9]
max = 0
for m in numbers:
    max += s
print(f'sum:{sum}')
print(f'count:{len(numbers)}')
print(f'average:{sum/len(numbers)}')


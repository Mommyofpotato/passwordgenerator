#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random


# In[2]:


letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

symbols=['!','@','#','$','%','^','&','*','(',')','-','+']

numbers=['0','1','2','3','4','5','6','7','8','9']

print("Welcome to the password Generator")
num_letters=input("How many letters would you like?")
num_letters=int(num_letters)         
num_symbols=input("How many symbols would you like?")
num_symbols=int(num_symbols)
num_numbers=input("How many numbers would you like?")
num_numbers=int(num_numbers)
pass_length=num_numbers+num_letters+num_symbols


# In[5]:


password=[]
for letter in range(num_letters):
    letter_random=random.randint(0,51)
    password+=letters[letter_random]

for number in range(num_numbers):
    number_random=random.randint(0,9)
    password+=numbers[number_random]

for symbol in range(num_symbols):
    symbols_random=random.randint(0,11)
    password+=symbols[symbols_random]
print(password)


# In[12]:


random_password=[]
for character in password:
    randomize=random.randint(0,pass_length-1)
    random_password+=password[randomize]
password=""
for char in random_password:
    password+=char
print("Here is your password:",password)


# In[ ]:





# In[ ]:





#!/usr/bin/env python
# coding: utf-8

# # Write a Python program to get the Fibonacci series between 0 to 50

# In[ ]:


n=10
a=0
b=1
s=0
print("Expected output:")
for x in range(n):
    print(s,end=" ")
    s=a+b
    b=a
    a=s


# # Write a Python program that accepts a word from the user and reverse it.
# 
# 

# In[ ]:


def reverse(string):
    reversed_string = ""
    for i in string:
        reversed_string = i + reversed_string
    print("output:", reversed_string)
string = input("output:")
reverse(string)



# # Write a Python program to count the number of even and odd numbers from a series of numbers.
# 

# In[11]:


sample_numbers=eval(input("numbers="))
count_even=0
count_odd=0
for i in sample_numbers:
    if(i%2==0):
        count_even=count_even+1
    else:
        count_odd=count_odd+1
print("Number of even numbers:",count_even)
print("Number of odd numbers:",count_odd)


# In[ ]:





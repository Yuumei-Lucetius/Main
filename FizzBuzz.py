
# coding: utf-8

# In[10]:

"""
Python-implementation of a FizzBuzz question:

Write a program that prints the numbers from 1 to 100. But for multiples of three print "Fizz" instead 
of the number and for the multiples of five print "Buzz". For numbers which are multiples of both three 
and five print "FizzBuzz".
"""

i = 1
while i < 100:
    if i % 3 and i % 5:
        print (i)
    elif not i % 3 and not i % 5:
        print ("FizzBuzz")
    elif not i % 3:
        print ("Fizz")
    elif not i % 5:
        print ("Buzz")
    i += 1


# In[ ]:




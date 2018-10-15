
# coding: utf-8

# In[11]:


n = int(input("Enter a number: "))
for i in range(1,n):
    if i % 15 == 0:
        print ("FizzBuzz")
    elif i % 3 == 0:
        print ("Fizz")
    elif i % 5 == 0:
        print ("Buzz")
    else:
        print (i)


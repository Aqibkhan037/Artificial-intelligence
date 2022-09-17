#!/usr/bin/env python
# coding: utf-8

# In[7]:


n = input('Enter the number to check weather it is happy or not:')

choice = 1
sum=0
x=0
res=0
while choice!=0:
    for i in n:
        x=int(i)
        sum+=(x**2)
    print('The result of squaring and addition is: ',sum)
    n=str(sum)
    sum=0
    choice = int(input('Enter 0 to exit or 1 to continue:'))
if n=='1':
    print('The Number is Happy Number')
else:
    print('The Number is Sad Number')


# In[ ]:





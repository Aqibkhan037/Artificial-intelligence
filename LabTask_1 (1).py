#!/usr/bin/env python
# coding: utf-8

# In[6]:


n = int(input('Enter a Number'))
if n%2==0:
    print('The Number is Even')
else:
    print('The Number is Odd')


# In[5]:


n = int(input('Enter the Number'))

sum = n

while n!=0:
    n=int(input('Enter the Number'))
    sum+=n
print('The Result is ',sum)
    


# In[14]:


n = int(input('Enter the Number'))

counter = 0

for i in range (1,n+1):
    if n%i==0:
        counter+=1
if counter>2:
    print('Not Prime Number')
else:
    print(' Prime Number ')


# In[15]:


sum=0
for i in range (0,5):
    n = int(input('Enter the Number'))
    sum+=n
print('The Result is',sum)


# In[17]:


result=0
for i in range (1,10+1):
    result += i
print('The Result is',result)
    


# In[18]:


n = int(input('Enter a Number'))
print('The Number Entered was',n)


# In[21]:


import random

n = random.randint(1,9)

n1 = int(input('Enter a Number for Guessing'))

if n1>n:
    print('The Number you Entered is High',n)
elif n1<n:
    print('The Number you Entered is low',n)
elif n1==n:
    print('Nice Guess Mate')


# In[26]:


n = int(input('Enter a Number'))
x=0
print('The Entered Number',n)
result = ''
while n!=0:
    x = n%10
    result =result + str(x) 
    n=int(n/10)

print('The Reversed Number',result)


# In[28]:


n = int(input('Enter a Number of elements you want to add'))
even=0
odd = 0

for i in range (0,n):
    n = int(input('Enter a Number'))
    if n%2==0:
        even+=n
    else: odd+=n

print('The total of even numbers is',even)
print('The total of odd numbers is',odd)




# In[37]:


n = int(input ("How many terms the user wants to print? "))  
   
a = 0  
b = 1  
c = 0  
if n <= 0:  
    print ("Please enter a positive integer, the given number is not valid")   
elif n == 1:  
    print ("The Fibonacci sequence of the numbers up to", n, ": ")  
    print(a)   
else:  
    print ("The fibonacci sequence of the numbers is:")  
    while c < n:  
        print(a)  
        d = a + b   
        a = b  
        b = d  
        c += 1  


# In[52]:


n = int(input('Enter a marks of student:'))

if n>100 or n<0:
    print('invalid input')
else:
    if n<50:
        print('You Got F Grade, Better luck next time:',n)
    elif n>50 and n<60:
        print(' Your Grade is E, Improvement suggested',n)
    elif n>61 and n<70:
        print('D is your Grade',n)
    elif n>71 and n<80:
        print('C is your Grade',n)
    elif n>81 and n<90:
        print('Your Grade is B,Good',n)
    elif n>91 and n<100:
        print('Your Scored a Great Deal, Excelent',n)
    
        


# In[53]:


n = int(input('Enter the Number'))

fact = 1

for i in range (1,n+1):
    fact = fact*i
print('The Factorial is:',fact)
    


# In[ ]:





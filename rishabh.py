#!/usr/bin/env python
# coding: utf-8

# In[1]:


n=int(input("enter the value of n"))


# In[3]:


arr=[]
for i in range(n):
    value=int(input("enter the value"))
    arr.append(value)


# In[4]:


print(arr)


# In[5]:


arr=[]
for i in range(n):
    value=int(input("enter the value"))
    arr.append(value)


# In[6]:


print(arr)


# In[17]:


for i in range(n):
    for j in range(i,n):
        if arr[i]>arr[j]:
            temp=arr[i]
            arr[i]=arr[j]
            arr[j]=temp
print(arr)


# In[18]:


summ=0
for i in arr:
    summ=summ+i
mean=summ/len(arr)
print(summ)
print(mean)
print(arr[len(arr)//2])


# In[21]:


sum(arr)


# In[24]:


arr.reverse()


# In[25]:


print(arr)


# In[26]:


arr[::-1]


# In[27]:


print(arr)


# In[28]:


arr=arr[::-1]


# In[29]:


print(arr)


# In[36]:


import math
summ2=0
for i in arr:
    summ2=summ2+((i-mean)**2)
ans=math.sqrt(summ2/n)
print(ans)


# In[37]:


variance=ans**2


# In[38]:


print(variance)


# In[ ]:





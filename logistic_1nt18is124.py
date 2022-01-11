#!/usr/bin/env python
# coding: utf-8

# In[9]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[13]:


df=pd.read_csv(r"C:\Users\risha\Downloads\Student-University.csv",header=None)


# In[14]:


df.head()


# In[15]:


X = df.iloc[:,0:2]
Y = list(df[2])


# In[17]:


for i in range(len(X)):
    X[0] =  ( X[0] - X[0].min() ) / ( X[0].max() - X[0].min() ) 
    X[1] =  ( X[1] - X[1].min() ) / ( X[1].max() - X[1].min() ) 


# In[18]:


X.head()


# In[19]:


from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(X, Y, train_size = 0.8)


# In[20]:


x1_train = list(x_train[0])
x1_test = list(x_test[0])
x2_train = list(x_train[1])
x2_test = list(x_test[1])


# In[21]:


l_rate = 0.3
e = 2.71828
b0 = 1
b1 = 0.5
b2 = 0.5
n = len(x1_train)
n_test = len(x1_test)
b = [b0, b1, b2]


# In[22]:


def grad_desc(b):
    P = []
    X = []
    a = 0
    
    for i in range(n):
        X.append(b[0] + (b[1] * x1_train[i]) + (b[2] * x2_train[i]))
                 
    for i in range(n):
        P.append( 1 / ( 1 + ( e ** ( -1 * X[i] ) ) ) )
                 
    for j in range(3):
                 for i in range(n):
                     a = l_rate * (y_train[i] - P[i]) * (P[i]) * (1 - P[i])
                     if(j == 1):
                        a *= x1_train[i]
                     if(j == 2):
                        a *= x2_train[i]
                     b[j] += a 
    return b


# In[29]:


for i in range(100):
    b = grad_desc(b)
print(b)


# In[24]:


x = []
p = []

for i in range(n_test):
    x.append(b[0] + (b[1] * x1_test[i]) + (b[2] * x2_test[i]))
    
for i in range(n_test):
    p.append( 1 / ( 1 + ( e ** ( -1 * x[i] ) ) ) )
    
df1 = pd.DataFrame(list(zip(x, p)), columns =['X', 'P'])
df1.head()


# In[25]:


pred = []
for i in range(n_test):
    if (df1.P[i] > 0.5):
        pred.append(1)
    else:
        pred.append(0)

df1['Class'] = pred
df1['Y'] = y_test
df1.head()


# In[26]:


from sklearn.metrics import classification_report, confusion_matrix
print(confusion_matrix(y_test, pred))
print(classification_report(y_test, pred))


# In[ ]:





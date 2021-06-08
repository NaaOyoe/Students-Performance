#!/usr/bin/env python
# coding: utf-8

# In[12]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')

df = pd.read_csv("StudentsPerformance.csv")
df


# In[4]:


df.shape


# In[5]:


df.isnull().sum() # there are no null values,which means that there no missing data. I chosethe isnull method because
it shows the number of values in each coloumn.


# In[14]:


df.head(3)


# In[22]:


df['race/ethnicity'].value_counts()[0:5].keys()


# In[23]:


plt.figure(figsize=(8,5))
plt.bar(list(df['race/ethnicity'].value_counts()[0:5].keys()),list(df['race/ethnicity'].value_counts()[0:5]),color='g')


# In[39]:


scores = df[['test preparation course','math score']]


# In[40]:


scores.head()


# In[42]:


scores=scores.sort_values(by=['math score'],ascending=False)


# In[43]:


scores.head()


# In[47]:


plt.figure(figsize=(8,5))
plt.bar(list(scores['test preparation course'])[0:5],list(scores['math score'])[0:5],color='b')
plt.show()


# In[51]:


df.head()


# In[55]:


df['lunch']=='standard'


# In[56]:


standard=df[df['lunch']=='standard']
standard.head(10)


# In[58]:


standard.sort_values(by=['math score'],ascending=False).head()


# In[72]:


standard[['gender','math score']].sort_values(by=['math score'],ascending=False).head()                                                                     


# In[75]:


plt.figure(figsize=(8,5))
plt.bar(list(standard['gender'])[0:5],list(standard['math score'])[0:5],color='r')
plt.show()


# In[ ]:





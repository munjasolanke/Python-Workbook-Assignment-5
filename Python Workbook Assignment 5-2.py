#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Python Workbook Assignment 5-2 
import pandas as pd
names = ['Bob','Jessica','Mary','John','Mel']
grades = [76,95,77,78,99]
bsdegrees = [1,1,0,0,1]
msdegrees = [2,1,0,0,0]
phddegrees = [0,1,0,0,0]
GradeList = zip(names,grades,bsdegrees,msdegrees,phddegrees)
df = pd.DataFrame(data=GradeList,columns=['Names','Grades','bsdegrees','msdegrees','phddegrees'])
df


# In[18]:


df['Grades'].count() # number of values


# In[19]:


df['bsdegrees'].count()


# In[20]:


df['msdegrees'].count()


# In[21]:


df['phddegrees'].count()


# In[4]:


df['Grades'].mean() # arithmetic average


# In[22]:


df['bsdegrees'].mean()


# In[23]:


df['msdegrees'].mean()


# In[24]:


df['phddegrees'].mean()


# In[6]:


df['Grades'].std() # standard deviation


# In[25]:


df['bsdegrees'].std()


# In[26]:


df['msdegrees'].std()


# In[27]:


df['phddegrees'].std()


# In[8]:


df['Grades'].min() # minimum


# In[28]:


df['bsdegrees'].min()


# In[29]:


df['msdegrees'].min()


# In[30]:


df['phddegrees'].min()


# In[9]:


df['Grades'].max() # maximum


# In[31]:


df['bsdegrees'].max()


# In[32]:


df['msdegrees'].max()


# In[33]:


df['phddegrees'].max()


# In[10]:


df['Grades'].quantile(.25) # first quartile


# In[34]:


df['bsdegrees'].quantile(.25)


# In[35]:


df['msdegrees'].quantile(.25)


# In[36]:


df['phddegrees'].quantile(.25)


# In[11]:


df['Grades'].quantile(.5) # second quartile


# In[37]:


df['bsdegrees'].quantile(.5) 


# In[38]:


df['msdegrees'].quantile(.5) 


# In[39]:


df['phddegrees'].quantile(.5) 


# In[12]:


df['Grades'].quantile(.75) # third quartile


# In[40]:


df['bsdegrees'].quantile(.75)


# In[41]:


df['msdegrees'].quantile(.75)


# In[42]:


df['phddegrees'].quantile(.75)


# In[13]:


# computes the arithmetic average of a column
# mean = dividing the sum by the number of values
df['Grades'].mean()


# In[43]:


df['bsdegrees'].mean()


# In[44]:


df['msdegrees'].mean()


# In[45]:


df['phddegrees'].mean()


# In[14]:


# finds the median of the values in a column
# median = the middle value if they are sorted in order
df['Grades'].median()


# In[46]:


df['bsdegrees'].median()


# In[47]:


df['msdegrees'].median()


# In[48]:


df['phddegrees'].median()


# In[15]:


# finds the mode of the values in a column
# mode = the most common single value
df['Grades'].mode()


# In[50]:


df['bsdegrees'].mode()


# In[51]:


df['msdegrees'].mode()


# In[52]:


df['phddegrees'].mode()


# In[16]:


df.var()


#!/usr/bin/env python
# coding: utf-8

# In[34]:


import pandas as pd
fname = 'train.csv'
data = pd.read_csv(fname)     
'''here we load the dataset for analysis'''


# In[3]:


len(data)
'''this determines the length of the dataset. how many rows we have'''


# In[33]:


data.head()
'''we look at the dataset form the tp to determine the headers adn the different coloumn labels'''


# In[14]:


data.count()
'''each coloumn has entries in it. throuhg the 
count fucntion we can determine the entries in each of them'''


# In[31]:


data['Age'].min(), data['Age'].max()
# here we determine the extremes of the data values provided in this case the age


# In[8]:


data['Survived'].value_counts()
# here we determine the number of Survivors adn those who did not survive, 0 & 1 respectively


# In[9]:


data['Survived'].value_counts() * 100 / len(data) 
# this fucntion determines the percentages of each group, survivors and deaths.


# In[10]:


data['Sex'].value_counts()
# calculates the number of peopel in each sex group


# In[12]:


data['Pclass'].value_counts()
# counts the number of people in each passenger class.


# In[20]:


get_ipython().run_line_magic('matplotlib', 'inline')
alpha_color = 0.7
data['Survived'].value_counts().plot(kind='bar')
# here we plot the number of survivors and deaths on a bar graph


# In[21]:


data['Sex'].value_counts().plot(kind='bar',
                                color=['b', 'r'],
                                alpha=alpha_color)
# below is the chart showing that there were more males than females in the ship. 


# In[24]:


data['Pclass'].value_counts().sort_index().plot(kind='bar',
                                   alpha=alpha_color)
# plots and indexes teh coloumn according to the passenger classes.


# In[25]:


data.plot(kind='scatter', x='Survived', y='Age')
# a scatter plot ot use in understaidn the distribution of survivors adn their ages. the chart is 
# not clear but it show that all surviors were in all age groups 


# In[26]:


data[data['Survived']== 1]['Age'].value_counts().sort_index().plot(kind='bar')


# In[27]:


bins = [0, 10, 20, 30, 40, 50, 60, 70, 80]
data['AgeBin'] = pd.cut(data['Age'], bins)
# this places teh different people in their respective age groups adn uses this to create 
# a chart below.


# In[28]:


data[data['Survived'] == 1]['AgeBin'].value_counts().sort_index().plot(kind='bar')


# In[29]:


data[data['Survived'] == 0]['AgeBin'].value_counts().sort_index().plot(kind='bar')


# In[ ]:





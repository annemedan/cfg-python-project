#!/usr/bin/env python
# coding: utf-8

# In[7]:


import pandas as pd
import seaborn as sns
import matplotlib as mpt


# In[3]:


data = pd.read_csv("data.csv")


# In[4]:


data.head()


# In[5]:


data.info()


# In[6]:


data = data.drop(["latitude", "longitude"], axis=1)


# In[13]:


#state 
state = sns.barplot(x="state", y="firespots", data=data)
state.set_xticklabels(chart.get_xticklabels(), rotation=45)


# In[9]:


#month
month = sns.barplot(x="month", y="firespots", data=data)


# In[ ]:





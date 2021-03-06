#!/usr/bin/env python
#coding: utf-8

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


#year

year = sns.barplot(x="year", y="month", data=data)

#year with most fires

most_firespots = sns.barplot(x="year", y="firespots", data=data)


import csv

with open("data.csv") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line=0
    highest_firespots=0
    month=""
    state=""
    for row in csv_reader:
        if line!=0:
            if row[0]=="2019":
                if int(row[5])>highest_firespots:
                    highest_firespots=int(row[5])
                    month=row[1]
                    state=row[2]
        line += 1                
    
    print(highest_firespots)
    print("The month with the highest firespots [{}], was {} on {}".format(highest_firespots,month,state))
    print("I've processed {} lines to provide this information.".format(line))

 

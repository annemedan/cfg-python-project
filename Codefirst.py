#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import seaborn as sns
import matplotlib as plt
import csv


# In[3]:


print("Sales Dictionary")

with open('sales.csv', 'r') as csv_file:
    spreadsheet = csv.DictReader(csv_file)
    
    for row in spreadsheet:
        print(dict(row))


# In[5]:


with open('sales.csv', 'r') as csv_file:
    spreadsheet = csv.DictReader(csv_file)
    
    sales = []

    for row in spreadsheet:
        sales_value = row['sales']
        sales.append(sales_value)
    
    
print('Sales Monthly: {}'.format(sales))


# In[7]:


with open('sales.csv', 'r') as csv_file:
    spreadsheet = csv.DictReader(csv_file)

    sales = []

    for row in spreadsheet:
        month_sales = int(row['sales'])
        sales.append(month_sales)
        
sum_sales = sum(sales)
cont_sales = len(sales)

   
print('Sales Total: {}'.format(sum_sales))

print('Sales Average: {}'.format(sum_sales / cont_sales))


# In[8]:


with open('sales.csv', 'r') as csv_file:
    spreadsheet = csv.DictReader(csv_file)
       
    percent = []
    
    for n in range(11):
        perc = sales[1 + n] / sales[0 + n] * 100
        percent.append(perc)
        
 
print('Sales Monthly changes as a percentage: {}'.format(percent))


# In[9]:


with open('sales.csv', 'r') as csv_file:
    spreadsheet = csv.DictReader(csv_file)
    
    sales = []

    for row in spreadsheet:
        month_sales = int(row['sales'])
        sales.append(month_sales)
        
lowest_sales = min(sales)
highest_sales = max(sales)

print('Lowest Sales: {}'.format(lowest_sales))

print('Highest Sales: {}'.format(highest_sales))


# In[10]:


keys = ["Lowest Sales", "Highest Sales", "Sales Average", "Sales Total"]

data = [{"Lowest Sales":  lowest_sales},
         {"Highest Sales": highest_sales},
         {"Sales Average": sum_sales / cont_sales },
         {"Sales Total": sum_sales}
]

with open('result.csv', 'w+') as csv_file:
    spreadsheet = csv.DictWriter(csv_file, fieldnames=keys)
    spreadsheet.writeheader()
    spreadsheet.writerows(data)


# In[ ]:





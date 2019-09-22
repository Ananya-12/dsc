#!/usr/bin/env python
# coding: utf-8

# In[72]:


import numpy as np
import matplotlib.pyplot as plt 
import pandas as pd
import os
import zipfile
import seaborn as sn


# In[66]:


with zipfile.ZipFile("/home/ananya/Documents/ananya/dsc/telco-customer-churn.zip","r") as z:
    z.extractall(".")


# In[14]:


d=pd.read_csv("/home/ananya/Documents/ananya/dsc/telco-customer-churn.zip")
d.head()


# In[26]:


d.info()


# In[62]:


d.describe()


# In[ ]:





# In[46]:


#droping the duplicate row 
d=d.drop_duplicates(keep='first')

shape=d.shape
print('the number of categories is  and the total number of the customers are respectively')
print(shape[1],shape[0])


# In[54]:


gen=d['gender'].value_counts()
print('Total number of males and female are respectively', gen[0] ,' and ' , gen[1])

sen=d['SeniorCitizen'].value_counts()
print('Total no of senior citizen',sen[1])

sen=d['PaperlessBilling'].value_counts()
print('number of customer applyong for paperless billing ' , sen[0])


#do the same for others aswell 


# In[45]:


sub=d.columns
print('The column of the data are:' , )


# In[55]:


#checking for missing data 
d.isnull().sum()


# In[57]:


#the type f data stored in each category 
d.dtypes


# In[1]:


#fig, ax = plt.subplots()
#ax.hist(d['tenure'],10)


# In[2]:


#sn.scatterplot(x='MonthlyCharges',y='tenure',data=d)


# In[ ]:




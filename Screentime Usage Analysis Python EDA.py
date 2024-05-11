#!/usr/bin/env python
# coding: utf-8

# In[8]:


import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go


# In[10]:


data = pd.read_csv(r'C:\Users\bhato\Downloads\Screentime.csv')
print(data.head())


# In[11]:


data.isnull().sum()


# In[12]:


print(data.describe())


# In[13]:


figure = px.bar(data_frame=data, 
                x = "Date", 
                y = "Usage", 
                color="App", 
                title="Usage")
figure.show()


# In[14]:


figure = px.bar(data_frame=data, 
                x = "Date", 
                y = "Notifications", 
                color="App", 
                title="Notifications")
figure.show()


# In[15]:


figure = px.bar(data_frame=data, 
                x = "Date", 
                y = "Times opened", 
                color="App",
                title="Times Opened")
figure.show()


# In[16]:


figure = px.scatter(data_frame = data, 
                    x="Notifications",
                    y="Usage", 
                    size="Notifications", 
                    trendline="ols", 
                    title = "Relationship Between Number of Notifications and Usage")
figure.show()


# In[ ]:





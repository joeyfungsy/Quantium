#!/usr/bin/env python
# coding: utf-8

# ## Background
# One of the client, Category Manager for Chips, wants to have a better understanding on who their target customers are and what their purchasing behaviours are. As a data analyst in the Quantium's retail team, the goal for us is to get a supermarket's strategic plan for the chip category in the next half year by considering what metrics would be helpful to describe the customers' purchasing behavior. 
# 
# ### Key
# - customer segments 
# - chip puchasing behavior
# 
# 

# In[2]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go


# In[3]:


trans_data = pd.read_excel('https://insidesherpa.s3.amazonaws.com/vinternships/companyassets/32A6DqtsbF7LbKdcq/QVI_transaction_data.xlsx')


# In[4]:


trans_data.head(5)


# In[5]:


# Noticed that the format of the Date Column in transaction_data is off
# Changing to the right format
trans_data['DATE'] = pd.to_datetime(trans_data['DATE'], errors = 'coerce', unit = 'd', origin = '1900-01-01')
trans_data.head(5)


# In[6]:


# check to see if there are any missing values for the transaction data
trans_row_missing = trans_data.isnull().sum(axis=1)/trans_data.shape[1]
print(trans_row_missing[trans_row_missing>0.8])
# no missing values 


# In[7]:


cust_data = pd.read_csv('https://insidesherpa.s3.amazonaws.com/vinternships/companyassets/32A6DqtsbF7LbKdcq/QVI_purchase_behaviour.csv')


# In[8]:


cust_data.head(5)


# In[9]:


# check to see if there are any missing values for the transaction data
cust_row_missing = cust_data.isnull().sum(axis=1)/cust_data.shape[1]
print(cust_row_missing[cust_row_missing>0.8])
# no missing values 


# In[10]:


# Combine the 2 tables 
com_data = pd.merge(trans_data, cust_data, on = 'LYLTY_CARD_NBR', how = 'left')
com_data.head(5)


# In[11]:


# Only want the chip products in the table -- goal of our project 
chips_data = com_data[com_data['PROD_NAME'].str.contains('Chip') == True].copy()
chips_data.head(5)


# In[12]:


chips_data['PROD_NAME'].count()


# In[13]:


# Remove unnecessary information from the product name -- weight in this case
prod_name_split = chips_data["PROD_NAME"].str.replace(r'([0-9]+[gG])','').str.replace(r'[^\w]', ' ').str.split()
prod_name_split


# ### General Summary of the Products: 
# To see what kinds of chips are most selling:
# Thins chips
# favour: Corn, Salt 

# In[15]:


#initializing dictionary 
counted_word = {}

#counting number of times each word comes up in the list of words
def word_count(line):
    for word in line:
        if word not in counted_word:
            counted_word[word] = 1
        else:
            counted_word[word] += 1
            
product_list = prod_name_split.apply(lambda line: word_count(line))
print(pd.Series(counted_word).sort_values(ascending=False))


# In[16]:


chips_data.describe()


# In[19]:


# check to see if there are any outliers 
chips_data.sort_values(by = 'PROD_QTY',ascending = False).head(5)


# In[20]:


chips_data['DATE'].describe()


# ### Summary of the transaction 
# This table records the transaction history from July 3 2018 to July 2 2019, exactly 1 year. There are total 49770 transactions on chips purchases.

# In[21]:


# group the purchases by months in the year 
chips_month = chips_data.groupby('DATE')[['TXN_ID']].count().reset_index()
chips_month


# In[22]:


fig6 = px.line(chips_month,chips_month['DATE'],chips_month['TXN_ID'])
fig6.update_layout(title='Transactions over time',title_x=0.5)
fig6.show()


# ## Time 
# Dec 2018 at the top

# In[23]:


chips_month_2 = chips_data.groupby(["LIFESTAGE", "PREMIUM_CUSTOMER",'DATE'])[['TXN_ID']].count().reset_index()
chips_month_2


# #chips_member_2.loc[chips_member_2['PREMIUM_CUSTOMER'] == 'Budget']
# fig7 = px.bar(chips_month_2, x = chips_month_2.loc[chips_month_2['DATE'] == 'Dec 2018'],
#                             y = chips_month_2['TXN_ID'] , barmode = 'stack', color="PREMIUM_CUSTOMER", 
#                           title = 'Proportion of Sales')
# fig7.update_layout(title_x = 0.5)
# fig7.show()

# ### Customer Behavior
# 

# In[24]:


# Overview on the customers information vs sales 
chips_group= pd.DataFrame(chips_data.groupby(["LIFESTAGE", "PREMIUM_CUSTOMER"])["TOT_SALES"].agg(["sum", "mean"]))
chips_group.round(0)


# In[25]:


# Get a bar graph to have a better understanding of the information above 
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output


# In[26]:


chips_group_2 = chips_group.groupby(['LIFESTAGE','PREMIUM_CUSTOMER'])[['sum']].sum().reset_index()
chips_group_2


# In[27]:


fig = px.bar(chips_group_2, chips_group_2['LIFESTAGE'], chips_group_2['sum'], chips_group_2['PREMIUM_CUSTOMER'], text=(chips_group_2['sum']) )
fig.update_traces(texttemplate='%{text:.2s}', textposition='inside')
fig.update_layout(title='Customers Lifestage VS Total Sales (Jul 2018 - Jul 2019)',title_x=0.5,uniformtext_minsize=8, uniformtext_mode='hide')
fig.show()


# In[28]:


# Overview on the customers information -- numbers of customers by membership status 
chips_member= pd.DataFrame(chips_data.groupby(["LIFESTAGE", "PREMIUM_CUSTOMER"])['LYLTY_CARD_NBR'].agg(["count", "mean"]))
chips_member.round(0)


# In[29]:


chips_member_2 = chips_member.groupby(['LIFESTAGE','PREMIUM_CUSTOMER'])[['count']].sum().reset_index()
chips_member_2


# In[30]:


fig4 = px.bar(chips_member_2, x = chips_member_2['LIFESTAGE'], 
                            y = chips_member_2['count'] , barmode = 'stack', color="PREMIUM_CUSTOMER", 
                          title = 'Proportion of Sales')
fig4.update_layout(title_x = 0.5)
fig4.show()


# In[31]:


fig2 = px.pie(chips_member_2, chips_member_2['PREMIUM_CUSTOMER'], chips_member_2['count'], color_discrete_sequence=px.colors.sequential.RdBu)
#fig.update_traces(textposition='inside', textinfo='percent+label')
fig2.update_layout(title='Percentage of the Customers - Membership',title_x=0.5,uniformtext_minsize=8, uniformtext_mode='hide')
fig2.show()


# In[32]:


fig3 = px.pie(chips_member_2, chips_member_2['LIFESTAGE'], chips_member_2['count'], color_discrete_sequence=px.colors.sequential.RdBu)
#fig.update_traces(textposition='inside', textinfo='percent+label')
fig3.update_layout(title='Percentage of the Customers - Lifestage',title_x=0.5,uniformtext_minsize=8, uniformtext_mode='hide')
fig3.show()


# ## What can we tell from the graphs above
# 
# - Older Single/Couples customers has the highest total sales in combine, Retired customers comes 2nd and Older Familes customers comes 3rd 
# 
# To be more specific
# - Older Families who are also budgetted are the top customers with 45K sales in total, retireed customers who are mainstreamed comes 2nd with 41K and young singles/couples comes 3rd with 40K
# 
# In general, 
# - Most of our customers who purchased chips are elderly/retired or young families (reasons may be: (purchasing for themselves) more time to spend at home -> watching TV, (purchasing for others) have kids/youth at home, have parties/movies nights etc)
# - premium members have less interest in purchasing chases (reasons may be: health diets, vegen etc)
# -
# 
# Those groups should be our targetted customers 
# 

# In[31]:


chips_member_2.loc[chips_member_2['PREMIUM_CUSTOMER'] == 'Budget']


# In[ ]:





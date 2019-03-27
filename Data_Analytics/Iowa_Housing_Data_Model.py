#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

iowa_home_path = "/Users/simplyram/Documents/Python/Data_Analytics/train.csv"
home_data = pd.read_csv(iowa_home_path)

home_data.describe()


# In[2]:


sorted_df = pd.DataFrame({ 'built':home_data['YearBuilt'].value_counts(),
                          'remod':home_data['YearRemodAdd'].value_counts(),
                          'sold':home_data['YrSold'].value_counts(),
                          'price':home_data.groupby('YrSold').mean()['SalePrice'] }).sort_index(ascending=False)
sorted_df.round().fillna(0)
#sorted_df.describe()


#     sorted

# In[3]:


sor_DF = home_data[home_data['YrSold'] == 2010]['MoSold'].value_counts().sort_index()


# In[4]:


sor_DF


# In[5]:


relevant_years = home_data[~home_data['YearBuilt'].isnull()].copy()
years_grouped = relevant_years[['YrSold', 'SalePrice']].groupby('YrSold')


# In[6]:


relevant_years


# In[7]:


years_grouped


# In[8]:


years = pd.DataFrame()


# In[9]:


years


# In[10]:


for year in years_grouped.groups:
    group = years_grouped.get_group(year)
    years[year] = group.sort_values('SalePrice', ascending=False).head(5).reset_index()['SalePrice']


# In[11]:


years


# In[12]:


years_grouped.groups


# In[13]:


crisis = pd.DataFrame({'mean':years_grouped.median()['SalePrice'], 'top':years.mean()})
crisis /= crisis.mean()
crisis['dif'] = crisis['top'] - crisis['mean']
crisis


# In[14]:


y = home_data.SalePrice


# In[15]:


# Create the list of features below
feature_names = ["LotArea","YearBuilt","1stFlrSF","2ndFlrSF","FullBath","BedroomAbvGr","TotRmsAbvGrd"]

# select data corresponding to features in feature_names
X = home_data[feature_names] 


# In[16]:


# Review data
# print description or statistics from X
X.describe()

# print the top few lines
X.head()


# In[17]:


from sklearn.tree import DecisionTreeRegressor
#specify the model. 
#For model reproducibility, set a numeric value for random_state when specifying the model
iowa_model = DecisionTreeRegressor(random_state=1)

# Fit the model
iowa_model.fit(X,y)


# In[20]:


predictions = iowa_model.predict(X.head())
print(predictions)


# In[21]:


y.head()


# In[ ]:
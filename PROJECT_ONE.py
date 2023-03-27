#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
dataset= pd.read_csv('data.csv')
dataset


# In[3]:


dataset.head()


# In[4]:


dataset.tail()


# In[5]:


dataset.info()


# In[6]:


dataset.coluns = dataset.columns.str.replace(' ','_')
dataset


# In[8]:


actual_data =dataset.dropna()
actual_data


# In[10]:


new_data =dataset.dropna()
new_data


# ###  After using the dropna method, it eliminated the null sets in the code.So the fillna method will be called to call back the removed cells with the mean,mode and median distribution.
# 
# # AN INFERENCE ON THE ENTIRE DATA GIVEN
# 
# #### The inference provided the statistical breakdownof all elements provided in the csv file.Some of these inferences include the standard deviation , mean and count.
# 
# 
# 
# 

# In[11]:


dataset.describe()


# In[12]:


dataset.columns


# #  FINDING THE MODE OF THE VARIOUS PROPERTIES
# 

# In[20]:


dataset.columns= dataset.columns.str.replace(' ','_')


# In[21]:


mod_fa=dataset.fixed_acidity.mode()
mod_va=dataset.volatile_acidity.mode()
mod_ca=dataset.citric_acid.mode()
mod_rs=dataset.residual_sugar.mode()
mod_chl=dataset.chlorides.mode()
mod_fsd=dataset.free_sulfur_dioxide.mode()
mod_tsd=dataset.total_sulfur_dioxide.mode()
mod_dens=dataset.density.mode()
mod_pH=dataset.pH.mode()
mod_sul=dataset.sulphates.mode()
mod_alc=dataset.alcohol.mode()
mod_qua=dataset.quality.mode()

print(f"THE MODE OF THE VARIOUS COLUMNS:",end='\n\n')
print(f'fixed_acidity: {mod_fa}')
print(f'volatile_acidity: {mod_va}')
print(f'citric_acid: {mod_ca}')
print(f'residual_sugar: {mod_rs}')
print(f'chlorides: {mod_chl}')
print(f'free_sulfur_dioxide: {mod_fsd}')
print(f'total_sulfur_dioxide: {mod_tsd}')
print(f'density: {mod_dens}')
print(f'pH: {mod_pH}')
print(f'sulphates: {mod_sul}')
print(f'alcohol: {mod_alc}')
print(f'quality: {mod_qua}')


# # FINDING THE MEAN OF THE VARIOUS PROPERTIES
# 

# In[22]:


mean_fa=dataset.fixed_acidity.mean()
mean_va=dataset.volatile_acidity.mean()
mean_ca=dataset.citric_acid.mean()
mean_rs=dataset.residual_sugar.mean()
mean_chl=dataset.chlorides.mean()
mean_fsd=dataset.free_sulfur_dioxide.mean()
mean_tsd=dataset.total_sulfur_dioxide.mean()
mean_dens=dataset.density.mean()
mean_pH=dataset.pH.mean()
mean_sul=dataset.sulphates.mean()
mean_alc=dataset.alcohol.mean()
mean_qua=dataset.quality.mean()

print(f"THE MEAN OF THE VARIOUS COLUMNS:",end='\n\n')
print(f'fixed_acidity: {mean_fa}')
print(f'volatile_acidity: {mean_va}')
print(f'citric_acid: {mean_ca}')
print(f'residual_sugar: {mean_rs}')
print(f'chlorides: {mean_chl}')
print(f'free_sulfur_dioxide: {mean_fsd}')
print(f'total_sulfur_dioxide: {mean_tsd}')
print(f'density: {mean_dens}')
print(f'pH: {mean_pH}')
print(f'sulphates: {mean_sul}')
print(f'alcohol: {mean_alc}')
print(f'quality: {mean_qua}')


# # FINDING THE MEDIAN OF THE VARIOUS PROPERTIES

# In[23]:


median_fa=dataset.fixed_acidity.median()
median_va=dataset.volatile_acidity.median()
median_ca=dataset.citric_acid.median()
median_rs=dataset.residual_sugar.median()
median_chl=dataset.chlorides.median()
median_fsd=dataset.free_sulfur_dioxide.median()
median_tsd=dataset.total_sulfur_dioxide.median()
median_dens=dataset.density.median()
median_pH=dataset.pH.median()
median_sul=dataset.sulphates.median()
median_alc=dataset.alcohol.median()
median_qua=dataset.quality.median()

print(f"THE MEDIAN OF THE VARIOUS COLUMNS:",end='\n\n')
print(f'fixed_acidity: {median_fa}')
print(f'volatile_acidity: {median_va}')
print(f'citric_acid: {median_ca}')
print(f'residual_sugar: {median_rs}')
print(f'chlorides: {median_chl}')
print(f'free_sulfur_dioxide: {median_fsd}')
print(f'total_sulfur_dioxide: {median_tsd}')
print(f'density: {median_dens}')
print(f'pH: {median_pH}')
print(f'sulphates: {median_sul}')
print(f'alcohol: {median_alc}')
print(f'quality: {median_qua}')



# # CORRELATION BETWEEN VARIOUS COLUMNS
# 
# ### This Correlation is after removing all Null Entries

# In[24]:


dataset.corr()


# # FILLING UP NULL ENTRIES WITH MEAN VALUES
# 
# ### The mean values that were found were used to replace all the null entries in the dataframe.
# 
# ### This was done using the fillna method.
# 
# #### This is more effective and sustainable than the dropna method which tends to reduce the number of columns by the number of null values dropped.

# In[27]:


dataset.columns=dataset.columns.fillna()
dataset


# In[26]:


import ydata_profiling
profile=ydata_profiling.ProfileReport(dataset)
profile


# In[ ]:





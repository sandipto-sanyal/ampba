# -*- coding: utf-8 -*-
"""
Name: Sandipto Sanyal
PGID: 12010004
"""
#!/usr/bin/env python
# coding: utf-8

# # Install necessary libraries

# In[1]:


get_ipython().system('pip install sqldf')
get_ipython().system('pip install pandasql')
get_ipython().system('pip install plotnine')
get_ipython().system('pip install palettable')


# # Import necessary Libraries

# In[2]:


get_ipython().run_line_magic('matplotlib', 'inline')
import pandas as pd
from pandasql import sqldf
from plotnine import *
import numpy as np


# # Load dataset

# In[3]:


df = pd.read_csv('Indian_cities.csv')
df.head()


# # Check for NaN values

# In[4]:


df.isna().sum()


# # Questions to address
# In this EDA we will address the below questions:
# 1. What is the statewise data collection statistics? For which states we have higher number of census data available?
# 1. What is the statewise distribution of effective_literacy_rate_female? Which state has the highest mean effective_literacy_rate_female?
# 1. Is there any striking relationship between total_graduates vs. sex_ratio?
# 1. What is the correlation between total_graduates and sex_ratio?

# ## Statewise datacollection statistics

# ### View the numerical statistics <a id='numerical_statistics'></a>

# In[5]:


df.state_name.value_counts()


# In[6]:


(ggplot(data=df)
 + aes(x='state_name')
 + geom_bar(fill='red')
 + theme(axis_text_x=element_text(size=7, rotation=90),
         figure_size=(10,2)
        )
 + ggtitle('Number of census data per state')
).draw()


# <b>Inference: </b>We can see that West Bengal and Uttar Pradesh have highest number of census data followed by Andhra Pradesh, Maharashtra.

# ## Statewise distribution of effective_literacy_rate_female

# In[7]:


(ggplot(data=df)
 + aes(x='effective_literacy_rate_female', fill='state_name')
 + geom_histogram()
 + facet_wrap('state_name', nrow=5, )
 + theme(axis_text_x=element_text(size=7, rotation=90),
         figure_size=(10,7)
        )
 + ggtitle('Statewise distribution of effective_literacy_rate_female')
).draw()


# <b>Inference: </b>Most of the states show a left skewed data distribution for effective_literacy_rate_female. Tamil Nadu shows somewhat a normal distribution and it ranges from 75 to 100 percent effective_literacy_rate_female

# ### State with highest mean effective_literacy_rate_female

# In[8]:


sql = '''
select
state_name,
avg(effective_literacy_rate_female) as average_effective_literacy_rate_female,
count(state_name) as count_state_name
from df
group by state_name
order by count_state_name desc, average_effective_literacy_rate_female desc
'''
sqldf(sql)


# <b>Inference: </b>Though in this dataset we can see that Mizoram is a clear winner in average effective_literacy_rate_female but is this list reliable? It is already seen [here](#numerical_statistics) that Mizoram has only 1 city surveyed in Census. As per Mizoram (India): Districts & Towns - Population Statistics, Charts and Map. (n.d.). Retrieved April 15, 2020, from http://www.citypopulation.de/php/india-mizoram.php it has quite a large number of cities and towns so our dataset might not be the actual representation of the whole population of the state.<br>
# To be on the safe side we also include the number of census data available alongwith the above data.

# # Relationship between sex_ratio vs. total_graduates
# We will view the relationship with log(total_graduates) due to the range of values

# In[9]:


(ggplot(data=df)
 + aes(x='total_graduates', y='sex_ratio')
 + geom_jitter()
 + scale_x_log10()
 + theme(axis_text_x=element_text(size=7, rotation=90),
         figure_size=(6,3)
        )
 + labs(x='log(Total_graduates)')
 + ggtitle('Sex ratio vs. log(Total_graduates)')
).draw()


# ## Create a log transform for total_graduates

# In[10]:



df['log_total_graduates'] = np.log10(df['total_graduates'])


# In[11]:


df[['sex_ratio', 'log_total_graduates']].corr()


# <b>Inference: </b>There is a very small negative correlation between sex_ratio and log_total_graduates

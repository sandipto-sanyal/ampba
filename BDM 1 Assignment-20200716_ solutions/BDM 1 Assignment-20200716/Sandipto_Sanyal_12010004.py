#!/usr/bin/env python
# coding: utf-8

# # Name: Sandipto Sanyal
# # PGID: 12010004

# # Install findspark

# In[1]:


#!pip install findspark


# # Import necessary libraries

# In[2]:


import findspark
findspark.init()
import os
from pyspark import SparkContext
import csv
from StringIO import StringIO
import numpy as np


# # Create SparkContext

# In[3]:


sc = SparkContext(master="local", appName="Question 1")


# # Define a function to read the csv and split the lines

# In[4]:


def split(line):
    """
    Operator function for splitting a line with csv module
    """
    reader = csv.reader(StringIO(line))
    return reader.next()


# # Question 1

# ## Create RDDs of the input

# In[5]:


users_link = r'file:///home/cloudera/Desktop/git/big_data_management1/BDM 1 Assignment-20200716/users.csv'
transactions_link = r'file:///home/cloudera/Desktop/git/big_data_management1/BDM 1 Assignment-20200716/transactions.csv'
users_rdd = sc.textFile(users_link).cache()
transactions_rdd = sc.textFile(transactions_link).cache()


# ## Make transformations of the data
# Below we make some transformations of the dataset so that it renders into a CSV format.

# In[6]:


users_rdd = users_rdd.map(split)
transactions_rdd = transactions_rdd.map(split)


# In[7]:


users_rdd.collect()


# In[8]:


transactions_rdd.collect()


# ## a) Count of unique locations where each product is sold

# ### Create RDDs userid|location and userid|product to perform join on userid

# In[9]:


def create_userid_location_rdd(row):
    data = [row[0], row[3]]
    return data
def create_userid_product_rdd(row):
    data = [row[2],row[4], float(row[3])]
    return data
userid_location_rdd = users_rdd.map(create_userid_location_rdd)
userid_product_rdd = transactions_rdd.map(create_userid_product_rdd)


# In[10]:


joined_rdd = userid_location_rdd.rightOuterJoin(userid_product_rdd)


# In[11]:


joined_rdd.collect()


# In[12]:


grouped_rdd = joined_rdd.map(lambda row:(row[1][1],row[1][0])).groupByKey().collect()
grouped_rdd


# In[13]:


print("Count of unique locations where each product is sold:")
[(items, (np.unique(np.array((list(locations))))).shape[0]) for (items, locations) in grouped_rdd]


# ## b) Products bought by each user
# To perform this we will make use of the joined_rdd that we created earlier in step a

# In[14]:


grouped_rdd = joined_rdd.map(lambda row: (row[0],row[1][1])).groupByKey()
print('Products bought by each user:')
([(userid, list(items)) for (userid, items) in grouped_rdd.collect()])


# # c) Total spending done by each user on each product
# To perform this we take help of the userid_product_rdd

# In[15]:


userid_product_rdd.collect()


# In[16]:


spending_user_item = userid_product_rdd.map(lambda row: ((row[0],row[1]),row[2])).groupByKey().sortByKey()
print('Total spending done on each product by each user::')
([(key[0],key[1],sum(list(value))) for (key, value) in spending_user_item.collect()])


# # Question 2

# ## Read the CSV file and parse into new separated lines

# In[17]:


olympics_link = r'file:///home/cloudera/Desktop/git/big_data_management1/BDM 1 Assignment-20200716/olympics.csv'
olympics_rdd = sc.textFile(olympics_link, use_unicode=False).cache()
olympics_rdd = olympics_rdd.map(split).map(lambda row: row[0].split('\t'))


# In[18]:


olympics_rdd.first()


# <font color='red'>Assuming columns are: player name, age, country, year, date, category, gold, silver, bronze, total

# ## a) Total medals that each country won in particular sport

# In[19]:


total_medals = olympics_rdd.map(lambda row: [(row[2],row[5]), int(row[9])]).groupByKey().sortByKey().collect()
print('Total medals by country by sport')
([(key[0], key[1], sum(list(value))) for (key, value) in total_medals])


# # b) India medals in each olympic game

# In[20]:


india_medals = olympics_rdd.filter(lambda row: row[2]=='India').map(lambda row:[(row[2],row[3]), int(row[9])]).groupByKey().sortByKey().collect()
print('Number of India medals in each olympic')
[(key[0], key[1], sum(list(value))) for (key, value) in india_medals]


# # c) Top 3 countries by total medal by each olympic games

# In[21]:


# first group by year country and total medals tally
country_year_medals_rdd = olympics_rdd.map(lambda row:[(row[3],row[2]),int(row[9])]).groupByKey().map(lambda row: (row[0][0],sum(list(row[1])),row[0][1]))
# sort the RDD based on year and total medals
country_year_medals_rdd = country_year_medals_rdd.sortBy(lambda row: (row[0],row[1]),ascending=False)
# group the RDD based on year
country_year_medals_rdd = country_year_medals_rdd.groupBy(lambda row: row[0]).map(lambda row: (row[0],list(row[1])[0:3]))
country_year_medals_rdd.collect()


# In[22]:


sc.stop()


# In[ ]:





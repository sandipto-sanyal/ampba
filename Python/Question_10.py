# -*- coding: utf-8 -*-
"""
Name: Sandipto Sanyal
PGID: 12010004
"""
#!/usr/bin/env python
# coding: utf-8

# # Install necessary libraries

# In[1]:


get_ipython().system('pip install pandasql')
get_ipython().system('pip install plotnine')
get_ipython().system('pip install palettable')
get_ipython().system('jupyter nbextension enable --py --sys-prefix widgetsnbextension')
get_ipython().system('pip install gmaps')
get_ipython().system('jupyter nbextension enable --py --sys-prefix gmaps')


# # Import Libraries

# In[2]:

get_ipython().run_line_magic('matplotlib', 'inline')
import pandas as pd
import os
from plotnine import *
from datetime import datetime
import matplotlib.pyplot as plt
import matplotlib
matplotlib.style.use('ggplot')
from pandasql import sqldf


# # Set path for datasets

# In[3]:


path = 'datasets'
df = pd.read_csv(os.path.join(path, 'earthquake.csv'))


# # Display sample of data

# In[4]:


display(df.head())


# # Get basic descriptive statistics

# In[5]:


df.describe()


# # Get column datatypes

# In[6]:


df.dtypes


# # Convert date time to datetime object

# In[7]:


def convert_to_date_time(n):
    applicable_formats = ['%m/%d/%Y %H:%M:%S',
                          '%Y-%m-%dT%H:%M:%S.%fZ'
                         ]
    try:
        return datetime.strptime(n,applicable_formats[0])
    except:
        try:
            return datetime.strptime(n.split(' ')[0], applicable_formats[1])
        except Exception as e:
            print("Error: {}".format(e))
df['datetime'] = df["Date"] + " " + df["Time"]
df['datetime'] = df['datetime'].apply(convert_to_date_time)
df.head()


# # Find columns with NaNs
# We are checking which columns contain NaN values. This helps us to understand whether that particular column is worth studying for or not.

# In[8]:


df.isna().sum().sort_values(ascending=False)


# # Remove NaN from Magnitude Type
# We will remove rows containing NaN in Magnitude Type as it will interfere with analysis later

# In[9]:


df = df[~df['Magnitude Type'].isna()]


# # Univariate data analysis of categorical columns

# ## Type
# Here we try to visualize the distribution of Type of earthquake in our dataset

# In[10]:


(ggplot(data=df) +
 aes(x='Type') +
 geom_bar() +
 ggtitle('distribution of Type of earthquake')
).draw()


# <b>Inference: </b>We can see that most of the data belong to type Earthquake. According to the categories we assume that Earthquake means natural earthquake.

# # Univariate analysis of Continuous variable

# ## Magnitude

# In[11]:


g1 = (ggplot(data=df)
     + aes(x='Magnitude')
     + geom_histogram(bins=20) 
     + theme(figure_size=(6,4))
     + labs(title="Distribution of Magnitude"))

g2 = (ggplot(data=df)
 + aes(x='Magnitude', fill="Magnitude Type")
 + geom_histogram(bins=20)
 + facet_wrap("Magnitude Type", scales="free")
 + theme(figure_size=(10,7), panel_spacing_y=0.3, panel_spacing_x=0.5)
 + labs(title="Distribution of Magnitude for different Magnitude Type")
)


# In[12]:


g1.draw()


# In[13]:


g2.draw()


# <b>Inference: </b>From the above plots we can conclude below:
# 1. Most of the earth quakes are of magnitude between 5.5 to 6.
# 1. Our dataset consists of different Magnitude Type. From the 2nd plot it is evident that some Magnitude type are dedicated to measure earthquakes of magnitude lower than 5.6 while some are dedicated for magnitude higher than 5.6.

# # View yearwise variations

# ## Group data by year
# Below we will group our data to find the yearwise mean of the magnitudes

# In[14]:


sql = """
SELECT 
strftime("%Y", datetime) AS YEAR,
AVG(Magnitude),
COUNT(Magnitude)
from
df
GROUP BY YEAR
"""
yearwise_mean_magnitude = sqldf(sql)
yearwise_mean_magnitude['YEAR'] = pd.to_datetime(yearwise_mean_magnitude['YEAR'], format='%Y')
yearwise_mean_magnitude.head()


# ## View the chart
# Below we will plot yearwise mean magnitude against time

# In[15]:


figure = plt.figure(figsize=(7,5))
plt.plot(yearwise_mean_magnitude['YEAR'], yearwise_mean_magnitude['AVG(Magnitude)'])
plt.xlabel('Year')
plt.ylabel('Mean magnitude')
plt.title('Variation of mean magnitude w.r.t year')
plt.show()


# <b>Inference: </b>At first glance it appears the mean of the magnitude of the earthquakes dropped drastically in and around 1970's. But a careful observation will reveal that the drop is only 0.25 in magnitude.

# ## View yearwise variation of number of earthquakes

# In[16]:


figure = plt.figure(figsize=(7,5))
plt.plot(yearwise_mean_magnitude['YEAR'], yearwise_mean_magnitude['COUNT(Magnitude)'])
plt.xlabel('Year')
plt.ylabel('No. of earthquakes')
plt.title('Variation of no. of earth quakes w.r.t year')
plt.show()


# <b>Inference: </b>We can see that the variation of number of earthquakes in our dataset shows an increasing trend yearwise especially after 1980. This can be the result one of the below factors:
#  - Number of earthquakes has really increased as a result of natural phenomenon
#  - Use of sophisticated means of measurement methodology like Magnitude Type
#  - Advent of more monitoring stations
# 
# Let's delve deeper into this investigation

# # View variation in count of Magnitude Types with year

# ## Group count of Magnitude Type with year

# In[17]:


sql = """
SELECT 
strftime("%Y", datetime) AS YEAR,
`Magnitude Type`,
COUNT(`Magnitude Type`) AS COUNT
from
df
GROUP BY YEAR, `Magnitude Type`
ORDER BY YEAR DESC, COUNT DESC
"""
yearwise_count_magnitude_type = sqldf(sql)
yearwise_count_magnitude_type['YEAR'] = pd.to_datetime(yearwise_count_magnitude_type['YEAR'], format='%Y')
yearwise_count_magnitude_type.head()


# ## View chart
# Below we will visualize how with the advent of years we saw introduction of new Magnitude Types

# In[18]:


(ggplot(data=yearwise_count_magnitude_type)
+ aes(x='YEAR', y='COUNT', fill="Magnitude Type")
+ geom_col()
+ facet_wrap("Magnitude Type", scales="free_y")
+ theme(axis_text_x=element_text(angle=90), panel_spacing_x=0.5, figure_size=(10,5))
+ labs(title="Variation of Count of Magnitude Type over Years")
).draw()


# <b>Inference: </b>Here we are specifically concentrating into Magnitude Units which have high counts (> 100). The above plots show a clear example that over the years usage of magnitude type changed from "MB" with high usage in around 1970-1990 to "MWB", "MWC" in between 2000-2010 and "MWW" from 2010. This clearly indicates that the increase in number of earth quakes is in our dataset is perhaps mostly due to advent of new ways of measurements and hence higher number in reporting of the earthquakes.

# # View variation in count of Sources with year

# ## Group Source Counts with Year
# Let's dive to check whether with time the number of seismic network source for monitoring earthquakes has increased.

# In[19]:


sql = """
SELECT 
strftime("%Y", datetime) AS YEAR,
`Source`,
COUNT(`Source`) AS COUNT
from
df
GROUP BY YEAR, Source
ORDER BY COUNT DESC, YEAR DESC
"""
yearwise_count_Source = sqldf(sql)
yearwise_count_Source['YEAR'] = pd.to_datetime(yearwise_count_Source['YEAR'], format='%Y')


# ## View which sources reported high number of earthquakes

# In[20]:


yearwise_count_Source[yearwise_count_Source.COUNT >=100]


# ## View the charts
# Below we will visualize whether with time there was increase in sources

# In[21]:


(ggplot(data=yearwise_count_Source)
+ aes(x='YEAR', y='COUNT', fill="Source")
+ geom_col()
+ facet_wrap("Source", scales="free_y")
+ theme(axis_text_x=element_text(angle=90), panel_spacing_x=0.5, figure_size=(10,5))
+ labs(title="Variation of Count of Source over Years")
).draw()


# <b>Inference: </b>From the above plot it is seen that with the advent of years no such Source is contributing as such to the increase in earthquakes. The Source "US" shows consistently active from 1970-2010 and beyond with more or less uniform distribution. Thus the rise in number of earthquakes changes in Magnitude Type is probably playing as one of the key factors in measuring and reporting the earthquakes.

# # Conclusion
# From the above analysis we can conclude that with the advent of time changes and sophistication in Magnitude type is playing a key role in the rise in number of earthquakes.

# # Appendix
# Below we will see on Google earth map the locations of different earthquakes

# ## Create a new column to contain the coordinates as tuple

# In[22]:


df['coordinates'] = tuple(zip(df.Latitude, df.Longitude))
df.head()


# ## Create google maps HTML

# In[23]:


import gmaps
gmaps.configure(api_key='AIzaSyAv_ofDygjbc0mBeXg36rXiV5wzgEJoqL4')


# ## Get the locations

# In[27]:


locations = df.coordinates
weights = df.Magnitude
fig = gmaps.figure()
fig.add_layer(gmaps.heatmap_layer(locations, weights=weights))
fig


# <b>Inference: </b>The above map shows the distribution and intensity of the earthquakes around the globe.

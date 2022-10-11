#!/usr/bin/env python
# coding: utf-8

# In[6]:


import pandas as pd
import numpy as np
import time
df_washington = pd.read_csv('washington.csv')
df_chicago = pd.read_csv('chicago.csv')
df_nyc = pd.read_csv('new_york_city.csv')
df_nyc.head(2)


# In[17]:


df_chicago.head(2)


# In[16]:


df_washington.head(2)


# ## Creating new dataframes with the similar number of columns and names
# 

# In[15]:


new_df_chicago=df_chicago[['Start Time','End Time', 'Trip Duration', 'Start Station', 'End Station', 'User Type']]
new_df_chicago.head(2)


# In[14]:


new_df_nyc=df_nyc[['Start Time','End Time', 'Trip Duration', 'Start Station', 'End Station', 'User Type']]
new_df_nyc.head(2)


# In[13]:


new_df_washington=df_washington[['Start Time','End Time', 'Trip Duration', 'Start Station', 'End Station', 'User Type']]
new_df_washington.head(2)


# ## Concatenate the three data frames new_df_washington, new_df_nyc and new_df_chicago
# 

# In[18]:


import pandas as pd
import numpy as np
import time
new_df_washington = pd.DataFrame(new_df_washington)
new_df_nyc = pd.DataFrame(new_df_nyc)
new_df_chicago = pd.DataFrame(new_df_chicago)
bikeshare_df = pd.concat([new_df_washington, new_df_nyc, new_df_chicago])
bikeshare_df.tail()


# ## TO DO: display the most common month

# In[38]:



bikeshare_df['Start Time'] = pd.to_datetime(bikeshare_df['Start Time'])
bikeshare_df['month'] = bikeshare_df['Start Time'].dt.month
popular_month = bikeshare_df['month'].mode()[0]
print('Most Popular Start month:', popular_month)


# ## TO DO: display the most common week

# In[29]:


bikeshare_df['Start Time'] = pd.to_datetime(bikeshare_df['Start Time'])
bikeshare_df['week'] = bikeshare_df['Start Time'].dt.isocalendar().week
popular_week = bikeshare_df['week'].mode()[0]
print('Most Popular Start week:', popular_week)


# ## TO DO: display the most popular hour

# In[40]:


bikeshare_df['Start Time'] = pd.to_datetime(bikeshare_df['Start Time'])
bikeshare_df['hour'] = bikeshare_df['Start Time'].dt.hour
popular_hour = bikeshare_df['hour'].mode()[0]
print('Most Popular Start Hour:', popular_hour) 


# ## TO DO: display most commonly used start station

# In[41]:


Start_Station = bikeshare_df['Start Station'].mode()[0]
print('Most Popular Start Station:', Start_Station)


# ##   TO DO: display most commonly used end station

# In[45]:


End_Station = bikeshare_df['End Station'].mode()[0]
print('Most Popular End Station:', End_Station)


#  ## TO DO: display most frequent combination of start station and end station trip

# In[47]:



Common_station_combination = bikeshare_df.groupby(['Start Station','End Station']).size().idxmax()
print('Most frequent combination of start station and end station trip:', Common_station_combination)                                         


#  ## TO DO: display total travel time

# In[10]:


total_travel_time = df_washington['Trip Duration'].sum() + df_nyc['Trip Duration'].sum() +df_chicago['Trip Duration'].sum()
print('Total travel time in seconds is:', total_travel_time) 


# ## TO DO: display mean travel time

# In[30]:


mean_travel_time = bikeshare_df['Trip Duration'].mean()
print('The mean travel time in seconds is:',mean_travel_time)


#  ## TO DO: Display counts of user types

# In[16]:


number_of_user_types = bikeshare_df['User Type'].value_counts(ascending=True)
print(number_of_user_types)


# ## TO DO: Display counts of gender

# In[20]:


gender_split = df_chicago['Gender'].value_counts(ascending=True) + df_nyc['Gender'].value_counts(ascending=True) 
print(gender_split)


# ## TO DO: Display earliest, most recent, and most common year of birth

# In[20]:


import pandas as pd
import numpy as np
import time
df_bikeshare = pd.concat([df_nyc, df_chicago])
df_bikeshare.tail()


# In[28]:


oldest_user=df_bikeshare['Birth Year'].min()
youngest_user=df_bikeshare['Birth Year'].max()
common_age=df_bikeshare['Birth Year'].mode()
print('The ealiest year of birth is:', oldest_user)
print('The most recent year of birth is:',youngest_user)
print('The most common year of birth is:',common_age)


# In[ ]:



# The most common age is 1989

# the oldest year of birth is 1885
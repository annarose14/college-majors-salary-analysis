#!/usr/bin/env python
# coding: utf-8

# In[4]:


#import pandas into your notebook and read the .csv file. 
import pandas as pd
df = pd.read_csv('salaries_by_college_major.csv')


# In[5]:


df.head() # to peek at the top 5 rows of our dataframe. 


# In[6]:


#To see the number of rows and columns we can use the shape attribute
df.shape


# In[7]:


#We can access the column names directly with the columns attribute.

df.columns


# In[8]:


#Before we can proceed with our analysis
#we should try and figure out if there are any missing or junk data in our dataframe. 
#That way we can avoid problems later on. In this case,
#we're going to look for NaN (Not A Number) values in our dataframe. 
#NAN values are blank cells or cells that contain strings instead of numbers.
#Use the .isna() method and see if you can spot if there's a problem somewhere.


# In[9]:


df.isna()


# In[10]:


# Check the last couple of rows in the dataframe:


# In[11]:


df.tail()


# In[12]:


#We don't want this row in our dataframe. There's two ways you can go about removing this row. 
#The first way is to manually remove the row at index 50. 
#The second way is to simply use the .dropna() method from pandas.
#Let's create a new dataframe without the last row and examine the last 5 rows to make sure we removed the last row:


# In[13]:


clean_df = df.dropna()
clean_df.tail()


# In[14]:


#To access a particular column from a data frame we can use the square bracket notation,
clean_df['Starting Median Salary']


# In[15]:


#To find the highest starting salary 
clean_df['Starting Median Salary'].max()


# In[16]:


#The highest starting salary is $74,300. 
#But which college major earns this much on average? 
#For this, we need to know the row number or index so that we can look up the name of the major.
#Lucky for us, the .idxmax() method will give us index for the row with the largest value.


# In[17]:


clean_df['Starting Median Salary'].idxmax()


# In[18]:


#To see the name of the major that corresponds to that particular row, we can use the .loc (location) property.

clean_df['Undergraduate Major'].loc[43]


# In[19]:


clean_df['Undergraduate Major'][43]


# In[20]:


#If you don't specify a particular column you can use the .loc property to retrieve an entire row:
clean_df.loc[43]


# In[21]:


#The Highest Mid-Career Salary


# In[22]:


#If you have multiple lines in the same cell, 
#only the last one will get printed as an output automatically. 
#If you'd like to see more than one thing printed out, 
#then you still have to use a print statement on the lines above.


# In[23]:


print(clean_df['Mid-Career Median Salary'].max())
print(f"Index for the max mid career salary: {clean_df['Mid-Career Median Salary'].idxmax()}")
clean_df['Undergraduate Major'][8]


# In[24]:


#The Lowest Starting and Mid-Career Salary


# In[25]:


print(clean_df['Starting Median Salary'].min())
clean_df['Undergraduate Major'].loc[clean_df['Starting Median Salary'].idxmin()]


# In[26]:


clean_df.loc[clean_df['Mid-Career Median Salary'].idxmin()]


# Lowest Risk Majors
# 
# A low-risk major is a degree where there is a small difference between the lowest and highest salaries. In other words, if the difference between the 10th percentile and the 90th percentile earnings of your major is small, then you can be more certain about your salary after you graduate.
# 
# How would we calculate the difference between the earnings of the 10th and 90th percentile? Well, Pandas allows us to do simple arithmetic with entire columns, so all we need to do is take the difference between the two columns:

# In[27]:


clean_df['Mid-Career 90th Percentile Salary'] - clean_df['Mid-Career 10th Percentile Salary']


# or alternative method

# In[28]:


clean_df['Mid-Career 90th Percentile Salary'].subtract(clean_df['Mid-Career 10th Percentile Salary'])


# In[29]:


#We can add this to our existing dataframe with the .insert() method:


# In[30]:


spread_col = clean_df['Mid-Career 90th Percentile Salary'] - clean_df['Mid-Career 10th Percentile Salary']
clean_df.insert(1, 'Spread', spread_col)
clean_df.head()


# In[31]:


#Sorting by the Lowest Spread


# In[32]:


#To see which degrees have the smallest spread, we can use the .sort_values() method


# In[33]:


#And since we are interested in only seeing the name of the degree and the major,
#we can pass a list of these two column names to look at the .head() of these two columns exclusively.


# In[34]:


low_risk = clean_df.sort_values('Spread')
low_risk[['Undergraduate Major', 'Spread']].head()


# In[35]:


#Majors with the Highest Potential


# In[36]:


highest_potential = clean_df.sort_values('Mid-Career 90th Percentile Salary', ascending=False)
highest_potential[['Undergraduate Major', 'Mid-Career 90th Percentile Salary']].head()


# In[37]:


# Majors with the Greatest Spread in Salaries


# In[38]:


highest_spread = clean_df.sort_values('Spread', ascending=False)
highest_spread[['Undergraduate Major', 'Spread']].head()


# In[39]:


clean_df.groupby('Group').count()


# In[44]:


pd.options.display.float_format = '{:,.2f}'.format 
clean_df.groupby('Group').mean()


# Learnings
# Use .head(), .tail(), .shape and .columns to explore your DataFrame and find out the number of rows and columns as well as the column names.
# 
# Look for NaN (not a number) values with .findna() and consider using .dropna() to clean up your DataFrame.
# 
# You can access entire columns of a DataFrame using the square bracket notation: df['column name'] or df[['column name 1', 'column name 2', 'column name 3']]
# 
# You can access individual cells in a DataFrame by chaining square brackets df['column name'][index] or using df['column name'].loc[index]
# 
# The largest and smallest values, as well as their positions, can be found with methods like .max(), .min(), .idxmax() and .idxmin()
# 
# You can sort the DataFrame with .sort_values() and add new columns with .insert()
# 
# To create an Excel Style Pivot Table by grouping entries that belong to a particular category use the .groupby() method
# 
# 

# In[ ]:





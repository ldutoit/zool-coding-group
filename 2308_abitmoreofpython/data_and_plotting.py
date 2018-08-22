#!/usr/bin/env python

#This script is a very simple example of how to process data with python.
# The module pandas is very well suited for data structure... 

#Okay! We're going to look at a bike dataset fro Montreal.
#Is it a commuter city or a biking-for-fun city -- do people bike more on weekends, 
#or on weekdays?

#adapted from http://nbviewer.jupyter.org/github/jvns/pandas-cookbook/blob/master/cookbook/Chapter%204%20-%20Find%20out%20on%20which%20weekday%20people%20bike%20the%20most%20with%20groupby%20and%20aggregate.ipynb

import pandas as pd # pandas  is a python fo data strucre 
import matplotlib.pyplot as plt

plt.ion() # make plot appear each time



#loading the data, don't be afraid the help to understand more . help(pd.read_csv())
bikes = pd.read_csv('bikes.csv', sep=';', encoding='latin1', parse_dates=['Date'], dayfirst=True, index_col='Date')

#make a first plot to look at biking in the berri neighborhood 
bikes['Berri 1'].plot() 


# create a data frame only with the berri neighborhood to focus on it
type(berri_bikes) # Berri is a dataframe, an object defined by the panda library.
berri_bikes = bikes[['Berri 1']].copy() # it uses the copy method on this object

#look at the first 5 data points
berri_bikes[:5]


# We are now gonna transform these dates on weekdays to analyse the data in that way.
berri_bikes.index 
# we can see that there are only 310 days covered

# we can check which day of the month 
berri_bikes.index.day

# Or we can check which day of the week (mon-sun) 
berri_bikes.index.weekday


#Let's add a column weekday to our data frame
berri_bikes.loc[:,'weekday'] = berri_bikes.index.weekday
berri_bikes[:5]

# Let's count the number of bikes per day by summing the number of bikes
weekday_counts = berri_bikes.groupby('weekday').aggregate(sum)
weekday_counts


#replace this weekday numbers by actual week days
weekday_counts.index = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
weekday_counts



#and plot it
weekday_counts.plot(kind='bar')


#remember you also so this plot
bikes['Berri 1'].plot() 


#But python can do a lot more cool plots
# Are you curious? Surely there is something for your paper!
# Have a look to the link below. Alot of plots are visible
# and the code is always provided.
#https://matplotlib.org/gallery.html

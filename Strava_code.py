#!/usr/bin/env/python

import numpy as np 
import matplotlib.pyplot as plt 
import mysql.connector 
import pandas as pd
import pandasql as psql
#from psql import sqldf 
 

'''Loading in the Strava data'''

stravadf_old_headers = pd.read_csv(
'/Users/gracebreen/Python_files/Strava_Project/export_53215524/activities.csv',
header=0,
usecols=['Activity Date', 'Activity Type', 'Elapsed Time', 'Distance', 'Average Grade', 'Calories'])
#print(stravadf_old_headers.head(100))


'''Changing the names of some columns to remove spaces'''

stravadf = stravadf_old_headers.rename(columns={'Activity Type':'Activity_Type', 'Elapsed Time':'Elapsed_Time', 'Average Grade':'Average_Grade'})


selected_df = psql.sqldf("select Average_Grade, Distance from stravadf")
print(selected_df.head())

plt.figure()
plot = stravadf.plot(x="Average_Grade", y="Distance", style='o')
plot.set_xlabel("Average Gradient")
plot.set_ylabel("Distance, Kilometres")
plt.title("Distance of Strava Activities versus Average Gradient")
plt.show()
plt.savefig('Distance_versus_AvgGradient.png')

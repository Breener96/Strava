#!/usr/bin/env/python

import numpy as np 
import matplotlib.pyplot as plt 
import mysql.connector 
import pandas as pd 
#import pandasql as ps 

'''Loading in the Strava data'''

data = pd.read_csv(
'/Users/gracebreen/Python_files/Strava_Project/export_53215524/activities.csv',
usecols=['Activity Date', 'Activity Type', 'Elapsed Time', 'Distance', 'Average Grade', 'Calories'])
print(data.head(100))



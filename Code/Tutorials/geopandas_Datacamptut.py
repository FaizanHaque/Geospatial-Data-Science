# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 20:25:54 2019

@author: Home
"""

#tutorial link
#https://www.datacamp.com/community/tutorials/geospatial-data-python

import geopandas as gpd
import numpy as np
import pandas as pd
from shapely.geometry import Point

import missingno as msn

import seaborn as sns
import matplotlib.pyplot as plt

# Getting to know GEOJSON file:
country = gpd.read_file("../Data/gz_2010_us_040_00_5m.json")
country.head()


# =============================================================================
# type(country)
# type(country.geometry)
# type(country.geometry[0])
# =============================================================================
country.plot()
#Exclude Alaska and Hawaii for now
country[country['NAME'].isin(['Alaska','Hawaii']) == False].plot(figsize=(30,20), color='#3B3C6E');
florence = pd.read_csv('../data/stormhistory.csv')
florence.head()
# Notice you can always adjust the color of the visualization
msn.bar(florence, color='darkolivegreen');

florence.describe()
# dropping all unused features:
florence = florence.drop(['AdvisoryNumber','Forecaster','Received'], axis=1)
florence.head()
# Add "-" in front of the number to correctly plot the data:
florence['Long'] = 0 - florence['Long']
florence.head()
florence['coordinates'] = florence[['Long','Lat']].values.tolist()
florence.head()
# =============================================================================

# Change the coordinates to a geoPoint
florence['coordinates'] = florence['coordinates'].apply(Point)
florence.head()

florence = gpd.GeoDataFrame(florence,geometry='coordinates')
print("Mean wind speed of Hurricane Florence is {} mph and it can go up to {} mph maximum".format(round(florence.Wind.mean(),4),
                                                                                         florence.Wind.max()))
florence.plot(figsize=(20,10));
fig, ax = plt.subplots(1,figsize=(30,20))
#base = country[country['NAME'].isin(['Alaska','Hawaii']) == False].plot(ax=ax, color='#3B3C6E')
base = country[country['NAME'].isin(['Alaska','Hawaii']) == False].plot(ax=ax, color='#3B3C6E')
#plotting the hurricane position on top with red color to stand out:
# =============================================================================
# florence.plot(ax = base, color ='darkred', marker = "*", markersize = 10);
# fig, ax = plt.subplots(1,figsize(20,20))
# base = country[country['NAME'].isin(['Alaska','Hawaii'])== False].plot(ax=ax, color = '#3B3C6E')
# florence.plot(ax=base, column= 'Wind', marker = "<", markersize=10,cmap='cool',label='Wind speed(mph)")
# _ = ax.axis('off')      
# plt.legend()
# ax.set_title("Hurricane Florence in US Map", fontsize = 25)
# plt.set_title('Hurricance_footage.png', bbox_inches =' tight');
# fig, ax = plt.subplots(1, figsize=(20,20))
# =============================================================================
base = country[country['NAME'].isin(['Alaska','Hawaii']) == False].plot(ax=ax, color='#3B3C6E')
florence.plot(ax=base, column='Wind', marker="<", markersize=10, cmap='cool', label="Wind speed(mph)")
_ = ax.axis('off')
plt.legend()
ax.set_title("Hurricane Florence in US Map", fontsize=25)
plt.savefig('Hurricane_footage.png',bbox_inches='tight');      
               
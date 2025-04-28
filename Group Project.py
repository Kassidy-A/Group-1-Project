
#GROUP PROJECT

# Latex Project
###### With title, date, members, an intro

###############################################################################

# Step 1: Set up Environment

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

###############################################################################

#Step 2: Load and Clean the Data
## choose csv from canvas
df = pd.read_csv()


df.isnull().sum()      #checks for missing values
df.dropna(inplace=True)     #drops missing values
df.duplicated().sum       #checks for duplicate data
df.drop_duplicates(inplace=True)  

###############################################################################

# Step 3: Summary Stats, Descriptive Stats, and Correlation

#one line of code 
#df.describe()
#what do these stats tell you?

###############################################################################

# Step 4: Analysis

#what info you want to show from your group

#stats one column, depending on the data and what it means???????

###############################################################################

# Step 5: Visualization

    #Choose 1 or 2 (depends on the data)
#Histogram
#Boxplot
#Bar Chart

###############################################################################

# Step 6: Linear Regression Model

#line of best fit

###############################################################################

# Step 7: Other Analysis Ideas:

#KMeans, classification, z-score, IQR.
    











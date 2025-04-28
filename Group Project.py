
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
df = pd.read_csv("C:/Users/12516/Downloads/airline-safety.csv")


# Displaying the first few rows
print(df.head())
print("\n Data Info\n")
print(df.info())


print("\nMissing Values: ")
df.isnull().sum()      #checks for missing values
print(df.isnull().sum())


# check dataset shape
print(f"Dataset shapr {}")


df.dropna(inplace=True)     #drops missing values


duplicate_row = df.duplicated().sum       #checks for duplicate data
print(f"Number of duplication row {duplicate_row}")
if duplicate_row > 0:
    df = df.drop_duplication()
df.drop_duplicates(inplace=True)  


# Basic cleaning: removing leading/trailing spaces from column names
df.column = df.column.str.strip()

###############################################################################

# Step 3: Summary Stats, Descriptive Stats, and Correlation

#one line of code 

summary_stats = df.describe()
print("\n Summary Statistics: ")
print(summary_stats)
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
    











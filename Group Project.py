
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

# central tendency

mean_values = df.mean(numeric_only = True)
median_value = df.median(numeric_only = True)
mode_value = df.mode(numeric_only = True)

# description
std_value = df.std(numeric_only = True)
var_value = df.var(numeric_only = True)
range_value = df.max(numeric_only = True) - df.min(numeric_only = True)
iqr_value = df.quantile(0.75) - df.quantile(0.25)

# shapes

Skewness = df.skew(numeric_only = True)
kurtosis_vals = df.kurtosis(numeric_only  = True)


Stats.round(2) = pd.DataFrame({
    "Mean ": mean_value,
    "Median": median_value,
    "Mode": mode_value,
    "Standard Deviation": std_value,
    "Variance": var_value,
    "Range": range_value,
    "IQR": iqr_value,
    "Skewness": Skewness,
    "Kurtosis": Kurtosis_vals
})

# Display
print("Descriptive Statistics: ")
print(Stats.round(3))


correlations = df.corr(numeric_only = True)
print("Correlation Matrix")
print(correlation)

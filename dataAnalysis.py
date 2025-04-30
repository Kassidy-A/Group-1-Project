
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


# Load the original dataset
file_path = "C:/Users/12516/Downloads/drug-use-by-age.csv"  # Update path if needed
df = pd.read_csv(file_path)


# Initial inspection
print("Initial shape:", df.shape)
# 17 rows and 28 columns
print("\nData types:\n", df.dtypes)
# it data types for each column
print("\nMissing values:\n", df.isnull().sum())
# if it is all 0 implies there is not missing values for that column



df.drop_duplicates()
df = df.drop_duplicates()

# 2. Convert numeric columns to appropriate types
# for some datas such as 22-23 to a min age value
# we are going to use str.extract()
df['age_min'] = df['age'].str.extract(r'(\d+)').astype(int)
df.loc[df['age'] == '65+', 'age_min'] = 65

df=df.drop(columns= "age")

frequency_cols = [col for col in df.columns if 'frequency' in col]
df[frequency_cols] = df[frequency_cols].replace('-', pd.NA)
df[frequency_cols] = df[frequency_cols].apply(pd.to_numeric, errors='coerce')


print("\n New Data types : \n" , df.dtypes)

# SUmmary Statistics
summary_stats = df.describe()
print("\n Summary Statistics: ")
print(summary_stats)

# corrleation

corrleations = df.corr(numeric_only = True)
print("Correlation Matrix")
print(corrleations)


# 
plt.figure(figsize=(10, 6))
plt.hist(df['alcohol_use'], bins=10, color='skyblue', edgecolor='black')

plt.title('Distribution of Alcohol Use Across Age Groups')
plt.xlabel('Percentage Using Alcohol (%)')
plt.ylabel('Number of Age Groups')
plt.grid(axis='y', alpha=0.4)
plt.show()

plt.figure(figsize=(10, 6))
plt.hist(df['alcohol_frequency'], bins=10, color='purple', edgecolor='black')

plt.title('Distribution of Alcohol Use Across Age Groups')
plt.xlabel('Percentage Using Alcohol (%)')
plt.ylabel('Number of Age Groups')
plt.grid()
plt.show()


# Choose column to plot
col = 'alcohol_frequency'

# Prepare data: list of alcohol_frequency values per age group
age_groups = sorted(df['age_min'].dropna().unique())
data_by_age = [df[df['age_min'] == age][col].dropna() for age in age_groups]

# Create boxplot
plt.figure(figsize=(14, 6))
plt.boxplot(data_by_age, labels=age_groups)
plt.title('Alcohol Frequency by Age Group')
plt.xlabel('Age (Minimum of Age Range)')
plt.ylabel('Alcohol Frequency')
plt.grid()
plt.show()

# histrogram 
plt.figure(figsize=(12, 6))
plt.hist([df['alcohol_use'], df['marijuana_use']], 
         bins=8, 
         color=['royalblue', 'limegreen'], 
         label=['Alcohol', 'Marijuana'],
         edgecolor='black')

plt.title('Comparison of Alcohol vs. Marijuana Use Distributions')
plt.xlabel('Percentage Using Substance (%)')
plt.ylabel('Number of Age Groups')
plt.legend()
plt.grid(False)
plt.show()

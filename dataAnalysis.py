
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


# Plot sample sizes alongside usage rates
plt.figure(figsize=(12,4))
plt.bar(df['age_min'], df['n'], color='skyblue', alpha=0.7, label='Sample size (n)')
plt.plot(df['age_min'], df['alcohol_use']*100, 'r-', label='Alcohol use (%)')
plt.legend()
plt.title('Survey Sample Sizes vs. Alcohol Use Rates')
plt.xticks(rotation=45)
plt.show()

plt.figure(figsize=(10, 6))
plt.hist(df['alcohol_use'], bins=10, color='skyblue', edgecolor='black')

plt.title('Distribution of Alcohol Use Across Age Groups', fontsize=14)
plt.xlabel('Percentage Using Alcohol (%)', fontsize=12)
plt.ylabel('Number of Age Groups', fontsize=12)
plt.grid(axis='y', alpha=0.4)
plt.show()


# Choose one example frequency column to plot
col_to_plot = 'alcohol_frequency'

# Create a boxplot of frequency by age group
plt.figure(figsize=(12, 6))
plt.boxplot(x='age_min', y=col_to_plot, data=df)
plt.title(f'Boxplot of {col_to_plot} by Age Group')
plt.xlabel('Age (Minimum of Group)')
plt.ylabel('Frequency')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()



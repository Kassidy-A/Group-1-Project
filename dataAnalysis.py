
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
df.to_latex('df_table.tex',index = False)

# Initial inspection
print("Initial shape:", df.shape)
# 17 rows and 28 columns
print("\nData types:\n", df.dtypes)
# it data types for each column
print("\nMissing values:\n", df.isnull().sum())
# if it is all 0 implies there is not missing values for that column


# for xxx_use it means Percentage of those in an age group who used alcohol in the past 12 months
# for xxx_frequency it means Median number of times a user in an age group used alcohol in the past 12 months
df.drop_duplicates()
df = df.drop_duplicates()

# Convert numeric columns to appropriate types
# for some datas such as 22-23 to a min age value
# we are going to use str.extract()
df['age_min'] = df['age'].str.extract(r'(\d+)').astype(int)
df.loc[df['age'] == '65+', 'age_min'] = 65

# clean up the columns
frequency_cols = [col for col in df.columns if 'frequency' in col]
df[frequency_cols] = df[frequency_cols].replace('-', pd.NA)
df[frequency_cols] = df[frequency_cols].apply(pd.to_numeric, errors='coerce')

df.to_csv("data_cleaned.csv",index=False)
print("\n New Data types : \n" , df.dtypes)

# SUmmary Statistics
summary_stats = df.describe()
print("\n Summary Statistics: ")
print(summary_stats)

summary_stats.to_latex('summary_statistics.tex', index=False)



# corrleation

corrleations = df.corr(numeric_only = True)
print("Correlation Matrix")
print(corrleations)
corrleations.to_latex("correlations.tex",index=False)

# create a visualzation
# Generate histogram of alcohol use percentages
# Using 10 bins for optimal distribution representation
plt.figure(figsize=(10, 6))
plt.hist(df['alcohol_use'], bins=10, color='skyblue', edgecolor='black')
plt.title('Distribution of Alcohol Use Across Age Groups')
plt.xlabel('Percentage Using Alcohol (%)')
plt.ylabel('Number of Age Groups')
plt.grid(axis='y', alpha=0.4)
plt.show()


# Alcohol Frequency by Age Group (Bar Plot)
plt.figure(figsize=(10, 6))
plt.bar(df['age'],df['alcohol_frequency'], color='cyan', edgecolor='black')
plt.title('Distribution of Alcohol Use Across Age Groups')
plt.xlabel('Age Groups')
plt.ylabel('Alcohol_frequency')
plt.grid(axis='y', alpha=0.4)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Alcohol Use by Age Group (Bar Plot)
plt.figure(figsize=(12, 8))
plt.bar(df['age'], df['alcohol_use'], color='teal', edgecolor='black')
plt.title('Alcohol Use by Age Group')
plt.xlabel('Age Group')
plt.ylabel('Percentage Who Used Alcohol')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


#Alcohol Use Prevalence by Age Group (Bar Plot)
plt.scatter(df['marijuana_frequency'], df['marijuana_use'], color='lime')
plt.xlabel('Frequency')
plt.ylabel('Use')
plt.title('Scatter plot of Marijunan Frequency vs. Use')
plt.show()


# First plot (for the first 5 variables)
plt.figure(figsize=(10, 6))
plt.boxplot([df['marijuana_use'], df['alcohol_use'], df['cocaine_use'],
             df['crack_use'], df['heroin_use']])

# Adding titles and labels for the first plot
plt.title('Boxplot of Marijuana, Alcohol, Cocaine, Crack, and Heroin Use')
plt.ylabel('Use Percentage')
plt.xticks([1, 2, 3, 4, 5], ['Marijuana Use', 'Alcohol Use', 'Cocaine Use', 'Crack Use', 'Heroin Use'])
plt.grid(True)
# Show the first plot
plt.show()

# Second plot (for the remaining 4 variables)
plt.figure(figsize=(10, 6))
plt.boxplot([df['hallucinogen_use'], df['inhalant_use'], df['pain_releiver_use'], df['oxycontin_use']])

# Adding titles and labels for the second plot
plt.title('Boxplot of Hallucinogen, Inhalant, Pain Reliever, and Oxycontin Use')
plt.ylabel('Use Percentage')
plt.xticks([1, 2, 3, 4], ['Hallucinogen Use', 'Inhalant Use', 'Pain Reliever Use', 'Oxycontin Use'])
plt.grid(True)
plt.show()








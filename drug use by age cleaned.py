# -*- coding: utf-8 -*-
"""
Created on Wed Apr 30 12:20:30 2025

@author: dance
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the original dataset
file_path = 'drug-use-by-age.csv'  # Update path if needed
df = pd.read_csv(file_path)

# --- Cleaning ---

# Step 1: Replace '-' with NaN
df_cleaned = df.replace('-', pd.NA)

# Step 2: Convert frequency columns to numeric
frequency_columns = [col for col in df_cleaned.columns if 'frequency' in col]
for col in frequency_columns:
    df_cleaned[col] = pd.to_numeric(df_cleaned[col], errors='coerce')

# Step 3: Clean 'age' column (remove extra spaces)
df_cleaned['age'] = df_cleaned['age'].str.strip()

# Save cleaned version
output_path = 'drug_use_by_age_cleaned.csv'
df_cleaned.to_csv(output_path, index=False)

print(f"Cleaned file saved to: {output_path}")

# --- Optional: Plotting ---

# Example: Plot marijuana use vs age
plt.figure(figsize=(12,6))
sns.barplot(x='age', y='marijuana_use', data=df_cleaned, palette='Greens_d')
plt.xticks(rotation=45)
plt.title('Marijuana Use by Age Group')
plt.xlabel('Age Group')
plt.ylabel('Percentage Using Marijuana (%)')
plt.tight_layout()
plt.show()
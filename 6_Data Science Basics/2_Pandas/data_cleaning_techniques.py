# Handling missing values
# Removing duplicates
# Renaming columns

import pandas as pd

df = pd.read_csv("../assets/data1.csv")

# Check the number of missing values
print("Number of missing values: ", df.isnull().sum())

# Fill Missing Values
df['age'] = df['age'].fillna(40)

# Drop Rows with missing values
df = df.dropna()

# Check for duplicates
print("Number of duplicates: ", df.duplicated().sum())

# Remove duplicates
df = df.drop_duplicates()

# Rename columns
df = df.rename(columns={"age": "How old"})

# Transforming Data
df['name'] = df['name'].str.upper()  # Convert the string values of the column to uppercase

# Normalize Numeric Data
df['age'] = (df['age'] - df['age'].mean()) / df['age'].std()
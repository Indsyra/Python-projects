import pandas as pd

# Load CSV File
df = pd.read_csv("../assets/data.csv")

# Print the 5 first rows
print(df.head())

# Inspecting Data
# Shape of the Dataframe
print(df.shape)

# Data Types
print(df.dtypes)

# Summary Statistics
print(df.describe())
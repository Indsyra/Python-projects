# Data Analysis: Process of inspecting, cleaning, transforming and modeling data to extract meaningful information and support decision making.

import pandas as pd
import matplotlib.pyplot as plt

# Load Sales Data
data = pd.read_csv("..\\assets\\data_analysis\\sales_data.csv")

print(data.head())

# Summary of Dataset
print(data.info())

# Statistical Summary
print(data.describe())

# Check for missing values
print(data.isnull().sum())

# Check for duplicates
print(data.duplicated().sum())

# Cleaning and Transforming Data

# Fill Missing Values
data["Product_Category"] = data["Product_Category"].fillna("Unknown")

# Drop Rows with missing values
data = data.dropna()

# Convert Date Column to Datetime
data["Date"] = pd.to_datetime(data["Date"])

data["Sales_Amount"] = pd.to_numeric(data["Sales_Amount"], errors="coerce")

# Add a Year-Month column
data["Year_Month"] = data['Date'].dt.to_period('M')

# Add a Revenue Column (if Quantity and Price are available)
data["Revenue"] = data["Quantity"] * data["Price"]

# Total Sales by Month
monthly_sales = data.groupby("Year_Month")["Sales_Amount"].sum()
print(monthly_sales)


# Top Products
top_products = data.groupby("Product_Name")["Revenue"].sum().sort_values(ascending=False).head()
print(top_products)

# Plot Monthly Sales
monthly_sales.plot(kind="bar", figsize=(10, 6), color="skyblue")
plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)
plt.show()
#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd

# 1. Load dataset
df = pd.read_csv("sales_data.csv")

# 2. Display first few rows
print("First 5 rows of the dataset:")
print(df.head(), "\n")

# 3. Basic information
print("Dataset Info:")
print(df.info(), "\n")

print(f"Rows: {df.shape[0]}, Columns: {df.shape[1]}\n")

# 4. Handle missing values
# Fill missing Quantity with 0
df['Quantity'] = df['Quantity'].fillna(0)

# Fill missing Total_Sales using Quantity * Price
df['Total_Sales'] = df['Total_Sales'].fillna(df['Quantity'] * df['Price'])

# 5. Remove duplicate rows (if any)
df = df.drop_duplicates()

# 6. Sales Analysis
total_revenue = df['Total_Sales'].sum()
average_sales = df['Total_Sales'].mean()
max_sale = df['Total_Sales'].max()
min_sale = df['Total_Sales'].min()

# Best-selling product (by total sales)
best_product = (
    df.groupby('Product')['Total_Sales']
    .sum()
    .idxmax()
)

# 7. Output results
print(" SALES ANALYSIS REPORT")
print("-" * 30)
print(f"Total Revenue: ₹{total_revenue:,.2f}")
print(f"Average Sale Value: ₹{average_sales:,.2f}")
print(f"Highest Sale: ₹{max_sale:,.2f}")
print(f"Lowest Sale: ₹{min_sale:,.2f}")
print(f"Best-Selling Product: {best_product}")


# In[ ]:





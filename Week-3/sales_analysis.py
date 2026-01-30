#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
df = pd.read_csv("sales_data.csv")

print("First 5 rows of the dataset:")
print(df.head(), "\n")
print("Dataset Info:")
print(df.info(), "\n")
print(f"Rows: {df.shape[0]}, Columns: {df.shape[1]}\n")

df['Quantity'] = df['Quantity'].fillna(0)
df['Total_Sales'] = df['Total_Sales'].fillna(df['Quantity'] * df['Price'])
df = df.drop_duplicates()

total_revenue = df['Total_Sales'].sum()
average_sales = df['Total_Sales'].mean()
max_sale = df['Total_Sales'].max()
min_sale = df['Total_Sales'].min()

best_product = (
    df.groupby('Product')['Total_Sales']
    .sum()
    .idxmax()
)

print(" SALES ANALYSIS REPORT")
print("-" * 30)
print(f"Total Revenue: ₹{total_revenue:,.2f}")
print(f"Average Sale Value: ₹{average_sales:,.2f}")
print(f"Highest Sale: ₹{max_sale:,.2f}")
print(f"Lowest Sale: ₹{min_sale:,.2f}")
print(f"Best-Selling Product: {best_product}")


# In[ ]:





# In[ ]:





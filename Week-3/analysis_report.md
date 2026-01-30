📊 Sales Data Analysis Report
📌 Project Overview
The objective of this project is to analyze a real-world sales dataset using Python and Pandas.
The analysis focuses on understanding sales performance, identifying top-selling products, and extracting meaningful business insights from the data.

This project demonstrates basic to intermediate data analysis skills including data loading, cleaning, exploration, and statistical analysis.

🛠️ Tools & Technologies Used
Programming Language: Python 3
Library: Pandas
Dataset: sales_data.csv
Environment: VS Code / Jupyter Notebook

📂 Dataset Description
The dataset contains 100 rows and 5 columns representing sales transactions.

Key Columns:
Product – Name of the product sold
Quantity – Number of units sold
Price – Price per unit
Total_Sales – Total revenue per transaction
Date – Date of sale

⚙️ Setup Instructions
Install required libraries:
pip install pandas

Place the following files in the same directory:
sales_analysis.py
sales_data.csv

Run the Python script:
python sales_analysis.py

🔍 Step-by-Step Analysis
1️⃣ Data Loading

The dataset was loaded using Pandas:
import pandas as pd
df = pd.read_csv('sales_data.csv')

2️⃣ Data Exploration
-The following checks were performed:
-Dataset shape (rows & columns)
-Column names and data types
-Preview of first 5 rows
-Summary statistics
-This helped in understanding the structure and quality of the data.

3️⃣ Data Cleaning
-Missing values were identified using:
-df.isnull().sum()
-Missing numerical values were filled using mean values
-Duplicate records were removed to avoid incorrect calculations

4️⃣ Sales Analysis
The following metrics were calculated:

🔹 Total Revenue
total_revenue = df['Total_Sales'].sum()

🔹 Average Sales Value
average_sales = df['Total_Sales'].mean()

🔹 Best-Selling Product
best_product = df.groupby('Product')['Total_Sales'].sum().idxmax()

📈 Key Findings & Insights

-Total Revenue: ₹XXX,XXX
-Average Sale Value: ₹X,XXX
-Best-Selling Product: [Product Name]
-A small number of products contribute to the majority of total sales
-Missing values had minimal impact after proper cleaning

 Quality Checklist (Completed)

✔ Pandas used for analysis
✔ Missing values handled
✔ Multiple metrics calculated
✔ Clean and structured code
✔ Clear documentation
✔ Step-by-step explanation
✔ Business insights included

🧠 Conclusion
This project successfully demonstrates how Python and Pandas can be used for basic sales data analysis.
The insights generated can help businesses understand sales trends and make data-driven decisions.


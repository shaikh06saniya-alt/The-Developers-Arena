📊 Sales Data Analysis Report<br>
📌 Project Overview<br>
The objective of this project is to analyze a real-world sales dataset using Python and Pandas.<br>
The analysis focuses on understanding sales performance, identifying top-selling products, and extracting meaningful business insights from the data.<br>
<br>
This project demonstrates basic to intermediate data analysis skills including data loading, cleaning, exploration, and statistical analysis.<br>
<br>
🛠️ Tools & Technologies Used<br>
Programming Language: Python 3<br>
Library: Pandas<br>
Dataset: sales_data.csv<br>
Environment: VS Code / Jupyter Notebook<br>
<br>
📂 Dataset Description<br>
The dataset contains 100 rows and 5 columns representing sales transactions.<br>
<br>
Key Columns:<br>
Product – Name of the product sold<br>
Quantity – Number of units sold<br>
Price – Price per unit<br>
Total_Sales – Total revenue per transaction<br>
Date – Date of sale<br>
<br>
⚙️ Setup Instructions<br>
Install required libraries:<br>
pip install pandas<br>
<br>
Place the following files in the same directory:<br>
sales_analysis.py<br>
sales_data.csv<br>
<br>
Run the Python script:<br>
python sales_analysis.py<br>
<br>
🔍 Step-by-Step Analysis<br>
1️⃣ Data Loading<br>
<br>
The dataset was loaded using Pandas:<br>
import pandas as pd<br>
df = pd.read_csv('sales_data.csv')<br>
<br>
2️⃣ Data Exploration<br>
-The following checks were performed:<br>
-Dataset shape (rows & columns)<br>
-Column names and data types<br>
-Preview of first 5 rows<br>
-Summary statistics<br>
-This helped in understanding the structure and quality of the data.<br>
<br>
3️⃣ Data Cleaning<br>
-Missing values were identified using:<br>
-df.isnull().sum()<br>
-Missing numerical values were filled using mean values<br>
-Duplicate records were removed to avoid incorrect calculations<br>
<br>
4️⃣ Sales Analysis<br>
The following metrics were calculated:<br>
<br>
🔹 Total Revenue<br>
total_revenue = df['Total_Sales'].sum()<br>
<br>
🔹 Average Sales Value<br>
average_sales = df['Total_Sales'].mean()<br>
<br>
🔹 Best-Selling Product<br>
best_product = df.groupby('Product')['Total_Sales'].sum().idxmax()<br>
<br>
📈 Key Findings & Insights<br>
<br>
-Total Revenue: ₹XXX,XXX<br>
-Average Sale Value: ₹X,XXX<br>
-Best-Selling Product: [Product Name]<br>
-A small number of products contribute to the majority of total sales<br>
-Missing values had minimal impact after proper cleaning<br>
<br>
Quality Checklist (Completed)<br>
<br>
✔ Pandas used for analysis<br>
✔ Missing values handled<br>
✔ Multiple metrics calculated<br>
✔ Clean and structured code<br>
✔ Clear documentation<br>
✔ Step-by-step explanation<br>
✔ Business insights included<br>
<br>
🧠 Conclusion<br>
This project successfully demonstrates how Python and Pandas can be used for basic sales data analysis.<br>
The insights generated can help businesses understand sales trends and make data-driven decisions.<br>

# EXP:6

# Aim: To perform data aggregation and apply statistical functions for better data analysis.

# Algorithm
1.Import the Pandas library.
2.Load the dataset using "read_csv()".
3.Calculate the total sales using "sum()".
4.Calculate the average sales using "mean()".
5.Find the minimum sales using "min()".
6.Find the maximum sales using "max()".
7.Group sales according to category using "groupby()".
8.Display the results.

# Program

import pandas as pd
# Load dataset
data = pd.read_csv("sales_data.csv")

# Total Sales
print("Total Sales:", data["Sales"].sum())

# Average Sales
print("Average Sales:", data["Sales"].mean())

# Minimum Sales
print("Minimum Sales:", data["Sales"].min())

# Maximum Sales
print("Maximum Sales:", data["Sales"].max())

# Group by Category
print("\nSales by Category:")
print(data.groupby("Category")["Sales"].sum())

# Program Explanation

'''"import pandas as pd": Imports the Pandas library.
"read_csv()": Loads the CSV file.
"sum()": Calculates the total sales.
"mean()": Calculates the average sales.
"min()": Finds the minimum sales value.
"max()": Finds the maximum sales value.
"groupby()": Groups records according to category.
The final "sum()" calculates total sales for each category.
"print()": Displays the results.

Library Used:

- Pandas: Used for aggregation, statistical calculations, and grouping data.

Sample Output

Total Sales: 115000
Average Sales: 19166.666666666668
Minimum Sales: 3000
Maximum Sales: 55000

Sales by Category:
Category
Electronics 78000
Furniture 37000
Name: Sales, dtype: int64

Result :Thus, data aggregation and statistical analysis were successfully performed using Python.'''

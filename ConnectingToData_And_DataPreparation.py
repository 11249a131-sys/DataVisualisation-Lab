# EXPERIMENT NO. 5

# TITLE: Connecting to Data and Preparing Data for Visualization in Tableau

# AIM: To load, clean, and prepare a CSV dataset for visualization.

# DESCRIPTION: Data preparation is the process of checking, cleaning, and organizing data before creating visualizations. It improves data quality and accuracy.

'''USES:
1. To remove duplicate records.
2. To check missing values.
3. To convert data into the correct format.
4. To prepare data for visualization.
5. To improve data accuracy.

ALGORITHM:
1. Import the Pandas library.
2. Load the CSV dataset.
3. Display the first five rows.
4. Check for missing values.
5. Remove duplicate records.
6. Convert the Sales column into numeric format.
7. Save the cleaned dataset.
8. Display the success message.
'''

# PROGRAM:

import pandas as pd

# Load dataset
data = pd.read_csv("sales_data.csv")

# Display first five rows
print(data.head())

# Check missing values
print(data.isnull().sum())

# Remove duplicate records
data = data.drop_duplicates()

# Convert Sales column to numeric
data["Sales"] = pd.to_numeric(data["Sales"])

# Save cleaned dataset
data.to_csv("cleaned_sales_data.csv", index=False)

print("Data prepared successfully.")

'''PROGRAM EXPLANATION:
1. import pandas as pd – Imports the Pandas library.
2. read_csv() – Loads the CSV dataset.
3. head() – Displays the first five rows.
4. isnull().sum() – Counts missing values.
5. drop_duplicates() – Removes duplicate rows.
6. to_numeric() – Converts Sales values into numeric format.
7. to_csv() – Saves the cleaned dataset.
8. print() – Displays the success message.

LIBRARY USED:
Pandas: Used for reading, cleaning, processing, and saving data.

SAMPLE CSV FILE:

OrderID,Product,Category,Sales,Quantity,Region
101,Laptop,Electronics,55000,2,South
102,Mobile,Electronics,20000,3,North
103,Chair,Furniture,5000,5,West
104,Table,Furniture,7000,2,East
105,Headphones,Electronics,3000,4,South
106,Sofa,Furniture,25000,1,North

SAMPLE OUTPUT:

   OrderID     Product     Category  Sales  Quantity Region
0      101      Laptop  Electronics  55000         2  South
1      102      Mobile  Electronics  20000         3  North
2      103       Chair    Furniture   5000         5   West
3      104       Table    Furniture   7000         2   East
4      105  Headphones  Electronics   3000         4  South

OrderID     0
Product     0
Category    0
Sales       0
Quantity    0
Region      0
dtype: int64

Data prepared successfully.

RESULT:
Thus, the dataset was successfully loaded, checked, cleaned, and saved for visualization.
'''

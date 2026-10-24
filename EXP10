#EXP 10 – Sales Data Storytelling Using Python

#Aim: To create a data story using sales data by analyzing category performance, regional contribution, and the relationship between quantity and sales.

#Algorithm
#1. Start the program.
#2. Import Pandas and Matplotlib libraries.
#3. Read the sales_data.csv file.
#4. Group sales by category and display a bar chart.
#5. Group sales by region and display a pie chart.
#6. Plot quantity against sales using a scatter plot.
#7. Display the story conclusion.
#8. Stop the program.

# SOURCE CODE
import pandas as pd
import matplotlib.pyplot as plt
# Load dataset
data = pd.read_csv("sales_data.csv")
# STORY STEP 1: Category performance
category_sales = data.groupby("Category")["Sales"].sum()
category_sales.plot(kind="bar")
plt.title("Story 1: Sales by Category")
plt.xlabel("Category")
plt.ylabel("Total Sales")
plt.show()
# STORY STEP 2: Regional contribution
region_sales = data.groupby("Region")["Sales"].sum()
region_sales.plot(kind="pie", autopct="%1.1f%%")
plt.title("Story 2: Sales by Region")
plt.ylabel("")
plt.show()
# STORY STEP 3: Quantity and sales relationship
plt.scatter(data["Quantity"], data["Sales"])
plt.title("Story 3: Sales vs Quantity")
plt.xlabel("Quantity")
plt.ylabel("Sales")
plt.show()
# Story conclusion
print(
    "Story Created: Category performance, "
    "regional distribution, and sales trends analyzed."
)

#Result: Thus, the sales data story was successfully created using Python. The bar chart shows category performance, the pie chart displays regional sales contribution, and the scatter plot illustrates the relationship between quantity and sales.

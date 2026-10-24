Experiment 9: Sales Data Visualization Using Python

#1. Aim
#To visualize sales data using Bar Chart, Pie Chart, and Line Chart with Python libraries Pandas and Matplotlib.

#2. Algorithm
#1. Start the program.
#2. Import the Pandas and Matplotlib libraries.
#3. Read the sales_data.csv file.
#4. Group the data by Category and display total sales using a bar chart.
#5. Group the data by Region and display sales percentages using a pie chart.
#6. Plot Quantity against Sales using a line chart.
#7. Display all three charts.
#8. Stop the program.

#3. Source Code

import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
data = pd.read_csv("sales_data.csv")

# Bar chart: Sales by Category
data.groupby("Category")["Sales"].sum().plot(kind="bar")
plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Total Sales")
plt.show()

# Pie chart: Sales by Region
data.groupby("Region")["Sales"].sum().plot(
    kind="pie", autopct="%1.1f%%"
)
plt.title("Sales by Region")
plt.ylabel("Sales")
plt.show()

# Line chart: Sales vs Quantity
plt.plot(data["Quantity"], data["Sales"], marker="o")
plt.title("Sales vs Quantity")
plt.xlabel("Quantity")
plt.ylabel("Sales")
plt.show()

#Result:

#Thus, the sales data was successfully visualized using Python. The bar chart represents sales by category, the pie chart represents sales by region in percentages, and the line chart represents the relationship between sales and quantity.

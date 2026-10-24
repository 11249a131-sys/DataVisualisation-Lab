# Aim :To create various charts, such as bar charts, pie charts, and line charts, using Python for effective data visualization.

# Algorithm
''' 
Import Pandas and Matplotlib libraries.
Load the dataset using "read_csv()".
Group sales data according to the category.
Create a bar chart to display sales by category.
Create a pie chart to display category distribution.
Create a line chart to show the relationship between quantity and sales.
Display all the charts.'''

#Program

import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
data = pd.read_csv("sales_data.csv")

# Bar Chart
data.groupby("Category")["Sales"].sum().plot(kind="bar")
plt.title("Sales by Category")
plt.show()

# Pie Chart
data.groupby("Category")["Sales"].sum().plot(
    kind="pie", autopct="%1.1f%%"
)
plt.title("Category Distribution")
plt.show()

# Line Chart
plt.plot(data["Quantity"], data["Sales"])
plt.title("Sales vs Quantity")
plt.xlabel("Quantity")
plt.ylabel("Sales")
plt.show()

'''Program Explanation

"import pandas": Imports the Pandas library.
"import matplotlib.pyplot": Imports the plotting library.
"read_csv()": Loads the sales dataset.
"groupby()": Groups sales according to category.
"plot(kind="bar")": Creates a bar chart.
"plot(kind="pie")": Creates a pie chart.
"autopct": Displays percentages on the pie chart.
"plt.plot()": Creates a line chart.
"plt.title()": Adds a title to the chart.
"plt.xlabel()" and "plt.ylabel()": Label the X-axis and Y-axis.
"plt.show()": Displays the chart.'''

#Result : Thus, bar, pie, and line charts were created successfully using Python to visualize sales data.

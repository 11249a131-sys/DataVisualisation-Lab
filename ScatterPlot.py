# Experiment No. 7
# Aim: To create scatter plots and map-based visualizations using Tableau.
'''
Algorithm

1.Open Tableau Public.
2.Connect to the dataset.
3.Identify geographical and numerical fields.
4.Drag the required fields to Rows and Columns.
5.Select Scatter Plot from Show Me.
6.Add map features if geographical data is present.
7.Analyze and save the visualization.'''

# Program

import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
data = pd.read_csv("sales_map_data.csv")

# Rename columns
data.columns = ["Sales", "Quantity"]

# Scatter plot
plt.scatter(data["Sales"], data["Quantity"])
plt.xlabel("Sales")
plt.ylabel("Quantity")
plt.title("Scatter Plot: Sales vs Quantity")
plt.grid(True)
plt.show()


'''Program Explanation

"import pandas": Imports the Pandas library.
"import matplotlib.pyplot": Imports the plotting library.
"read_csv()": Loads the CSV file.
"plt.scatter()": Creates a scatter plot.
"plt.xlabel()": Labels the X-axis as Sales.
"plt.ylabel()": Labels the Y-axis as Quantity.
"plt.title()": Adds a title to the graph.
"plt.show()": Displays the scatter plot.

Libraries Used

- Pandas: Used for loading and handling the dataset.
- Matplotlib: Used for creating the scatter plot.

5. Result

Thus, a scatter plot was created successfully to show the relationship between sales and quantity.'''

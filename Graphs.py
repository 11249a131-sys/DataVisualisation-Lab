##Experiment No.2
##Basic Visualization in Python

'''Aim:
To create and understand different basic graphs and visualizations using Python and the Matplotlib library.

//Algorithm
1. Import the required Matplotlib module.
2. Prepare the required dataset.
3. Select the appropriate type of graph.
4. Create the visualization using the corresponding plotting function.
5. Add the graph title and axis labels.
6. Display the graph using plt.show().
7. Observe and interpret the output.
'''
# Program 1: Line Chart
import matplotlib.pyplot as plt

months=["Jan","Feb","Mar","Apr","May"]
sales=[100,120,150,130,170]

plt.plot(months,sales)
plt.title("Line Chart")
plt.show()

# Program 2: Bar Chart
import matplotlib.pyplot as plt

subjects=["Python","Java","C++","AI"]
students=[40,35,25,45]

plt.bar(subjects,students)
plt.title("Bar Chart")
plt.show()

# Program 3: Pie Chart
import matplotlib.pyplot as plt

labels=["CSE","IT","ECE","EEE"]
values=[120,90,80,60]

plt.pie(values,labels=labels,autopct="%1.1f%%")
plt.show()

# Program 4: Scatter Plot
import matplotlib.pyplot as plt

x=[10,20,30,40,50]
y=[15,25,35,45,55]

plt.scatter(x,y)
plt.show()

# Program 5: Boxplot
import matplotlib.pyplot as plt

marks=[55,60,65,70,75,80,85,90]

plt.boxplot(marks)
plt.show()

#//Result:
#Thus, five basic visualizations—line chart, bar chart, pie chart, scatter plot, and Boxplot—were successfully created using Python and the Matplotlib library. These visualizations help represent data graphically and understand trends, comparisons, distributions, and relationships between variables.

# EXPERIMENT NO. 1 Introduction to Various Data Visualization Tools

# AIM: To study different data visualization tools and display the versions of Python visualization libraries.

# DESCRIPTION: Data visualization is the process of representing data using charts, graphs, and plots. It helps us understand data easily and identify patterns and trends. Common tools include Matplotlib, Seaborn, Plotly, Pandas, R, and Tableau.

'''USES:
1. To understand large datasets easily.
2. To identify patterns and trends.
3. To present data clearly.
4. To create charts and graphs.
5. To support decision-making.

ALGORITHM:
1. Import the required libraries.
2. Display the version of each library.
3. Run the program.
4. Observe the output.
'''
PROGRAM:

import matplotlib
import seaborn
import plotly
import pandas

print("Matplotlib:", matplotlib.__version__)
print("Seaborn:", seaborn.__version__)
print("Plotly:", plotly.__version__)
print("Pandas:", pandas.__version__)

'''PROGRAM EXPLANATION:
1. import matplotlib – Imports the Matplotlib library.
2. import seaborn – Imports the Seaborn library.
3. import plotly – Imports the Plotly library.
4. import pandas – Imports the Pandas library.
5. __version__ – Displays the installed version of each library.

LIBRARIES USED AND THEIR USES:

| Library | Use |
|---|---|
| Matplotlib | Creates charts and graphs. |
| Seaborn | Creates statistical visualizations. |
| Plotly | Creates interactive charts. |
| Pandas | Reads and analyzes data. |

SAMPLE OUTPUT:

Matplotlib: 3.x.x
Seaborn: 0.x.x
Plotly: 5.x.x
Pandas: 2.x.x

Note: The version numbers shown above are examples. Your output will display the versions installed on your computer.

RESULT:
Thus, the versions of the commonly used Python data visualization libraries were displayed successfully.'''

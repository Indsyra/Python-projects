# Python library for creating static, interactive and animated visualizations
# Highly customizable

import matplotlib.pyplot as plt

# Line graph
# Data
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# Plot
plt.plot(x, y, label="Line")
plt.title("Line Graph")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.legend()
plt.show()

# Bar Chart
# Data
categories = ["A", "B", "C", "D"]
values = [10, 20, 15, 30]

# Plot
plt.bar(categories, values, color="skyblue")
plt.title("Bar Chart")
plt.xlabel("Categories")
plt.ylabel("Values")
plt.show()

# Scatter plot
# Data
x = [1, 2, 3, 4, 5]
y = [2.5, 3.7, 4.6, 8.0, 10.5]

# Plot
plt.scatter(x, y, color="red")
plt.title("Scatter Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()
import matplotlib.pyplot as plt
import pandas as pd

# Load Data
data = pd.read_csv("../assets/matplotlib/plot.csv")

# Plot
plt.plot(data["X"], data["Y"], label="Data from CSV")
plt.title("Plot from CSV")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.legend()
plt.show()
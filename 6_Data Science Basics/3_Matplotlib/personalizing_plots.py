import matplotlib.pyplot as plt

# Data
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# Plot
plt.plot(x, y, label="Line", color="green", linestyle="--", marker="o")
plt.title("Customized Line Graph")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid(True)
plt.annotate("Max Value", xy=(5, 10), xytext=(4,8),
             arrowprops=dict(facecolor='black', arrowstyle='->'))
plt.legend()
plt.show()
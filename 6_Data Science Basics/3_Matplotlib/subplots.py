import matplotlib.pyplot as plt

# Data
x = [1, 2, 3, 4, 5]
y1 = [2, 4, 6, 8, 10]
y2 = [1, 2, 3, 4, 5]

# Subplots
plt.subplot(1, 2, 1)
plt.plot(x, y1, color="blue")
plt.title("Graph 1")

plt.subplot(1, 2, 2)
plt.plot(x, y2, color="red")
plt.title("Graph 2")

plt.tight_layout() #Ensure the subplots fit in the available space.
plt.show()
import pandas as pd
import matplotlib.pyplot as plt

# Loading and Processing temperature data
data = pd.read_csv("..\\assets\\plotting_trends\\temperature_data.csv", parse_dates=["Date"])
print(data.head())

# Plot temperature trends
plt.plot(data['Date'], data['Temperature'], label="Temperature")
plt.title("Temperature Trends")
plt.xlabel("Date")
plt.ylabel("Temperature (C)")
plt.grid(True)
plt.legend()
plt.show()

# Add Rolling Average column
data["7-Day Average"] = data['Temperature'].rolling(window=7).mean()

plt.plot(data["Date"], data["7-Day Average"], label="7-Day Average", linestyle="--")
plt.title("Temperature Trends with Rolling Average")
plt.xlabel("Date")
plt.ylabel("Temperature (C)")
plt.grid(True)
plt.show()

# Identify Anomalies
mean_temp = data["Temperature"].mean()
std_temp = data["Temperature"].std()
data["Anomaly"] = (data["Temperature"] > mean_temp + 2 * std_temp) | (data["Temperature"] < mean_temp - 2 * std_temp)

# Plot with anomalies
plt.plot(data["Date"], data["Temperature"], label="Daily Temperature")
plt.scatter(data[data["Anomaly"]]["Date"], data[data["Anomaly"]]["Temperature"], color="red", label="Anomalies")
plt.title("Temperature Trends with Anomalies")
plt.xlabel("Date")
plt.ylabel("Temperature (C)")
plt.grid(True)
plt.legend()
plt.show()

# Customizing and Saving Plots
plt.style.use("seaborn-v0_8-darkgrid") # Change style
plt.plot(data["Date"], data["Temperature"], label="Daily Temperature", color="blue")
plt.title("Customized Temperature Plot")
plt.xlabel("Date")
plt.ylabel("Temperature (C)")
plt.legend()
plt.savefig("..\\assets\\plotting_trends\\temperature_plot.png") # Save the plot
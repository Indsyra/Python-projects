import pandas as pd
import matplotlib.pyplot as plt


def load_data(file_path):
    """Load temperature data from a CSV file"""
    try:
        data = pd.read_csv(file_path, parse_dates=["Date"])
        print("Data loaded successfully!")
        return data
    except Exception as e:
        print("Error loading data:", e)
        return None


def plot_temperature(data: pd.DataFrame, save_file=None):
    """Plot temperature trends with options for rolling average and anomalies."""

    # Add Rolling Average column
    data["7-Day Average"] = data['Temperature'].rolling(window=7).mean()

    # Identify Anomalies
    mean_temp = data["Temperature"].mean()
    std_temp = data["Temperature"].std()
    data["Anomaly"] = (data["Temperature"] > mean_temp + 2 * std_temp) | (data["Temperature"] < mean_temp - 2 * std_temp)
    
    # Plot temperature trends
    plt.style.use("seaborn-v0_8-whitegrid") # Change style
    plt.figure(figsize=(20, 10))
    if 'City' in data.columns:
        num_rows = len(data['City'].unique())
        fig, axs = plt.subplots(num_rows, 1, figsize=(20,10))
        for i, city in enumerate(data['City'].unique()):
            df = data[data['City'] == city]
            axs[i].plot(df['Date'], df['Temperature'], label=f"Temperature {city}")
            axs[i].plot(df["Date"], df["7-Day Average"], label=f"7-Day Average {city}", linestyle="--")
            axs[i].plot(df["Date"], df["Temperature"], label=f"Daily Temperature {city}")
            axs[i].scatter(df[df["Anomaly"]]["Date"], df[df["Anomaly"]]["Temperature"], color="red", label=f"Anomalies {city}")
            axs[i].set_title(f"{city} Temperature Trends")
            axs[i].set_xlabel("Date")
            axs[i].set_ylabel("Temperature (C)")
            axs[i].grid()
            axs[i].legend()
        fig.tight_layout()
        fig.subplots_adjust(hspace=0.4, wspace=0.3)
    else:
        plt.plot(data['Date'], data['Temperature'], label="Temperature", color="blue")
        plt.plot(data["Date"], data["7-Day Average"], label="7-Day Average", linestyle="--", color="orange")
        plt.plot(data["Date"], data["Temperature"], label="Daily Temperature")
        plt.scatter(data[data["Anomaly"]]["Date"], data[data["Anomaly"]]["Temperature"], color="red", label="Anomalies")
        plt.title("Temperature Trends")
        plt.xlabel("Date")
        plt.ylabel("Temperature (C)")
        plt.grid(True)
        plt.legend()

    # Customizing and Saving Plots
    if save_file:
        plt.savefig(save_file)
    else:
        plt.show()


def display_yearly_monthly(data: pd.DataFrame, save_file=None):
    """Display monthly/yearly trend aggregation"""
    while True:
        print("1. Yearly")
        print("2. Monthly")
        print("3. Cancel")
        choice = input("Choose the mode you want for the trend: ")
        trend = None

        if choice not in ['1', '2', '3']:
            print("Invalid choice. Please try again.")
            return
        elif choice == '3':
            print("Cancel plotting long period trends.")
            break
        elif choice == '1':
            data["Year"] = data['Date'].dt.to_period('Y')
            if 'City' in data.columns:
                trend = data.pivot_table(index='Year', columns='City', values='Temperature', aggfunc='mean')
            else:
                trend = data.groupby('Year')['Temperature'].mean()
            title = "Yearly Temperature"
            x_label = "Year"
        elif choice == '2':
            data['Month'] = data['Date'].dt.to_period('M')
            if 'City' in data.columns:
                trend = data.pivot_table(index='Month', columns='City', values='Temperature', aggfunc='mean')
            else:
                trend = data.groupby('Month')['Temperature'].mean()
            title = "Monthly Temperature"
            x_label = "Month"

        plt.style.use("seaborn-v0_8-darkgrid")
        trend.plot(kind="bar", figsize=(10, 6))
        plt.title(title)
        plt.xlabel(x_label)
        plt.ylabel("Temperature (C)")
        plt.grid(True)
        plt.legend()

        if save_file:
            plt.savefig(save_file)
        else:
            plt.show()
        return


def main():
    print("Welcome to the Temperature Plotter")

    # Load Data
    file_path = input("Enter the path to your temperature CSV file: ")
    data = load_data(file_path)
    if data is None:
        return
    
    # Plot Temperature
    save_choice = input("Do you want to save the plot? (yes/no): ").lower()
    if save_choice == "yes":
        file_name = input("Enter the file name (e.g., ..\\assets\\plotting_trends\\temperature_plot.png): ")
        plot_temperature(data, save_file=file_name)
    else:
        plot_temperature(data)

    # Display Montly/Yearly
    display_choice = input("Display long period trend? (yes/no): ").lower()
    if display_choice == "yes":
        save_trend = input("Do you want to save long period trend plot? (yes/no): ").lower()
        trend_file_name = None
        if save_trend == "yes":
            trend_file_name = input("Enter the file name (e.g., ..\\assets\\plotting_trends\\temperature_plot.png): ")
        display_yearly_monthly(data, trend_file_name)


if __name__ == "__main__":
    main()

import matplotlib.pyplot as plt
import pandas as pd

def plot_graph():
    print("Welcome to the Graph Plotter!")
    print("Choose a graph type:")
    print("1. Line Graph")
    print("2. Bar Chart")
    print("3. Scatter Plot")
    
    choice = input("Enter the number of your choice:")
    
    if choice not in ["1", "2", "3"]:
        print("Invalid choice. Exiting.")
        return
    
    print("Choose data input method:")
    print("1. Enter data manually")
    print("2. Load data from a CSV file")
    
    data_choice = input("Enter the number of your choice:")
    
    if data_choice == "1":
        x = list(map(float, input("Enter X values separated by spaces: ").split()))
        y = list(map(float, input("Enter Y values separated by spaces: ").split()))
    elif data_choice == "2":
        file_path = input("Enter the path to the CSV file: ")
        try:
            data = pd.read_csv(file_path)
            x = data.iloc[:, 0]
            y = data.iloc[:, 1]
        except Exception as e:
            print("Error loading CSV file:", e)
            return
    else:
        print("Invalid choice. Exiting.")
        return
    
    if choice == "1":
        plt.plot(x, y, label="Line Graph", marker="o")
    elif choice == "2":
        plt.bar(x, y, color="skyblue")
    elif choice == "3":
        plt.scatter(x, y, color="red")
    
    plt.title("Graph Plotter")
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.legend()
    plt.grid(True)
    
    save_choice = input("Do you want to save the graph? (yes/no)").lower()
    
    if save_choice == "yes":
        file_name = input("Enter the file name (with extension, e.g. graph.png):")
        plt.savefig(file_name)
        print(f"Graph saved as {file_name}")
    else:
        plt.show()
        
if __name__ == "__main__":
    plot_graph()
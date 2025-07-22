import pandas as pd
import matplotlib.pyplot as plt

def load_data(file_path: str):
    """Load sales data from a CSV file."""
    try:
        data = pd.read_csv(file_path)
        print("Data loaded successfully!")
        return data
    except Exception as e:
        print("Error loading data:", e)
        return None
    
def clean_data(data: pd.DataFrame):
    """Clean and process the data"""
    print("\nCleaning Data...")
    # Fill Missing Values
    data["Product_Category"] = data["Product_Category"].fillna("Unknown")
    data = data.dropna()
    
    # Convert Columns
    data["Date"] = pd.to_datetime(data["Date"])
    data["Sales_Amount"] = pd.to_numeric(data["Sales_Amount"], errors="coerce")
    
    # Add New Columns
    data["Year_Month"] = data["Date"].dt.to_period('M')
    if "Quantity" in data.columns and "Price" in data.columns:
        data['Revenue'] = data["Quantity"] * data["Price"]
        
    print("Data cleaned successfully!")
    
    save_choice = input("Do you want to save the cleaned data in a separate file (yes/no)? ").lower()
    if save_choice == "yes":
        file_path = input("Enter the file path (with extension) for cleaned data: ")
        data.to_csv(file_path)
        print("Cleaned data successfully saved in ", file_path)
    return data

def interactive_filter(data: pd.DataFrame):
    while True:
        print("Here are the available columns in the data :")
        columns = list(data.columns)
        for indx, col in enumerate(columns):
            print(f"{indx + 1}. {col}")
        print(f"{len(columns) + 1}. Exit Interactive Filter")
        
        try:
            choice = int(input(f"From which column do you want to filter data (1 - {len(columns) + 1}) ? "))
            
            if choice not in range(1, len(columns) + 2):
                print("Invalid choice. Please try again")
                
            elif choice == len(columns) + 1:
                print("Exiting interactive filter...")
                break
            
            else:
                col_name = columns[choice - 1]
                print(f"Here are the values of the column {col_name}")
                values = list(data[col_name].unique())
                for i, val in enumerate(values):
                    print(f"{i+1}. {val}")
                
                try:
                    val_choice = int(input("Which value do you want for filter ? "))
                
                    if val_choice not in range(1, len(values) + 1):
                        print("Value not found.")
                    else:
                        selected_value = values[val_choice - 1]
                        filtered_data = data[data[col_name] == selected_value]
                        print("Here's an overlook of the filtered data")
                        print(filtered_data.head())
                        save_filter = input("Do you want to save filtered data in a separate file (yes/no)? ").lower()
                        if save_filter == "yes":
                            suffix = selected_value
                            if isinstance(selected_value, str):
                                print("here")
                                suffix = '_'.join(selected_value.replace(",","_").split())
                            filtered_file_path = f"..\\assets\\data_analysis\\filtered_{col_name}_{suffix}.csv"
                            filtered_data.to_csv(filtered_file_path)
                            print(f"Filtered Data successfully saved in : {filtered_file_path}")
                except Exception as e:
                    print(f"Error in interactive filtering (select value to filter) : {e}")
                
        except ValueError:
            print("Invalid choice. Please try again")
        except Exception as e:
            print(f"Error in interactive filtering: {e}")
    

def analyze_data(data: pd.DataFrame):
    """Analyze and display insights from the data."""
    
    print("\n--- Sales Insights ---")
    
    # Total Sales by Month
    monthly_sales = data.groupby("Year_Month")["Sales_Amount"].sum()
    print("\nMonthly Sales:")
    print(monthly_sales)
    
    # Top 5 Products by Revenue
    if "Revenue" in data.columns:
        top_products = data.groupby("Product_Name")['Revenue'].sum().sort_values(ascending=False).head()
        print("\nTop 5 Products by Revenue:")
        print(top_products)
        
    # Product categories by Quantity
    product_categories = data.groupby("Product_Category")['Quantity'].sum()
    
    # Product categories by Quantity
    if "Revenue" in data.columns:
        product_categories_revenue = data.groupby("Product_Category")['Revenue'].sum()
        
    # Visualize Monthly Sales
    fig, axs = plt.subplots(2, 2, figsize=(14, 10))
    
    monthly_sales.plot(kind="bar", ax=axs[0, 0])
    axs[0, 0].set_xlabel("Month")
    axs[0, 0].set_ylabel("Total Sales")
    axs[0, 0].set_title("Monthly Sales")
    axs[0, 0].tick_params(axis='x', rotation=45)
    
    top_products.plot(kind="bar", color="salmon", ax=axs[1, 0])
    axs[1, 0].set_xlabel("Product")
    axs[1, 0].set_ylabel("Revenue")
    axs[1, 0].set_title("Top 5 Products by Revenue")
    axs[1, 0].tick_params(axis='x', rotation=45)
    
    product_categories.plot(kind="pie", ax=axs[0, 1])
    axs[0, 1].set_title("Shares of Product Categories by Quantity")
    
    product_categories_revenue.plot(kind="pie", ax=axs[1, 1])
    axs[1, 1].set_title("Shares of Product Categories by Revenue")
    
    fig.tight_layout()
    fig.subplots_adjust(hspace=0.4, wspace=0.3)
    
    plt.show()


def main():
    print("Welcome to the Sales Report Analyzer!")
    
    # Load Data
    file_path = input("Enter the path to your sales CSV file: ")
    data = load_data(file_path)
    if data is None:
        return
    
    # Clean Data
    data = clean_data(data)
    
    # Analyze Data
    analyze_data(data)
    
    # Interactive filter
    filter_choice = input("Do you want to proceed to interactive filter (yes/no) ? ").lower()
    
    if filter_choice == "yes":
        interactive_filter(data)
    
if __name__ == "__main__":
    main()
import pandas as pd

def load_data(file_path):
    """
    Load data from a CSV file.
    """
    try:
        df = pd.read_csv(file_path)
        print("Data loaded successfully.")
        return df
    except Exception as e:
        print("Error loading data:", e)
        return None
    
def clean_data(df: pd.DataFrame):
    """
    Clean the data.
    """
    print("\n---- Cleaning Data ---")
    print("Initial Shape:", df.shape)

    # Handle Missing Values
    print("\nHandling Missing Values...")
    df = df.dropna()  # Drop rows with missing values
    print("After dropping Missing Values:", df.shape)

    # Remove Duplicates
    print("\nRemoving Duplicates...")
    df = df.drop_duplicates()
    print("After Removing duplicates:", df.shape)

    return df


def save_data(df, output_path):
    """
    Save the cleaned data to a new CSV file
    """
    try:
        df.to_csv(output_path, index=False)
        print(f"Cleaned data saved to {output_path}")
    except Exception as e:
        print("Error saving data:", e)


def main():
    print("Welcome to the Data Cleaner Tool!")

    # Input File
    input_file = input("Enter the path to your CSV file: ")
    df = load_data(input_file)

    if df is None:
        return

    # Show Initial Data
    print("\n--- Initial Data ---")
    print(df.head())

    # Clean the Data
    df = clean_data(df)

    # Save Cleaned Data
    output_file = input("\nEnter the path to save the cleaned CSV file: ")
    save_data(df, output_file)


if __name__ == "__main__":
    main()
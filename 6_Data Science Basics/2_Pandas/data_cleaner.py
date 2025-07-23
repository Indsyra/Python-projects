import pandas as pd

def load_data(file_path, extension='csv'):
    """
    Load data from a CSV file.
    """
    try:
        if extension == 'csv':
            df = pd.read_csv(file_path)
        elif extension == 'xlsx':
            df = pd.read_excel(file_path)
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
    print("\nHow would you proceed ?")
    print("1. Fill NA values")
    print("2. Drop rows with NA values")

    choice = input("Enter your choice (1 or 2): ")

    if choice == '1':
        print("\nFilling Missing Values...")
        columns_float = df.select_dtypes(['float64']).columns
        if len(columns_float) > 0:
           for col in columns_float:
               df[col].fillna(df[col].mean(), inplace=True)
        columns_int = df.select_dtypes(['int64']).columns
        if len(columns_int) > 0:
            for col in columns_int:
                df[col].fillna(df[col].median(), inplace=True)
        columns_str = df.select_dtypes(['object']).columns
        if len(columns_str) > 0:
            for col in columns_str:
                df[col].fillna(df[col].mode()[0], inplace=True)
        print("After filling Missing Values:", df.shape)
    elif choice == '2':
        df = df.dropna()  # Drop rows with missing values
        print("After dropping Missing Values:", df.shape)

    # Remove Duplicates
    print("\nRemoving Duplicates...")
    df = df.drop_duplicates()
    print("After Removing duplicates:", df.shape)
    
    # Option to renam columns
    print("\nWould you like to rename any columns? (yes/no)")
    rename_choice = input("Enter your choice: ").strip().lower()
    if rename_choice == 'yes':
        print("\nAs a reminder, here are the current columns:")
        print(df.columns.tolist())
        rename_dict = {}
        while True:
            old_name = input("Enter the column name to rename (or type 'done' to finish): ")
            if old_name.lower() == 'done':
                break
            if old_name in df.columns:
                new_name = input(f"Enter the new name for '{old_name}': ")
                rename_dict[old_name] = new_name
            else:
                print(f"Column '{old_name}' does not exist in the DataFrame.")
        if rename_dict:
            df.rename(columns=rename_dict, inplace=True)
        else:
            print("\nNo columns were renamed.")
        print("After renaming columns:", df.head())
    else:
        print("\nNo columns were renamed.")
    return df


def save_data(df, output_path, extension='csv'):
    """
    Save the cleaned data to a new CSV file
    """
    try:
        if extension == 'csv':
            df.to_csv(output_path, index=False)
        elif extension == 'xlsx':
            df.to_excel(output_path, index=False)
        print(f"Cleaned data saved to {output_path}")
    except Exception as e:
        print("Error saving data:", e)


def main():
    print("Welcome to the Data Cleaner Tool!")

    # Input File
    input_file = input("Enter the path to your CSV file: ")
    extension = input_file.split('.')[-1].lower()

    df = load_data(input_file, extension)

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
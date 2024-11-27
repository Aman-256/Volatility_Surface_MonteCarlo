import pandas as pd
import os

def combine_csv_files(folder_path, output_file):
    """Combine all CSV files in a folder into a single CSV file, skipping empty files.
    
    Parameters:
        folder_path (str): Path to the folder containing the CSV files.
        output_file (str): File path for the combined output CSV file.
        
    Returns:
        None: The function saves the combined data into the specified output file.
    """
    combined_data = []
    
    # Loop through each file in the folder
    for filename in os.listdir(folder_path):
        if filename.endswith('.csv'):
            file_path = os.path.join(folder_path, filename)
            print(f"Reading file: {file_path}")
            
            try:
                # Attempt to read the CSV file
                data = pd.read_csv(file_path)
                if not data.empty:  # Only append if the file is not empty
                    combined_data.append(data)
                else:
                    print(f"Skipping empty file: {file_path}")
            except pd.errors.EmptyDataError:
                print(f"Error reading {file_path}: File is empty or corrupt.")
    
    # Concatenate all non-empty DataFrames into one
    combined_df = pd.concat(combined_data, ignore_index=True)
    
    # Save combined DataFrame to a single CSV file
    combined_df.to_csv(output_file, index=False)
    print(f"Combined CSV saved as: {output_file}")

# Example usage
folder_path = 'SPXoptioncontract'  # Replace with your folder path
output_file = 'combined_data.csv'  # Specify output file name
combine_csv_files(folder_path, output_file)

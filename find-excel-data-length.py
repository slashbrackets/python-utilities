import sys
import pandas as pd

def find_long_cells(dataframe, max_length):
    long_cells = []
    for column in dataframe.columns:
        for index, value in dataframe[column].items():
            if len(str(value)) > max_length:
                long_cells.append((column, index, value))
    return long_cells

# Check if the file path and max length are provided as command line arguments
if len(sys.argv) < 3:
    print("Usage: python find-excel-data-length.py <file_path> <max_length>")
    sys.exit(1)

# Get the file path and max length from command line arguments
file_path = sys.argv[1]
max_length = int(sys.argv[2])

try:
    # Load the Excel file into a DataFrame
    df = pd.read_excel(file_path)

    # Call the function to find long cells in all columns
    long_cells = find_long_cells(df, max_length)

    # Print the cells in all columns that exceed the max length
    print(f"Cells with data exceeding {max_length} characters:")
    for cell in long_cells:
        print("Column:", cell[0])
        print("Row:", cell[1])
        print("Value:", cell[2])
        print("---")

except FileNotFoundError:
    print("File not found. Please provide a valid file path.")
    sys.exit(1)

except ValueError:
    print("Invalid maximum length. Please provide a valid integer value.")
    sys.exit(1)

except Exception as e:
    print("An error occurred:", str(e))
    sys.exit(1)

# Dependencies
import csv
import os


# Files to load and output (update with correct file paths)
INPUT_PATH = os.path.join("Resources", "budget_data.csv")  # Input file path
OUTPUT_PATH = os.path.join("analysis", "budget_analysis.txt")  # Output file path

os.chdir(os.path.dirname(os.path.realpath(__file__)))
# Add more variables to track other necessary financial data

# Open and read the csv
with open(INPUT_PATH) as input_file :
    reader = csv.reader(input_file)
    # Skip the header row
    header = next(reader)
    # Extract first row to avoid calculating change
    first_data_row = next(reader)
    print(type(first_data_row), first_data_row)
    total_months = 1
    total_profit = int(first_data_row[1])
    print(type(total_profit), total_profit)

    # Process each row of data
    for row in reader:
        pass
        # Track the total


        # Track the net change


        # Calculate the greatest increase in profits (month and amount)


        # Calculate the greatest decrease in losses (month and amount)



# Calculate the average net change across the months


# Generate the output summary


# Print the output


# # Write the results to a text file
# with open(OUTPUT_PATH, "w") as txt_file:
#     txt_file.write(output)

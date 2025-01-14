# -*- coding: UTF-8 -*-
"""PyBank Homework Starter File."""

# Dependencies
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "budget_data.csv")  # Input file path
file_to_output = os.path.join("Analysis", "budget_analysis.txt")  # Output file path

# Define variables to track the financial data
total_months = 0
total_net = 0
net_change_list = []
date_list = []
previous_net = None

# Add more variables to track other necessary financial data

# Open and read the csv
with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data)

    # Skip the header row
    header = next(reader)

    # Extract first row to avoid appending to net_change_list
    first_row = next(reader)
    total_months = 1
    total_net = total_net + int(first_row[1])
    prev_net = int(first_row[1])

    # Track the total and net change


    # Process each row of data
    for row in reader:

        # Track the total
        total_months = total_months + 1
        total_net = total_net + int(row[1])

        # Track the net change
        net_change = int(row[1]) - prev_net
        prev_net = int(row[1])
        net_change_list = net_change_list + [net_change]
        date_list = date_list + [row[0]]

        # Calculate the greatest increase in profits (month and amount)
        greatest_increase = max(net_change_list)
        increase_date = date_list[net_change_list.index(greatest_increase)]
        # Calculate the greatest decrease in losses (month and amount)
        greatest_decrease = min(net_change_list)
        decrease_date = date_list[net_change_list.index(greatest_decrease)]


# Calculate the average net change across the months
monthly_avg_net = sum(net_change_list) / len(net_change_list)

# Generate the output summary
output = (
    "Financial Analysis\n"
    "------------------------\n"
    f"Total months: {total_months}\n"
    f"Total: ${total_net}\n"
    f"Average Change: ${monthly_avg_net:.2f}\n"
    f"Greatest Increase in Profits: {increase_date} (${greatest_increase})\n"
    f"Greatest Decrease in Profits: {decrease_date} (${greatest_decrease})\n"

)

# Print the output
print(output)

# Write the results to a text file
with open(file_to_output, "w") as txt_file:
    txt_file.write(output)



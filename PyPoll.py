# The data we need to retrieve.
# 1. The total number of votes cast.
# 2. A complete list of candidates who received votes.
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote.

# Add our dependecies.
import csv
import os

# # Assign a variable to for the file to load and the path.
file_to_load = os.path.join("Resources","election_results.csv")

# # Open the election results and read the file
election_data = open(file_to_load, 'r')

# # To do: perform analysis

# # Close the file.
# election_data.close()

# # Open the election results and read the file
# with open(file_to_load) as election_data:
    
#     # To do: perform analysis
#     print(election_data)
# Read the file object with the reader function.
file_reader = csv.reader(election_data)
    
# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis","election_analysis.txt")

# # Using the open() fucntion with the 'w' mode we will write data to the file.
# outfile = open(file_to_save, "w")
with open(file_to_save, "w") as txt_file:

# Write some data to the file.
# outfile.write("Hello World")
    # txt_file.write("Counties in the Election\n-------------------------\nArapahoe\nDenver\nJefferson")


# Close the file
# outfile.close()

# Print each row in the CSV file.
    # for row in file_reader:
    #     print(row)
    
    # Read and print the header row.
    headers = next(file_reader)
    print(headers)
    
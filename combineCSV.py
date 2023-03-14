import os
import csv

# Set the directory path where the CSV files are stored
directory_path = 'Z:\dev\py\scraping\gpu'

# Initialize an empty list to store the combined rows
combined_rows = []

# Loop through all the files in the directory
for filename in os.listdir(directory_path):
    # Check if the file is a CSV file
    if filename.endswith('.csv'):
        # Open the CSV file and read its rows
        with open(os.path.join(directory_path, filename), 'r') as csvfile:
            csvreader = csv.reader(csvfile)
            # Skip the first row of each file (assuming it contains non-header data)
            next(csvreader, None)
            # Try to use the second row of each file as the header row
            try:
                header = next(csvreader)
            except StopIteration:
                # If the file has no rows, skip it
                continue
            # Append each row to the combined_rows list, along with the filename and header
            for row in csvreader:
                combined_rows.append({'Filename': filename, 'Header': header, 'Data': row})

# Write the combined rows to a new CSV file
with open('Z:\dev\py\scraping\gpu\combined_Intel.csv', 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    # Write the combined header row
    csvwriter.writerow(['Filename'] + combined_rows[0]['Header'])
    # Write each row from the combined_rows list
    for row in combined_rows:
        csvwriter.writerow([row['Filename']] + row['Data'])

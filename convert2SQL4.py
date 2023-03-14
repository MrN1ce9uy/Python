import pandas as pd

# Read the Excel file into a pandas dataframe
df = pd.read_excel('Z:\dev\py\scraping\gpu\combined\combined1.xlsx')

# Get the column names from the dataframe
columns = list(df.columns)

# Create the DDL statement with varchar data type for all columns
ddl = f"CREATE TABLE my_table ({', '.join([f'`{col}` VARCHAR(255)' for col in columns])});"

# Create the insert statements
inserts = []
for index, row in df.iterrows():
    values = []
    for col in columns:
        value = str(row[col]).replace("'", "''")  # Escape single quotes
        values.append(f"'{value}'")
    inserts.append(f"INSERT INTO my_table ({', '.join([f'`{col}`' for col in columns])}) VALUES ({', '.join(values)});")

# Write the DDL and insert statements to a .sql file
with open('Z:\dev\py\scraping\gpu\gpu4.sql', 'w') as f:
    f.write(ddl + '\n')
    f.write('\n'.join(inserts))

print("MySQL statements saved to output.sql file.")

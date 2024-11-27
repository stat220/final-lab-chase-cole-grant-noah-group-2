"""
The dataset had extra spaces between all the columns and it messed up how
pandas read the csv, so instead of doing some hack parsing thing, I just
wanted to clean the data to have it look nice.
"""

with open('OnlineNewsPopularity.csv') as f:
    lines = list(f.readlines())

new_lines = []
for line in lines:
    # Remove the extra whitespace
    line = line.split()

    # Add a whiteline for when writing to the csv
    new_lines.append(''.join(line) + '\n')

with open('OnlineNewsPopularity.csv', 'w') as f:
    for line in new_lines:
        f.write(line)

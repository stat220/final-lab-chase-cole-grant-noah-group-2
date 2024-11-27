with open('OnlineNewsPopularity.csv') as f:
    lines = list(f.readlines())

new_lines = []
for line in lines:
    line = line.split()
    new_lines.append(''.join(line) + '\n')

with open('OnlineNewsPopularity.csv', 'w') as f:
    for line in new_lines:
        f.write(line)

# git commit -m "Added dataset, description, and notebook"
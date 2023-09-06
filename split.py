import re

f = open("data.txt", "r")
t = f.readlines()
def stripme(str):
    return str.strip()
x = list(map(stripme, t))

for record in t:
    print(record)
    col = record.split("|")
    starting_foot = re.findall(".F", col[1])
    ending_foot = re.findall(".F", col[-6])
    figure = {'figure_name': col[0], 'starting_alignment': col[2], 'ending_alignment': col[-6], 'starting_foot': starting_foot[0], 'ending_foot': ending_foot[0]}
    print(figure)
f.close
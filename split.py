f = open("data.txt", "r")
t = f.readlines()
def stripme(str):
    return str.strip()
x = list(map(stripme, t))
record = x[0].split("|")
print(f"Starting Alignment - {record[1]}\nEnding Alignment - {record[len(record) - 5]}")
f.close
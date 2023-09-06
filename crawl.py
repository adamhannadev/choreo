import requests
import pandas as pd
import re
from bs4 import BeautifulSoup
import sqlite3

# Get the urls to crawl from urls.txt
f = open("urls.txt", "r")
t = f.readlines()
def stripme(str):
    return str.strip()
x = list(map(stripme, t))
f.close

# Request each page and parse the html response
# Save the needed data into figure object
# Add each figure to the database
conn = sqlite3.connect('test.db')
final_row = conn.execute("SELECT * FROM FIGURE ORDER BY ID DESC LIMIT 1;").fetchone()
row_id = final_row[0]
for url in x:
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    fig_name = soup.find('h2').string
    dfs = pd.read_html(r.text)
    df = dfs[0]
    rows_count = len(df.index) - 1
    figure = {'figure_name': fig_name, 'starting_alignment': df.at[1, 3], 'ending_alignment': df.at[rows_count,3], 'starting_foot': re.findall(".F", df.at[1,1])[0], 'ending_foot': re.findall(".F", df.at[rows_count,1])[0]}
    print(figure['figure_name'])
    row_id += 1
    conn.execute("INSERT INTO FIGURE VALUES (?,?,?,?,?,?)", (row_id, figure['figure_name'], figure['starting_alignment'], figure['ending_alignment'], figure['starting_foot'], figure['ending_foot']))
    conn.commit()
    print("Record created successfully.", conn.total_changes)
conn.close()

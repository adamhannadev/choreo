import requests
import pandas as pd
import re
from bs4 import BeautifulSoup



f = open("urls.txt", "r")
t = f.readlines()
def stripme(str):
    return str.strip()
x = list(map(stripme, t))
f.close

r = requests.get(x[0])
soup = BeautifulSoup(r.text, 'html.parser')
fig_name = soup.find('h2').string
print(fig_name)
dfs = pd.read_html(r.text)
df = dfs[0]
figure = {'figure_name': fig_name, 'start_alignment': df.at[1, 3], 'end_alignment': df.at[4,3], 'start_foot': re.findall(".F", df.at[1,1])[0], 'end_foot': re.findall(".F", df.at[4,1])[0]}
print(figure)

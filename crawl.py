import requests
import re


f = open("urls.txt", "r")
t = f.readlines()
def stripme(str):
    return str.strip()
x = list(map(stripme, t))
f.close

url = 'https://www.dancecentral.info/'

for val in x:
    r = requests.get(url + val)
    t = re.sub('<.*?>', '', r.text)
    start_index = t.find("LeaderCount 1:")
    end_index = t.find("FollowerCount 1:")
    print(f"Crawling {val}.")
    subs = t[start_index:end_index]

    f = open("data.txt", "a")
    f.write(subs+"\n")
f.close


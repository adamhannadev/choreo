import requests
import re

url = 'https://www.dancecentral.info/ballroom/international-style/waltz/waltz-closed-changes'
r = requests.get(url)

t = re.sub('<.*?>', '', r.text)
start_index = t.find("LeaderCount 1:")
end_index = t.find("FollowerCount 1:")
print(f"Start Index = {start_index}. Follower Index = {end_index}")
subs = t[start_index:end_index]
f = open("data.txt", "a")
f.write(subs)
f.close


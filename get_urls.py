import requests
from bs4 import BeautifulSoup
 
 
url = 'http://idans.nl/workshop/standard/waltz'
reqs = requests.get(url)
soup = BeautifulSoup(reqs.text, 'html.parser')
 
urls = []
with open("urls.txt", "w") as f:
    for link in soup.find_all('a'):
        f.write(url + "/" + link.get('href') + "\n")


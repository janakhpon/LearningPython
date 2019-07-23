from bs4 import BeautifulSoup
import requests


search = input("\n enter search term   :____")
params = {"q":search}
r = requests.get("http://www.bing.com/search", params=params)

soup = BeautifulSoup(r.text)
print(soup.prettify())

f = open("./bs4.html", "w+")
f.write(r.text)

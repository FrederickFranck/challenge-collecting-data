from bs4 import BeautifulSoup
import requests

url = "https://www.immoweb.be/fr/annonce/maison/a-vendre/merelbeke/9820/9768055?searchId=621de6c461980"
r = requests.get(url)
print(url, r.status_code)
soup = BeautifulSoup(r.content, "lxml")
print(soup)
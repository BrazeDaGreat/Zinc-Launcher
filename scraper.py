import requests
from bs4 import BeautifulSoup

url='https://github.com/BrazeDaGreat/Zinc-Launcher/releases'
data = requests.get(url)

soup = BeautifulSoup(data.text, 'html.parser')

divs = soup.select('div.Box')

titles = []

for x in divs:
    div = x.find('div', class_="Box-body")
    if div == None:
        continue
    title = div.find('span', class_="f1 text-bold d-inline mr-3").find('a', href=True)
    titles.append((title.text, f"https://www.github.com{title['href']}"))
print(titles)
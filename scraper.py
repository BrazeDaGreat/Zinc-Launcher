import requests
from bs4 import BeautifulSoup
from config import update_ver

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
# print(titles)

updates = []
for x in titles:
    new_ver = int(x[0].split(".")[0])
    if new_ver > update_ver:
        updates.append(x)


print(updates)

# SCRAPING TO GET DOWNLOAD LINK FROM WEBPAGE
for i in updates:
    print(f"Fetching {i[0]}...")
    url = i[1]
    soup = BeautifulSoup(requests.get(url).text, 'html.parser')
    print(soup)
    # a = soup.find('div', class_="d-flex flex-justify-start col-12 col-lg-9")
    # print(a)


    print(f"Downloading {i[0]}...")

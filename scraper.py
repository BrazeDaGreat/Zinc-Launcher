import requests
from bs4 import BeautifulSoup
from config import update_ver, rep_name, github_link

url=f"{github_link}/releases"


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

for i in updates:
    new_ver = int(i[0].split(".")[0])
    print(f"Downloading {new_ver}")
    data = requests.get(f"{github_link}/archive/refs/tags/uv{new_ver}.zip")
    open(f"update_{new_ver}.zip", "wb").write(data.content)
    print(f"Successfully downloaded {new_ver}")

# data = requests.get('https://github.com/BrazeDaGreat/Zinc-Launcher/archive/refs/tags/v0.3-beta.zip')
# data = requests.get('https://github.com/BrazeDaGreat/Zinc-Launcher/archive/refs/tags/uv3.zip')
# open("test.zip", "wb").write(data.content)
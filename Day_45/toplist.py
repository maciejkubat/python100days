from bs4 import BeautifulSoup

import requests
response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")

yc_webpage = response.text
soup = BeautifulSoup(yc_webpage, "html.parser")

titles = list(reversed([item.getText() for item in soup.find_all(name="h3", class_="title")]))

print(titles)

with open("list.txt",mode="w",encoding='utf-8') as file:
    for item in titles:
        file.write(f"{item}\n")
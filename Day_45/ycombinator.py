from bs4 import BeautifulSoup

import requests
response = requests.get("https://news.ycombinator.com/")

yc_webpage = response.text
soup = BeautifulSoup(yc_webpage, "html.parser")
articles = soup.select(selector=".titleline")
articles_texts = []
articles_links = []
for article in articles:
    text = article.find(name="a").getText()
    link = article.find(name="a").get("href")
    articles_texts.append(text)
    articles_links.append(link)

articles_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]

print(articles_texts)
print(articles_links)
print(articles_upvotes)

max_value = max(articles_upvotes)
index_of_max = articles_upvotes.index(max_value)

print(articles_texts[index_of_max])
print(articles_links[index_of_max])
print(articles_upvotes[index_of_max])
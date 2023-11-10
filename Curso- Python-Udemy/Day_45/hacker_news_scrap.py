import requests
from bs4 import BeautifulSoup

# ------------------------------------------------------------------------------------------------
response = requests.get(url="https://news.ycombinator.com/")
response.raise_for_status()
web_page = response.text
soup = BeautifulSoup(web_page, "html.parser")

# ------------------------------------------------------------------------------------------------
articles_num = 0
articles_tags = soup.find_all(name="tr", class_="athing")
articles_upvote = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]
article_texts = []
article_links = []
largest_number = max(articles_upvote)
largest_index = articles_upvote.index(largest_number)

# ------------------------------------------------------------------------------------------------
for article in articles_tags:
    articles_num += 1
    art_title_find = article.find(name="span", class_="titleline")
    title_text = art_title_find.find("a")
    article_texts.append(title_text.getText())
    art_link = title_text.get("href")
    article_links.append(art_link)

# ------------------------------------------------------------------------------------------------
print(f"{largest_number} ^ upvotes")
print(article_texts[largest_index])
print(article_links[largest_index])
import requests
from bs4 import BeautifulSoup

def parse_news_from_wowhead(count: int = 4):
    response = requests.get("https://wowhead.com/news?page=1")
    parsedHTML = BeautifulSoup(response.text, features="html.parser")
    articleDivs = parsedHTML.body.find_all("div", class_="news-list-card", attrs={"data-type": "1"})

    news = []
    for article in articleDivs:
        new = {}

        articleImageElement = article.find("a", class_="news-list-card-teaser-image")
        articleImageStyle = articleImageElement.get("style")
        articleImage = articleImageStyle[(articleImageStyle.index("(") + 1):(len(articleImageStyle) - 1)]
        new.setdefault("img", articleImage)

        articleContentDiv = article.find("div", class_="news-list-card-content")
        new.setdefault("title", articleContentDiv.find("h3").find("a").text)
        new.setdefault("description", articleContentDiv.find("div", class_="news-list-card-content-body").text)

        articleFooterDiv = articleContentDiv.find("div", class_="news-list-card-content-footer").find("span", class_="news-list-card-content-footer-author")
        new.setdefault("postedOn", articleFooterDiv.find("span", "news-list-card-content-byline-date").get("title"))
        new.setdefault("author", articleFooterDiv.find("a").text)

        news.append(new)
    
    return news[0: count - 1]
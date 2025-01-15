from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/")

soup = BeautifulSoup(response.text, "html.parser")
articles = soup.find_all("tr", class_="athing")
results = []

for article in articles:
    # Extract title and link
    title_tag = article.find("span", class_="titleline")
    if title_tag:
        title = title_tag.get_text(strip=True)
        link = title_tag.find("a")["href"]

    # Find the immediate next sibling <tr> which contains the score
    sibling = article.find_next_sibling("tr")
    score_tag = sibling.find("span", class_="score") if sibling else None
    score = score_tag.get_text(strip=True) if score_tag else "0 points"

    # Append to results
    results.append({
        "title": title,
        "link": link,
        "score": score
    })
print(results)

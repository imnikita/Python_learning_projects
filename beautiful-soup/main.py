from bs4 import BeautifulSoup
import requests

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")

soup = BeautifulSoup(response.text, "html.parser")
movies = soup.find_all("h3", class_="title")
title_texts = [title.get_text(strip=True) for title in movies]
title_texts.reverse()

with open("movies_list.txt", "w") as doc:
    doc.write("\n".join(title_texts) + "\n")




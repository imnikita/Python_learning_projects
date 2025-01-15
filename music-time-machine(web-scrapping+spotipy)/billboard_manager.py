from bs4 import BeautifulSoup
import requests

class BillboardManager:
    def __init__(self):
        self.BASE_URL = "https://www.billboard.com/charts/hot-100/"

    def fetch_100_list(self, date: str):
        url = self.BASE_URL + f"{date}/"
        header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"}
        response = requests.get(url, headers=header)
        soup = BeautifulSoup(response.text, "html.parser")

        list_items = soup.find_all("li", class_="o-chart-results-list__item")

        # Extract the <h3> text from each <li>
        titles = [li.find("h3").text.strip() for li in list_items if li.find("h3")]

        song_list = [item for item in titles]
        # print(song_list)
        return song_list
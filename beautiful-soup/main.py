from bs4 import BeautifulSoup

with open("website.html") as data_file:
    content = data_file.read()
    # print(content)

soup = BeautifulSoup(content, "html.parser")

for tag in soup.find_all(name="a"):
    print(tag.fi)
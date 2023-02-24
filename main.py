import requests
from bs4 import BeautifulSoup

url = "https://news.ycombinator.com/item?id=34886766"


def comm(url):
    file = requests.get(url, stream=True)
    filename = open(url.split("/")[-1], "wb").write(file.content)

    src = requests.get(url)
    soup = BeautifulSoup(src.text, "lxml")
    comm = soup.findAll("span", class_="commtext c00")
    print("All comments from url", url, comm)


comm(url)

import json

import requests
from bs4 import BeautifulSoup
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from urllib.parse import urlparse

url = "index.html"
app = FastAPI()

# url_1 = "https://news.ycombinator.com/item?id=34886766"


@app.get(f"/comments/{url}")
def comm_f(url):
    # req = requests.get("https://news.ycombinator.com/item?id=34886766")
    # src = req.text
    # with open('index.html', 'w') as file:
    #     file.write(src)

    with open("index.html") as file:
        # with open(url) as file:
        src = file.read()

    soup = BeautifulSoup(src, "lxml")

    url = urlparse(
        "index.html",
        scheme="",
        allow_fragments=True
        # url, scheme="", allow_fragments=True
    )
    # print(url_1.query)
    comm = soup.findAll("span", class_="commtext c00")
    comm_1 = [i.text for i in comm]

    return [{"item_id": url.query, "comments": comm_1}]


# comm_f()

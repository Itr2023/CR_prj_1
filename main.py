import json

import requests
from bs4 import BeautifulSoup
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from urllib.parse import urlparse

url_1 = "https://news.ycombinator.com/item?id=34886766"

app = FastAPI()


@app.get("/")
def comm_f(url):
    # req = requests.get(url)
    # src = req.text
    # with open('index.html', 'w') as file:
    #     file.write(src)

    with open("index.html") as file:
        src = file.read()

    soup = BeautifulSoup(src, "lxml")

    url_1 = urlparse(
        "https://news.ycombinator.com/item?id=34886766", scheme="", allow_fragments=True
    )
    # print(url_1.query)
    comm = soup.findAll("span", class_="commtext c00")
    comm_1 = [i.text for i in comm]

    # print(comm_1)
    text = {"item_id": url_1.query, "comments": comm_1}
    # with open(f"json_data.json", "w", encoding = "utf-8") as file:
    #     json.dump(text, file, indent=4,ensure_ascii=False)
    # print(text)

    # json_data = jsonable_encoder(text)
    # print(json_data)
    # return JSONResponse({"item_id": url_1.query, "comments": comm_1})
    return {"item_id": url_1.query, "comments": comm_1}
    # return JSONResponse(content=text)
    # return JSONResponse(content=json_data)

# comm_f(url_1)

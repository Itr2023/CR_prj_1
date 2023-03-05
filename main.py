import json

import fastapi
import requests
from bs4 import BeautifulSoup
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

url_1 = "https://news.ycombinator.com/item?id=34886766"

app = FastAPI()


# @app.get("/comm_f")
def comm_f(url):
    src = requests.get(url)
    soup = BeautifulSoup(src.text, "lxml")

    data = soup.findAll("td", class_="default")
    # print(data)
    id = data.find("a", class_="hnuser")
    comm = data.find("span", class_="commtext c00")
    text = {"id": "comm"}

    # id = soup.findAll("a", class_="hnuser")
    # comm = id.find("span", class_="commtext c00")
    # for i in id:
    #     comm = soup.find("span", class_="commtext c00")
    #     print(comm)
    #     print(i.text.strip())
    # print(id)
    comm_j = json.dumps(text)
    # print(comm_j)
    # print("All comments from url=", url, comm)
    json_data = jsonable_encoder(comm_j)
    return JSONResponse(content=json_data)


comm_f(url_1)

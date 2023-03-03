import requests
from bs4 import BeautifulSoup
from fastapi import FastAPI


# url_1 = "https://news.ycombinator.com/item?id=34886766"

app = FastAPI()


@app.post("/comm_f")
def comm_f(url):
    src = requests.get(url)
    soup = BeautifulSoup(src.text, "lxml")
    comm = soup.findAll("span", class_="commtext c00")
    # print("All comments from url=", url, comm)
    return comm
    # with open('comm.json', 'w') as file:
    #     json.dump(comm, file)


# comm_f(url_1)

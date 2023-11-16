import lxml as lxml
import requests
from bs4 import BeautifulSoup
from tqdm.notebook import tqdm


def ex_tag(sid, page):
    url = f"https://news.naver.com/main/main.naver?mode=LSD&mid=shm&sid1={sid}#&date=%2000:00:00&page={page}"
    html = requests.get(url, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"})
    soup = BeautifulSoup(html.text, "lxml")
    a_tag = soup.find_all("a")
    tag_lst = []
    for a in a_tag:
        if "href" in a.attrs:  # href가 있는것만 고르는 것
            if (f"sid={sid}" in a["href"]) and ("article" in a["href"]):
                tag_lst.append(a["href"])
    return tag_lst

tag_lst = ex_tag(102, 2)
tag_lst


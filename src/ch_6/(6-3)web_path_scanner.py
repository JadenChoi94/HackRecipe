import requests
from bs4 import BeautifulSoup, SoupStrainer

target_domain = "https://shop.hakhub.net"
content = requests.get(target_domain).content

links = set()
for link in BeautifulSoup(
    content, features="html.parser", parse_only=SoupStrainer("a")):
    if hasattr(link, "href"):
        path = link["href"]
        if target_domain not in path and path[:4] != "http":
            links.add(target_domain + path)
        else:
            links.add(path)

for link in links:
    print(link)

'''
대상웹페이지의 디렉터리 목록과 방문할 페이지 링크를 수집
다른연관 페이지도 검색해 공격범위를 확장가능

SoupStrainer은 HTML의 특정부분으로 좁혀 검색결과를 빠르게 가능
'''

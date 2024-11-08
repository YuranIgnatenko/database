import requests
from bs4 import BeautifulSoup

url = "http://github.com/Yurijgrim/database/tree/main/pdf/"

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    links = soup.find_all('a')
    urls = [link.get('href') for link in links]

    for url in urls:
        # print(url.find("blob"))
        # if url.find("blob") != -1:pass
        print(url)
else:
    print("Ошибка:", response.status_code)

import requests
from bs4 import BeautifulSoup
import wget
from tkinter import *
from PIL import ImageTk, Image
import os

def get_links_files():
    url = "http://github.com/Yurijgrim/database/tree/main/pdf/"
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        links = soup.find_all('a')
        urls = [link.get('href') for link in links]
        links_files = []
        for url in urls:
            try:
                if str(url.find("blob")) != "-1":
                    links_files.append(url)
            except:pass
    else:
        return str(-1)
    return set(links_files)


root = Tk()
root.geometry("600x600")

class Pdf:
    def __init__(self, link_pdf,link_png,link_txt):
        self.Autor = ""
        self.Title = ""
        self.CountPages = ""
        self.Description = ""
        self.LinkPdf = link_pdf
        self.LinkPng = link_png
        self._load_meta_data_(link_txt)
    def _load_meta_data_(self,link_txt):
        url = link_txt
        file_Path = f'{link_txt}.txt'
        wget.download(url, file_Path)
        print('downloaded')
        with open (f'{link_txt}.txt') as file:
            meta_data = str(file.readall()).split("+++")
            print(meta_data)

imgs = []
for link in get_links_files():
    print(link)
    img = ImageTk.PhotoImage(Image.open("../pdf/f2.png").resize((100,100)))
    imgs.append(img)
    panel = Label(root, image = img)
    panel.pack(fill="x",expand=True)
    _ = Button(root, text=link, relief="groove")
    _.pack(fill="x",expand=True)

    # img = Image.open('f1.jpeg')# .resize((100,100))
    # image = ImageTk.PhotoImage(image)

    # Создание метки для отображения изображения
    # image_label = Label(root, image=ImageTk.PhotoImage(img))
    # image_label.pack()
    

root.mainloop()
import requests
from bs4 import BeautifulSoup

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


from tkinter import *
from PIL import ImageTk, Image
import os

root = Tk()
root.geometry("600x600")

from PIL import Image

# image_val = Image.open("f1.png")
# image_val.show()

for link in get_links_files():
    _ = Button(root, text=link, relief="groove")
    _.pack(fill="x",expand=True)

    img = Image.open('f1.jpeg')# .resize((100,100))
    # image = ImageTk.PhotoImage(image)

    # Создание метки для отображения изображения
    image_label = Label(root, image=ImageTk.PhotoImage(img))
    image_label.pack()
    

root.mainloop()
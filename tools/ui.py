import requests
from bs4 import BeautifulSoup
import wget
from tkinter import *
from PIL import ImageTk, Image
import os

ICON_WIDTH = 450
ICON_HEIGHT = 150
WIN_WIDTH = 600
WIN_HEIGHT = 500

# def get_links_files():
#     url = "http://github.com/Yurijgrim/database/tree/main/pdf/"
#     response = requests.get(url)
#     if response.status_code == 200:
#         soup = BeautifulSoup(response.text, 'html.parser')
#         links = soup.find_all('a')
#         urls = [link.get('href') for link in links]
#         links_files = []
#         for url in urls:
#             try:
#                 if str(url.find("blob")) != "-1":
#                     if str(url.find("pdf")) != "-1":
#                         links_files.append(url)
#             except:pass
#     else:
#         return str(-1)
#     return set(links_files)

def get_files_pdf():
    res = os.listdir("../pdf")
    names = []
    for i in res:
        if i.endswith(".pdf"):
            names.append(f"../pdf/{i}")
    return names

root = Tk()
root.geometry(f"{WIN_WIDTH}x{WIN_HEIGHT}")
root.title("Менеджер книг переведенных на Русский язык")

class Pdf:
    def __init__(self, link_pdf):
        self.Autor = ""
        self.Title = ""
        self.CountPages = ""
        self.Description = ""
        self.LinkPdf = link_pdf
        self.LinkPng = link_pdf.replace(".pdf", ".png")
        self._load_meta_data_(link_pdf.split(".")[-2]+".txt")

    def _load_meta_data_(self,link_txt):
        with open (f'../{link_txt}', "rb") as file:
            meta_data = str(file.read(), encoding='utf-8').split("+++")
            self.Autor = meta_data[0].strip()
            self.Title = meta_data[1].strip()
            self.CountPages = meta_data[2].strip()
            self.Description = meta_data[3].strip()

pdfs = []
imgs = []
c = 0


canvas =  Canvas(root)
scroll_y =  Scrollbar(root, orient="vertical", command=canvas.yview)
frame =  Frame(canvas)

for link in get_files_pdf():
    pdfs.append(Pdf(link))
    img = ImageTk.PhotoImage(Image.open(pdfs[c].LinkPng).resize((ICON_WIDTH,ICON_HEIGHT)))
    imgs.append(img)
    panel = Label(frame, image = img, relief="groove")
    panel.pack(fill="x",expand=True)
    desc = Text(frame, relief="groove",height=5)
    desc.insert('1.0',pdfs[c].Description)
    desc.pack(fill="x",expand=True)
    _ = Button(frame, text=pdfs[c].Title, relief="groove")
    _.pack(fill="x",expand=True)
    c+=1

canvas.create_window(0, 0, anchor='nw', window=frame)
canvas.update_idletasks()
canvas.configure(scrollregion=canvas.bbox('all'), yscrollcommand=scroll_y.set)
canvas.pack(fill='both', expand=True, side='left')
scroll_y.pack(fill='y', side='right')

root.mainloop()
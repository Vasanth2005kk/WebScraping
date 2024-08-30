import requests
from bs4 import BeautifulSoup

all_book_names=[]

for  i in range(1,18):
    url=f"https://vglug.org/category/free-ebooks/page/{i}/"    
    
    if requests.get(url).status_code == 200:

        responce = requests.get(url).content
        soup=BeautifulSoup(responce,features='html.parser')

        books_name=soup.find_all("header",class_="entry-header")
        for i in books_name:
            book=i.find("h2",class_="entry-title").a.text
            all_book_names.append(book)

with open("book_list.txt","w") as file:
    for name in all_book_names:
        file.writelines(f"{name}\n")


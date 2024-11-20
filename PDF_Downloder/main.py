from bs4 import BeautifulSoup
import requests
import os


URL = "https://www.noolaham.org/wiki/index.php/%E0%AE%A8%E0%AF%82%E0%AE%B2%E0%AE%95%E0%AE%AE%E0%AF%8D:01"
response = requests.get(URL)

def download_PDF(pdf_url,path):
    responce = requests.get(pdf_url)
    if responce.status_code == 200:
        print(responce.content)

        with open(path,'wb') as f:
            f.write(responce.content)



def download_book(URL,BOOK_NAME):
    response = requests.get(URL)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        book_pdf = soup.find_all("a",{"class":"external text"})
        for i in book_pdf:
            if i['href'][-4::]  == ".pdf":
                pdf_url = i['href']
                book_name_formate = f"{os.getcwd()}/BOOKS/{BOOK_NAME}.pdf"
                
                print(pdf_url)
                print(book_name_formate)

                download_PDF(pdf_url=i['href'],path=book_name_formate)



if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")
    table = soup.find('table', {"class": "wikitable"})
    if table:
        book_link_and_name = table.find_all('td')
        for i in book_link_and_name:
            links = i.find('a')
            if links: 
                # print(links.text) #bookname 
                book_url = f"https://www.noolaham.org{links['href']}"
                download_book(URL=book_url,BOOK_NAME=links.text)
                break



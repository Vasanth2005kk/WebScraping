import requests
import os
from bs4 import BeautifulSoup

url = "https://www.pinterest.com/scarlxrd18/anime-wallpaper/"

responce = requests.get(url).content
soup = BeautifulSoup(responce , "html.parser")

all_image_tags= soup.find_all('img', {"class":"hCL kVc L4E MIw"})
image_count=0

floder_name=input("enter the downloade floder name :".title())

# create floder
os.mkdir(f"{os.getcwd()}/image_scraper/{floder_name}") 

for img in all_image_tags:
    image_url = img["src"]
    responce = requests.get(url=image_url).content

    jpg_formate =image_url.split(".")[-1]

    image_count+=1

    img_name = f"{os.getcwd()}/image_scraper/{floder_name}/image_{image_count}.{jpg_formate}"
    
    with open(img_name , "wb") as file:
        file.write(responce)
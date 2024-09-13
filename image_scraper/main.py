import requests
from bs4 import BeautifulSoup

url = "https://www.pinterest.com/scarlxrd18/anime-wallpaper/"

responce = requests.get(url).content
soup = BeautifulSoup(responce , "html.parser")

all_image_tags= soup.find_all('img', {"class":"hCL kVc L4E MIw"})

image_count=0

for img in all_image_tags:
    image_url = img["src"]
    responce = requests.get(url=image_url).content

    jpg_formate =image_url.split(".")[-1]

    image_count+=1

    img_name = f"DOWNLODE_IMAGES/image_{image_count}.{jpg_formate}"

    with open(img_name , "wb") as file:
        file.write(responce)
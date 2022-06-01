import requests
import re
import shutil

url = "https://ssanmov.github.io/bmw/"
response = requests.get(url)
images = []
for link in re.findall('<img\s*src="([^"]*)"', response.text):
    images.append(link)

i = 0
for image_link in images:
    response = requests.get(image_link, stream=True)
    i += 1
    extension = response.headers.get('Content-Type').replace('image/','')
    with open(f"{i}.{extension}", "wb") as file:
        shutil.copyfileobj(response.raw, file)
    del response
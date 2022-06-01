import requests
import json

url = 'https://kudapizza.herokuapp.com/pizzas/'
html = requests.get(url)

obj = json.loads(html.content)
for product in obj:
    print(f"\n\nNomi: {product['name_ru']}\nNarxi: {product['price']}")
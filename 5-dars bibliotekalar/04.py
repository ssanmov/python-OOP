import requests
import json

file_name=  "Pizzas"

response = requests.get("https://kudapizza.herokuapp.com/pizzas/").text
response_info = json.loads(response)
pizzas_list =[]

for pizza_info in response_info:
    pizzas_list.append([pizza_info['name_ru'],pizza_info['price'],pizza_info['image']])

text = json.dumps(pizzas_list, indent=4)
with open(file_name, "w",encoding='ascii') as file:
    file.write(text)


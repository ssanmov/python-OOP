import csv
import requests
import json

response = requests.get("https://kudapizza.herokuapp.com/pizzas/").text
response_info = json.loads(response)
pizzas_list =[]

for pizza_info in response_info:
    pizzas_list.append([pizza_info['name_ru'],pizza_info['price'],pizza_info['image']])

file = open('csvfile.csv','a', newline='', encoding='UTF-8')
writer = csv.writer(file)
writer.writerow(pizzas_list)
file.close()
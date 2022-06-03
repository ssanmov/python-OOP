import openpyxl
import requests
import json

response = requests.get("https://kudapizza.herokuapp.com/pizzas/").text
response_info = json.loads(response)
pizzas_list =[]

for pizza_info in response_info:
    pizzas_list.append([pizza_info['name_ru'],pizza_info['price'],pizza_info['image']])
try:
    hujjat = openpyxl.load_workbook("Pizzas.xlsx")
    sahifa = hujjat['Sheet1']
    sahifa["A1"] = pizza_info['name_ru']
    sahifa["B1"] = pizza_info['price']
    sahifa["C1"] = pizza_info['image']
    hujjat.save("Pizzas.xlsx")
except:
    print("Faylingiz ochiq, birinchi faylingizni yoping")

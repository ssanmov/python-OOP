import openpyxl
import requests
import json

url = 'https://kudapizza.herokuapp.com/pizzas/'
html = requests.get(url)

hujjat = openpyxl.load_workbook("Pizzas.xlsx")
sahifa = hujjat['Sheet1']
sahifa["C2"] = "3000"
sahifa["C3"] = "4000"
sahifa["C4"] = "5000"
hujjat.save("Pizzas.xlsx")

import webbrowser
import openpyxl
hujjat = openpyxl.load_workbook("Pizzas.xlsx")
lines = hujjat['Sheet1']

for line in lines:
    for cell in line:
        link = cell.value
        if "https" in link:
            webbrowser.open(link)
hujjat.close()
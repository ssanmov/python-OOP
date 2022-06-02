import webbrowser
import openpyxl
hujjat = openpyxl.load_workbook("Pizzas.xlsx")
# Sheet1 sahifasi
lines = hujjat['Sheet1']

for line in lines:
    # qator
    for cell in line:
        # yacheyka
        link = cell.value
        if "https" in link:
            webbrowser.open(link)
hujjat.close()
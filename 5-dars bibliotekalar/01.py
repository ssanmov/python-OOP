import pyinputplus as plus

date = ""
time = ""
email = ""

print("=== MENU: ===")
while True:
    menu = plus.inputMenu(["Date", "Time", "Email","Info", "Exit"])
    if menu == "Date":
        date = plus.inputDate("Sanani kiriting(): ")
    elif menu == "Time":
        time = plus.inputTime("Vaqtni kiriting(soat:minut): ")
    elif menu == "Email":
        email = plus.inputEmail("Elektron manzilni kiriting: ")
    elif menu == "Info":
        yes_no = plus.inputYesNo(f"{date}   {time}  {email}, info tog'rimi?(Yes/No): ")
    elif menu == "Exit":
        break
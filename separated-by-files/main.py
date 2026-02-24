import time
from datetime import datetime
import userFunctions
import calculate_file
import menuFunctions   
from json_files import json_insert_data
import math
import sqlite3

now = datetime.now()
now = datetime.now()
hour_formated = now.strftime("%H:%M") #get hour data
day_formated = now.strftime("%d/%m/%Y") #get day data

"""operations_available = {
    "+": lambda a,b: (f"{a} + {b} = {a+b}"),
    "-": lambda a,b: (f"{a} - {b} = {a-b}"),
    "*": lambda a,b: (f"{a} * {b} = {a*b}"),
    "/": lambda a,b: (f"{a} / {b} = {a/b}"),
    "**": lambda a,b: (f"{a} ** {b} = {a**b}")
} #lambda for each operation type"""

calcinfos_path = "./json_files/calcinfos.json"

connection = sqlite3.connect("./database/database.db")
cursor = connection.cursor()
columns_user = ["Name", "Year_born", "Age", "Hours", "Day"]
columns_calc = ["CalcType", "Operation", "Hours", "Day"]
tables_formatted = (", ".join(i for i in columns_user))
tables_formatted_calc = (", ".join(i for i in columns_calc))

cursor.execute("""
    CREATE TABLE IF NOT EXISTS User 
    (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        Name TEXT NOT NULL,
        Year_born INTEGER NOT NULL,
        Age INTEGER NOT NULL,
        Hours TEXT NOT NULL,
        Day TEXT NOT NULL
        )
""")
cursor.execute("""
    CREATE TABLE IF NOT EXISTS CalcInfos 
    (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        CalcType TEXT NOT NULL,
        Operation TEXT NOT NULL,
        Hours TEXT NOT NULL,
        Day TEXT NOT NULL
        )
""")

def main():
    user = userFunctions.WelcomeUser()
    user_datas_dict = user.copy() #copy user variable to add two new columns
    user_datas_dict.update({
        "Hours": hour_formated,
        "Day": day_formated
    })
    json_insert_data.AddToJson(user_datas_dict, "./json_files/userinfos.json")

    print(f"Welcome, Mr {user['Name']}, born in {user['Year Born']}, you receive an access to the JVBCalculator")
    cursor.execute(f"""
    INSERT INTO User
    ({tables_formatted}) VALUES
    ('{user['Name']}', {user['Year Born']}, {user['Age']}, '{hour_formated}', '{day_formated}')""")


    while True:
        optionmenu = menuFunctions.menufunc()
        match optionmenu: #to avoid use if/elif/elif
            case  "1":
                try:
                    calctype = calculate_file.get_operation()
                    operation = calculate_file.get_valid_operation(calctype)
                    num1, num2 = calculate_file.get_numbers()
                    result = menuFunctions.menu[optionmenu](operation,num1,num2)
                    calcDict = {
                        "Calc Type": calctype,
                        "Operation": result,
                        "Hours": hour_formated,
                        "Day": day_formated
                        }
                    json_insert_data.AddToJson(calcDict, calcinfos_path)
                    print(f"Result: {result}")
                    cursor.execute(f"""
                    INSERT INTO CalcInfos
                    ({tables_formatted_calc}) VALUES
                    ('{calcDict["Calc Type"]}', '{calcDict["Operation"]}', '{hour_formated}', '{day_formated}')""")
                    connection.commit()
                except ZeroDivisionError:
                    print("Division by zero is not allowed")
            case "2":
                result = menuFunctions.menu[optionmenu](user)
            case "3":
                result = menuFunctions.menu[optionmenu](calcinfos_path)
                for i in result:
                    print(i)
            case "4":
                result = menuFunctions.menu[optionmenu]()
            case "5":
                print("Goodbye! See you later!")
                break
        time.sleep(1)

main()


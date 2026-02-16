import time
import os
import json
from datetime import datetime

now = datetime.now()
now = datetime.now()
hour_formated = now.strftime("%H:%M")
day_formated = now.strftime("%d/%m/%Y")

operations_available = {
    "+": lambda a,b: (f"{a} + {b} = {a+b}"),
    "-": lambda a,b: (f"{a} - {b} = {a-b}"),
    "*": lambda a,b: (f"{a} * {b} = {a*b}"),
    "/": lambda a,b: (f"{a} / {b} = {a/b}") 
}

#function input --> get datas from user
def WelcomeUser():
    bdayYear = False
    year = int(input("Which year we are? "))
    bday = input("Do you already make birthiday this year?(Y/N)").upper()

    if bday == "Y":
        bdayYear = True
    name = input("What is your name? ")
    age = int(input("How old are you? "))
    yearBorn = year - age - (0 if bdayYear else 1)
    user = {
        "Name": name,
        "Year Born": yearBorn,
        "Age": age
    }
    return user

#function output
def show_user_data(user):
    for i in user:
        user_datas = f"{i}:{user[i]}" #to show userdatas more friendly in print
        print(user_datas)
#function output
def operation(op,n1,n2):
    return operations_available[op](n1,n2)

def validate_number(msg):
    while True:
        try:
            return int(input(msg))
        except ValueError:
            print("Invalid number. Try again.")
def get_valid_operation(operation):
        while operation not in operations_available:
            print("Invalid operation, select only one of them:(+,-,/,*)")
            operation = input("Which operation do you wanna make((+)/(-)/(*)/(/))? ").strip()
        return operation
            
            
def get_operation():
    return input("Which operation do you wanna make((+)/(-)/(*)/(/))? ").strip()

def get_numbers():
    num1 = validate_number(("Type the first number: "))
    num2 = validate_number(("Type the second number: "))
    return num1, num2
def calculate(op,n1,n2):
    result = operation(op, n1, n2)
    return result

def exit_program(user,op,n1,n2):
    return "EXIT"

menu = {
    "1": calculate,
    "2": show_user_data,
    "3": exit_program
}

def menufunc():
    print("\n MENU: \n 1:Calculator \n 2:My Informations \n 3:Exit")
    optionmenu = input("Choose one of them options(1/2/3): ")
    while optionmenu not in menu:
        print("Invalid option. Please choose 1, 2, or 3.")
        optionmenu = input("Choose one of them options(1/2/3): ")
    return optionmenu

def add_user(userdata, file="userinfos.json"):
    array1 = []
    with open(file, "r") as f:
        content = f.read().strip()
    if content:
        content_decoded = json.loads(content) #json  str format into python object
        for i in content_decoded:
            array1.append(i)
        array1.append(userdata)
        json_data = json.dumps(array1, indent=4)
        with open("userinfos.json", "w") as f:
            f.write(json_data)

def main():
    user = WelcomeUser()
    user_datas_tuple = {} #stophere



    print(f"Welcome, Mr {user['Name']}, born in {user['Year Born']}, you receive an access to the JVBCalculator")
    """
    jsonusers = json.dumps(user)
    with open("userinfos.json", "a") as userinfojson:
        if userinfojson.tell() > 0:
            userinfojson.write(f"")
        userinfojson.write(f"\n{jsonusers}")
    """
    while True:
        optionmenu = menufunc()
        if optionmenu == "1":
            try:
                calctype = get_operation()
                operation = get_valid_operation(calctype)
                num1, num2 = get_numbers()
                result = menu[optionmenu](operation,num1,num2)
                print(f"Result {result}")
            except ZeroDivisionError:
                print("Division by zero is not allowed")
        elif optionmenu == "2":
            result = menu[optionmenu](user)
        elif optionmenu == "3":
            print("Goodbye! See you later!")
            break
        time.sleep(1)

main()
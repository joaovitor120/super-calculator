import json
from datetime import datetime

userdata =  {"Name": "jo", "Year Born": 2008, "Age": 1}
now = datetime.now()
hour_formated = now.strftime("%H:%M")
day_formated = now.strftime("%d/%m/%Y")
userdata["Day"] = day_formated
userdata["Hours"] = hour_formated
print(userdata)
array = []

"""with open("userinfos.json", "r") as jsonfile:
    jsontext = jsonfile.read()
    array.append(jsontext.strip())
    print(array)"""
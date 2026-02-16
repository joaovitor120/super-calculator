import json

def add_user(userdata, file="userinfos.json"):
    array1 = []
    with open(file, "r") as f:
        content = f.read().strip()
        print(content)
        print(type(content))
    if content:
        content_decoded = json.loads(content) #json  str format into python object
        print(type(content_decoded))
        for i in content_decoded:
            array1.append(i)
        array1.append(userdata)
        print(array1)
        json_data = json.dumps(array1, indent=4)
        print(type(json_data))
        print(json_data)
        with open("userinfos.json", "w") as f:
            f.write(json_data)
        
            
"""        if content:
            datas_json = json.loads(content)
            array1.append(datas_json)
            array1.append(userdata)
            print(array1)
            with open(file, "w") as f1:
                userinfos = json.dumps(array1, indent=4, ensure_ascii="False")
                print(userinfos)
        else: 
            with open(file, "w") as f1:
                json.dump(userdata, f1, indent=4)"""
            

userdata =  {"Name": "jo", "Year Born": 2008, "Age": 1}

add_user(userdata)
#add_user({"Name": "maria", "Year Born": 2010, "Age": 15})
#add_user({'Name': 'a', 'Year Born': 2008, 'Age': 12})
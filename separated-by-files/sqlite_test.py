import sqlite3

name = "joao"
yb = 2008
age = 10
hours = "12"
day = "1"
db = ""
connection = sqlite3.connect(db)
cursor = connection.cursor()
columns = ["Name", "Year_born", "Age", "Hours", "Day"]
tables_formatted = (", ".join(i for i in columns))
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

cursor.execute(f"""
    INSERT INTO User
    ({tables_formatted}) VALUES
    ('{name}', {yb}, {age}, '{hours}', '{day}')""")
connection.commit()
import sqlite3

connection = sqlite3.connect("./database/database.db", timeout=20)
cursor = connection.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS math_challenge
               (
               Id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
               Challenge TEXT NOT NULL,
               Result INTEGER NOT NULL
               )
""")

def add_math_challenge_datas(challenge, result):
    cursor.execute(f"""INSERT INTO math_challenge
                   (Challenge,Result) VALUES
                   ('{challenge}', {result})
""")
    connection.commit()
    connection.close()
import sqlite3

db = "./database/database.db"
connection = sqlite3.connect(db)
cursor = connection.cursor()

cursor.execute("""
DELETE FROM User WHERE id = 2
""")
connection.commit()

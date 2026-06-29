import sqlite3

connection = sqlite3.connect("alphaengine.db")

cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS test (
    id INTEGER PRIMARY KEY,
    name TEXT
)
""")

cursor.execute("""
INSERT INTO test (name)
VALUES (?)
""", ("Hello",))

connection.commit()

cursor.execute("SELECT * FROM test")

rows = cursor.fetchall()

print(rows)

connection.close()
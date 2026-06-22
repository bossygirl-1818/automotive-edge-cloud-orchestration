import sqlite3

conn = sqlite3.connect("data/orchestrator.db")

cursor = conn.cursor()

cursor.execute(
    "SELECT * FROM decisions ORDER BY id DESC LIMIT 10"
)

rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()
import sqlite3

conn = sqlite3.connect("agent_runs.db")
cursor = conn.cursor()

cursor.execute("SELECT version, SUM(correct), COUNT(*) FROM runs GROUP BY version")     # ask for all rows
rows = cursor.fetchall()                  # collect the results

for row in rows:
    print(row)

conn.close()
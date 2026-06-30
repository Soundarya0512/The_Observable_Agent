import sqlite3

conn = sqlite3.connect("agent_runs.db")
cursor = conn.cursor()                    # ← NEW: the cursor

cursor.execute("""
    CREATE TABLE IF NOT EXISTS runs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        version TEXT,
        question TEXT,
        tool_used TEXT,
        attempts INTEGER,
        success INTEGER,
        latency REAL,
        tokens INTEGER,
        correct INTEGER
    )
""")                                       # ← NEW: create the table

conn.commit()                              # ← NEW: save the change
print("Table created!")
conn.close()
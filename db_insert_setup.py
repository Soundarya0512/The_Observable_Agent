import sqlite3
import json
conn=sqlite3.connect("agent_runs.db")
cursor = conn.cursor()  
cursor.execute("DELETE FROM runs")

for filename in ["results_baseline.json", "results_retry.json", "results_modelswap.json"]:
    with open(filename, "r") as f:
        output = json.load(f)

    version = output["version"]

    for items in output["results"]:
        items["version"]=version
        items.setdefault("latency", 0)
        items.setdefault("tokens", 0)
        items.setdefault("tool_used", None)
        items.setdefault("attempts", 0)



    cursor.executemany("""
        INSERT INTO runs (version, question, tool_used, attempts, latency, tokens, correct) 
        VALUES (:version, :question, :tool_used, :attempts, :latency, :tokens, :correct)
    """, output["results"])

conn.commit()
print("Row inserted!")
conn.close()
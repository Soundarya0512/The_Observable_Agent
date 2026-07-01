from fastapi import FastAPI
import sqlite3

app=FastAPI()


@app.get("/scores")
def get_score():
    conn = sqlite3.connect("agent_runs.db")
    cursor = conn.cursor()

    cursor.execute("SELECT version, SUM(correct), COUNT(*) FROM runs GROUP BY version")     # ask for all rows
    rows = cursor.fetchall()
    
    result=[]                  # collect the results

    for row in rows:
        result.append({
            "version":row[0],
            "correct":row[1],
            "total":row[2]
        })
    
    
    conn.close()
    return result
      

      


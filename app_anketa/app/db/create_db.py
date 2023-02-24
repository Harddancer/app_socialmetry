import sqlite3
from settings import DB_NAME

def createAnketa():
    con = sqlite3.connect(DB_NAME)
    if con:
        cur = con.cursor()
        with open('/home/yamamotod/app_socialmetric/app_anketa/app/db/create_db.sql', 'r') as f:
            text = f.read()
        cur.executescript(text)
        cur.close()
        con.close()
        print(cur)
    else:
        print("NOT CONNECT")

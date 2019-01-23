import sqlite3
import os

conn = sqlite3.connect('test.db') #this will hold our connection to our database

with conn: #while we have this open session, do the below
    cur = conn.cursor() #cursor is whats operating on the database. below use the \ to make line breaks on the screen
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_drill2( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_name TEXT \
        )")
    conn.commit() #here we commit our changes



myPath = ('C:\\Users\\ericm\\OneDrive\\Documents\\Python\\PyDrill2')
listDir = os.listdir(myPath)
print(listDir)
i = 0
while i < len(listDir):
    splitPath = os.path.splitext(listDir[i])
    if splitPath[1] == ".txt":
        cur = conn.cursor()
        cur.execute("INSERT INTO tbl_drill2(col_name) VALUES (?)", \
            (listDir[i]))
        conn.commit()
        print(listDir[i])
    i+= 1
    
conn.close()


#Jackson Zou
#SoftDev
#skeleton :: SQLITE3 BASICS
#Oct 2019

import sqlite3
import csv

def addUser(username, password):
    DB_FILE="data/databases.db"

    db = sqlite3.connect(DB_FILE)
    c = db.cursor()

    #==========================================================
    command = "SELECT user_id, username FROM users WHERE username = \"{}\";".format(username)
    c.execute(command)
    new = c.fetchall()
    if len(new) == 0:
        command = "SELECT user_id FROM users;"
        c.execute(command)
        q = c.fetchall()
        command = "INSERT INTO users VALUES({}, \"{}\", \"{}\");".format(q[len(q)-1][0]+1,username,password)
        c.execute(command)
        db.commit() #save changes
        db.close()  #close database
        return True
    else:
        db.commit() #save changes
        db.close()  #close database
        return False
    #==========================================================

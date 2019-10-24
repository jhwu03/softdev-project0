#Jackson Zou
#SoftDev
#skeleton :: SQLITE3 BASICS
#Oct 2019

import sqlite3
import csv

def checkLogin(username, password):
    DB_FILE="data/databases.db"

    db = sqlite3.connect(DB_FILE)
    c = db.cursor()

    #==========================================================
    command = "SELECT id, username FROM users WHERE username = \"{}\" AND password = \"{}\";".format(username, password)
    c.execute(command)
    q = c.fetchall()
    if len(q) == 0:
        return -1 #return -1 if it doesn't exist
    else:
        return q[0][0] #return ID of user if exists
    #==========================================================

    db.commit() #save changes
    db.close()  #close database

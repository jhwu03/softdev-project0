#Jackson Zou
#SoftDev
#skeleton :: SQLITE3 BASICS
#Oct 2019

import sqlite3
import csv

def addEntry(userid, blogid, entrytext):
    DB_FILE="../data/databases.db"

    db = sqlite3.connect(DB_FILE)
    c = db.cursor()

    #==========================================================

    command = "SELECT entry_num FROM entries WHERE user_id = 0 AND blog_id = 1;".format(userid, blogid)
    c.execute(command)
    q = c.fetchall();
    print(q)
    #==========================================================

    db.commit() #save changes
    db.close()  #close database

addEntry(0,1, "bleh");

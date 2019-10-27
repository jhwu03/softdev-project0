#Jackson Zou
#SoftDev
#skeleton :: SQLITE3 BASICS
#Oct 2019

import sqlite3
import csv

def addEntry(userid, blogid, entrytext):
    DB_FILE="data/databases.db"

    db = sqlite3.connect(DB_FILE)
    c = db.cursor()

    #==========================================================

    command = "SELECT entry_num FROM entries WHERE user_id = {} AND blog_id = {};".format(userid, blogid)
    c.execute(command)
    q = c.fetchall();
    newentry_id = q[len(q)-1][0]+1
    command = "INSERT INTO entries VALUES({},{},{},\"{}\");".format(userid, blogid, newentry_id, entrytext)
    c.execute(command)
    #==========================================================

    db.commit() #save changes
    db.close()  #close database

def editEntry(userid, blogid, entrynum, entrytext):
    DB_FILE="data/databases.db"

    db = sqlite3.connect(DB_FILE)
    c = db.cursor()

    #==========================================================
    command = "UPDATE entries SET entry_text = \"{}\" WHERE user_id = {} AND blog_id = {} AND entry_num = {};".format(entrytext, userid, blogid, entrynum)
    c.execute(command)
    #==========================================================

    db.commit() #save changes
    db.close()  #close database

def createBlog(userid, blogtitle):
    DB_FILE="../data/databases.db"

    db = sqlite3.connect(DB_FILE)
    c = db.cursor()

    #==========================================================
    command = "SELECT blog_id FROM blogs WHERE user_id = {};".format(userid)
    c.execute(command)
    q = c.fetchall()
    if len(q) == 0:
        blogid = 1
    else:
        blogid = q[len(q)-1][0] + 1

    command = "INSERT INTO blogs VALUES({},{},\"{}\")".format(userid, blogid, blogtitle)
    c.execute(command)
    command = "INSERT INTO entries VALUES({},{},{},\"{}\")".format(userid, blogid, 0, "Pilot Entry")
    c.execute(command)
    #==========================================================

    db.commit() #save changes
    db.close()  #close database

createBlog(0,"haha")

#Jackson Zou
#SoftDev
#skeleton :: SQLITE3 BASICS
#Oct 2019

import sqlite3
import csv

def displayBlogs(userid):
        DB_FILE="data/databases.db"

        db = sqlite3.connect(DB_FILE)
        c = db.cursor()

        #==========================================================

        command = ""
        c.execute(command)
        #==========================================================

        db.commit() #save changes
        db.close()  #close database

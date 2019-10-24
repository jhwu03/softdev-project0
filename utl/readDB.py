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

        command = "SELECT blogs.user_id, blogs.blog_id, blog_name, entry_num, entry_text FROM blogs INNER JOIN entries ON blogs.user_id = entries.user_id AND blogs.blog_id = entries.blog_id WHERE blogs.user_id = {};".format(userid)
        c.execute(command)
        q = c.fetchall()
        print(q)

        #==========================================================

        db.commit() #save changes
        db.close()  #close database

def displayEntries(userid, blogid)
        DB_FILE="../data/databases.db"

        db = sqlite3.connect(DB_FILE)
        c = db.cursor()

        #==========================================================

        command = "SELECT blogs.user_id, blogs.blog_id, blog_name, entry_num, entry_text FROM blogs INNER JOIN entries ON blogs.user_id = entries.user_id AND blogs.blog_id = entries.blog_id WHERE blogs.user_id = {} AND blogs.blog_id = {};".format(userid, blogid)
        c.execute(command)
        q = c.fetchall()
        print(q)

        #==========================================================

        db.commit() #save changes
        db.close()  #close database

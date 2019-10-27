#Jackson Zou
#SoftDev
#skeleton :: SQLITE3 BASICS
#Oct 2019

import sqlite3
import csv

def displayBlogs(username):
    """Returns all blogs of a user specified by their userid. The return value of this method is going to a list of blogs. The overall list will be organized by [blog1, blog2, blog3, ...] and each blog will be a list so blog1 = [blog_id, blog_name, entry1, entry2, ...]"""
    DB_FILE="data/databases.db"

    db = sqlite3.connect(DB_FILE)
    c = db.cursor()

    #==========================================================
    userid = getUserID(username)
    command = "SELECT blogs.user_id, blogs.blog_id, blog_name, entry_num, entry_text FROM blogs INNER JOIN entries ON blogs.user_id = entries.user_id AND blogs.blog_id = entries.blog_id WHERE blogs.user_id = {};".format(userid)
    c.execute(command)
    q = c.fetchall()
    print(q)
    final = []
    for entry in q:
        index = entry[1] - 1
        if len(final) == index:
            final.append([])
            final[index].append(entry[1])
            final[index].append(entry[2])
            final[index].append(entry[4])
        else:
            final[index].append(entry[4])
    #==========================================================

    db.commit() #save changes
    db.close()  #close database

    return final

def displayEntries(username, blogid):
    """Returns all entries for the specified user_id, blog_id combination. Return value will be a list formatted as [blog_id, blog_name, entry1, entry2,...]"""
    DB_FILE="data/databases.db"

    db = sqlite3.connect(DB_FILE)
    c = db.cursor()

    #==========================================================
    userid = getUserID(username)
    command = "SELECT blog_name, entry_num, entry_text FROM blogs INNER JOIN entries ON blogs.user_id = entries.user_id AND blogs.blog_id = entries.blog_id WHERE blogs.user_id = {} AND blogs.blog_id = {};".format(userid, blogid)
    c.execute(command)
    q = c.fetchall()
    final = []
    final.append(q[0][1])
    final.append(q[0][0])
    for entry in q:
        final.append(entry[2])

    #==========================================================
    db.commit() #save changes
    db.close()  #close database

    return final

def getAllBlogs():
    """Returns the last entry for every existing blog. This will be primarily used in the featured section of the home page. Return value will be a list formatted as [blog1, blog2...]. blog1 will be [blog1_name, entry]"""
    DB_FILE="data/databases.db"

    db = sqlite3.connect(DB_FILE)
    c = db.cursor()

    #==========================================================
    blogs = []
    command = "SELECT user_id, username FROM users;"
    c.execute(command)
    q = c.fetchall()
    for num in range(q[len(q)-1][0]+1):
        entries = displayBlogs(num)
        for entry in entries:
            adding = []
            adding.append(q[num][1])
            adding.append(entry[0])
            adding.append(entry[1])
            adding.append(entry[len(entry)-1])
            blogs.append(adding)
    #==========================================================
    db.commit() #save changes
    db.close()  #close database

    return blogs

def getUserID(username):
    DB_FILE="data/databases.db"

    db = sqlite3.connect(DB_FILE)
    c = db.cursor()

    #==========================================================
    command = "SELECT user_id FROM users WHERE username = \"{}\";".format(username)
    c.execute(command)
    q = c.fetchall()
    if len(q) > 0:
        return q[0][0]
    else:
        return -1
    #==========================================================
    db.commit() #save changes
    db.close()  #close database

def searchUp(search):
    """From the search input it will check through the blogs list on the homepage to
    see which blogs have usernames, blog numbers, blog names, and entries that contain
    the key word"""
    allBlogs = getAllBlogs()
    results = []
    for blog in allBlogs:
        if search in str(blog[0]):
            results.append(blog)
        elif search in str(blog[1]):
            results.append(blog)
        elif search in str(blog[2]):
            results.append(blog)
        elif search in str(blog[3]):
            results.append(blog)
    return results

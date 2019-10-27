# Jackson Zou
# SoftDev1 PD 9
# p00


from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from utl import createDB
from utl import checkLogin
from utl import newuser
from utl import readDB
import sqlite3
app = Flask(__name__)

createDB.createTable() #always create tables when first run, just in case tables don't exist

@app.route("/")
def firstLogin():
    return render_template('login.html',
        errorMessage = "")


@app.route("/login", methods=["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]
    #valid = checkLogin.checkLogin(username,password)
    valid = checkLogin.checkLogin(username, password) #temp for testing
    if (valid == -1):
        return render_template('login.html',
            errorMessage = "Invalid Credentials")
    return redirect(url_for("home", user="LOGGEDIN"))

@app.route("/register")
def register():
    username = request.form["username"]
    password = request.form["password"]

    #add user checks if account exists (returns false). If DNE, enters into database, returns true
    valid = newuser.addUser(username, password)
    if (valid == False):
        return render_template('register.html',
            errorMessage = "Username already taken")
    return redirect(url_for("home", userDATA=username))

@app.route("/home")
def home():
    user = request.args.get('userDATA')
    #VARIABLES TO PASS
    entries = readDB.getAllBlogs()
    return render_template("home.html",
        username = user,
        recentEntries = entries)

@app.route("/{}".format(username))
def userPage():
    #username = session[usernae] reutrn specific template
    return 'ha'

if __name__ == "__main__":
    app.debug = True
    app.run()

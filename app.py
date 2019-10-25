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
import sqlite3
app = Flask(__name__)

createDB.createTable() #always create tables when first run, just in case tables don't exist

DB_FILE = "data/database.db"
db = sqlite3.connect(DB_FILE) #opens existing file or it makes new one if it does not exit
c = db.cursor()               #facilitate db ops

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
    valid = checkLogin.checkLogin(username,password)
    print(valid)
    valid = 0
    if (valid == -1):
        return render_template('register.html',
            errorMessage = "Username already taken")
    return redirect(url_for("home", user="NEWUSER"))

@app.route("/home")
def home():
    user = request.args.get('user')
    #VARIABLES TO PASS
    command = "SELECT blog.username, entries.entry "
    entries = "DISPLAY RECENT ENTRIES"
    return render_template("home.html",
        username = user,
        recentEntries = entries)

if __name__ == "__main__":
    app.debug = True
    app.run()

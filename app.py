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

@app.route("/")
def firstLogin():
    return render_template('login.html',
        errorMessage = "")


@app.route("/login", methods=["GET"])
def login():
    if (request.args):
        username = request.args["username"]
        password = request.args["password"]
        validLogin = checkLogin.checkLogin(username, password) #temp for testing
        if (validLogin == -1):
            return render_template('login.html', errorMessage = "Invalid Credentials")
        return redirect(url_for("home", user=username))
    return render_template("login.html", errorMessage="")


@app.route("/register", methods=["GET"])
def register():
    if (request.args):
        username = request.args["username"]
        password1 = request.args["password1"]
        password2 = request.args["password2"]
        if (password1 == password2):
            if (newuser.addUser(username, password1) == True):
                return redirect(url_for("home", user=username))
            return render_template('register.html',
                errorMessage = "Username already taken")
        return render_template('register.html',
            errorMessage = "Passwords do not match. Please try again.")
    return render_template('register.html', errorMessage = "")

    #add user checks if account exists (returns false). If DNE, enters into database, returns true


@app.route("/home")
def home():
    user = request.args.get('user')
    #VARIABLES TO PASS
    command = "SELECT blog.username, entries.entry "
    entries = "DISPLAY RECENT ENTRIES"
    return render_template("home.html",
        username = user,
        recentEntries = entries)

@app.route("/<user>")
def userPage(user):
    #username = session[usernae] reutrn specific template
    # if user DNE: return error template
    return render_template("user.html",
        user = user,
        allBlogs="TEMP")


if __name__ == "__main__":
    app.debug = True
    app.run()

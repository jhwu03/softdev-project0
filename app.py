# Jackson Zou
# SoftDev1 PD 9
# p00


from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from flask import session
from utl import createDB
from utl import checkLogin
from utl import checkUser
from utl import newuser
from utl import readDB
import sqlite3
import os
app = Flask(__name__)

app = Flask(__name__)
app.secret_key = os.urandom(32) #generates a secret key for session to start
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
        userID = checkLogin.checkLogin(username, password) #temp for testing
        if (userID == -1):
            return render_template('login.html', errorMessage = "Invalid Credentials")
        session['username'] = request.args["username"]          # assign username key in session to inputted username
        session['password'] = request.args["password"]          # assign password key in session to inputted password
        return redirect(url_for("home", user=username))
    return render_template("login.html", errorMessage="")


@app.route("/register", methods=["GET"])
def register():
    if (session):
        username = request.args["username"]
        password1 = request.args["password1"]
        password2 = request.args["password2"]
        if (password1 == password2):
            if (newuser.addUser(username, password1) == True):
                session['username'] = request.args["username"]     # assign username key in session to inputted username
                session['password'] = request.args["password1"]    # assign password key in session to inputted password
                return redirect(url_for("home", user=username))
            return render_template('register.html',
                errorMessage = "Username already taken")
        return render_template('register.html',
            errorMessage = "Passwords do not match. Please try again.")
    return render_template('register.html', errorMessage = "")

    #add user checks if account exists (returns false). If DNE, enters into database, returns true

@app.route("/logout", methods=["GET"])
def logout():      # route logs out the user by getting rid of username and password in session
    session.pop('username')
    session.pop('password')
    if 'password2' in session:
        session.pop('password2')
    return redirect(url_for("firstLogin"))    # redirect to beginning

@app.route("/home")
def home():
    if (session):
        user = request.args.get('user')
        command = "SELECT blog.username, entries.entry "
        entries = readDB.getAllBlogs()
        return render_template("home.html",
            username = user,
            recentEntries = entries)
    return redirect(url_for("firstLogin"))


@app.route("/user/<user>")
def userPage(user, password, temp1, temp2):
    #username = session[usernae] reutrn specific template
    # if user DNE: return error template
    #if (user == session["username"]):

    return render_template("user.html",
        user = user,
        allBlogs="TEMP")

@app.route("/<user>/<blog>")
def blogPage(user):

    return "blog page"

@app.route("/<user>/<blog>/<entry>")
def entryPage(user):
    return "entry page"



if __name__ == "__main__":
    app.debug = True
    app.run()

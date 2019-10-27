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
from utl import newuser
from utl import readDB
import sqlite3
import os
app = Flask(__name__)
app.secret_key = os.urandom(32) #generates a secret key for session to start
createDB.createTable() #always create tables when first run, just in case tables don't exist

@app.route("/")
def firstLogin():
    return render_template('login.html',
        errorMessage = "")


@app.route("/login", methods=["POST"])
def login():
    session['username'] = request.form["username"]          # assign username key in session to inputted username
    session['password'] = request.form["password"]          # assign password key in session to inputted password
    if (session):
        username = session['username']
        password = session['password']
        validLogin = checkLogin.checkLogin(username, password) #temp for testing
        if (validLogin == -1):
            return render_template('login.html', errorMessage = "Invalid Credentials")
        return redirect(url_for("home"))
    return render_template("login.html", errorMessage="")


@app.route("/register", methods=["POST"])
def register():
    session['username'] = request.form["username"]          # assign username key in session to inputted username
    session['password'] = request.form["password1"]          # assign password key in session to inputted password1
    session['password2'] = request.form["password2"]          # assign password key in session to inputted password2
    if (session):
        username = session['username']
        password1 = session['password']
        password2 = session['password2']
        if (password1 == password2):
            if (newuser.addUser(username, password1) == True):
                return redirect(url_for("home"))
            return render_template('register.html',
                errorMessage = "Username already taken")
        return render_template('register.html',
            errorMessage = "Passwords do not match. Please try again.")
    return render_template('register.html', errorMessage = "")

    #add user checks if account exists (returns false). If DNE, enters into database, returns true

@app.route("/logout", methods=["GET"])
def logout():                                               # route logs out the user by getting rid of username and password in session
    session.pop('username')
    session.pop('password')
    if 'password2' in session:
        session.pop('password2')
    return redirect(url_for("firstLogin"))                # redirect to beginning

@app.route("/home")
def home():
    user = session['username']
    #VARIABLES TO PASS
    entries = readDB.getAllBlogs()
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

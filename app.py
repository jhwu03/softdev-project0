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
<<<<<<< HEAD
=======

app = Flask(__name__)
>>>>>>> 2dd79b10cfae865b55c1634ca110e519d2774ee7
app.secret_key = os.urandom(32) #generates a secret key for session to start
createDB.createTable() #always create tables when first run, just in case tables don't exist

@app.route("/")
def firstLogin():
    return render_template('login.html',errorMessage = "")

@app.route("/login", methods=["POST"])
def login():
<<<<<<< HEAD
    print(request.form)
    if(request.form['sub1'] == 'Register'):
        return redirect(url_for("register")), render_template('register.html', errorMessage = "")
    else:
        session['username'] = request.form["username"]          # assign username key in session to inputted username
        session['password'] = request.form["password"]          # assign password key in session to inputted password
        if (session):
            if(session['username'] == None and session['passsword'] == None):
                return redirect(url_for("register")), render_template('register.html',errorMessage = "")
            username = session['username']
            password = session['password']
            validLogin = checkLogin.checkLogin(username, password) #temp for testing
            if (validLogin == -1):
                return render_template('login.html', errorMessage = "Invalid Credentials")
            return redirect(url_for("home"))
        else:
            return render_template('login.html',errorMessage = "")
=======
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
>>>>>>> 2dd79b10cfae865b55c1634ca110e519d2774ee7


@app.route("/register", methods=["POST"])

def register():
<<<<<<< HEAD
    if(request.form['sub1'] == 'Log In'):
        return redirect(url_for("firstLogin"))
    else:
        session['username'] = request.form["username"]          # assign username key in session to inputted username
        session['password'] = request.form["password1"]          # assign password key in session to inputted password1
        session['password2'] = request.form["password2"]          # assign password key in session to inputted password2
        if (session):
            if(session['username'] == None and session['passsword'] == None and session['password2'] == None):
                return redirect(url_for("login")), render_template('login.html',errorMessage = "")
            username = session['username']
            password1 = session['password']
            password2 = session['password2']
            if (password1 == password2):
                if (newuser.addUser(username, password1) == True):
                    return redirect(url_for("home"))
                return render_template('register.html',
                    errorMessage = "Username already taken")
=======
    if (session):
        username = request.args["username"]
        password1 = request.args["password1"]
        password2 = request.args["password2"]
        if (password1 == password2):
            if (newuser.addUser(username, password1) == True):
                session['username'] = request.args["username"]     # assign username key in session to inputted username
                session['password'] = request.args["password1"]    # assign password key in session to inputted password
                return redirect(url_for("home", user=username))
>>>>>>> 2dd79b10cfae865b55c1634ca110e519d2774ee7
            return render_template('register.html',
                errorMessage = "Passwords do not match. Please try again.")
        return render_template('register.html', errorMessage = "")

    #add user checks if account exists (returns false). If DNE, enters into database, returns true

@app.route("/logout", methods=["GET"])
<<<<<<< HEAD
def logout():                                               # route logs out the user by getting rid of username and password in session
=======
def logout():      # route logs out the user by getting rid of username and password in session
>>>>>>> 2dd79b10cfae865b55c1634ca110e519d2774ee7
    session.pop('username')
    session.pop('password')
    if 'password2' in session:
        session.pop('password2')
<<<<<<< HEAD
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
=======
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
>>>>>>> 2dd79b10cfae865b55c1634ca110e519d2774ee7
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

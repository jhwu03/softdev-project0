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
    valid = 0 #temp for testing
    if (valid == -1):
        return render_template('login.html',
            errorMessage = "Invalid Credentials")
    return redirect(url_for("home", user="LOGGEDIN"))

@app.route("/register")
def register():
    username = request.form["username"]
    password1 = request.form["password1"]
    password2 = request.form["password2"]

    #VALID REPRESENTS WHETHER THE USERNAME IS UNIQUE OR NOT!! CHECKLOGIN METHOD
    #valid = checkLogin.checkLogin(username,password)
    valid = 0
    if (valid == -1):
        return render_template('register.html',
            errorMessage = "Username already taken")
    if (password1 != password2): #.equals() ?)
        return render_template('register.html',
            errorMessage = "Passwords do not match. Please try again.")
    return redirect(url_for("home", user="NEWUSER"))

@app.route("/home")
def home():
    user = request.args.get('user')
    #VARIABLES TO PASS
    entries = "DISPLAY RECENT ENTRIES"
    return render_template("home.html",
        username = user,
        recentEntries = entries)

if __name__ == "__main__":
    app.debug = True
    app.run()

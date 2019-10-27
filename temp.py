@app.route("/user/<user>")
def userPage(user):
    #username = session[usernae] reutrn specific template
    # if user DNE: return error template
    if (user == session["username"]):
        return render_template("user.html",
            user = user,
            myBlogs = readDB.displayBlogs(session["userID"]))
    return render_template("otherUser.html",
        user = user,
        theirBlogs="TEMP")

@app.route("/<user>/<blog>")
def blogPage(user):

    return "blog page"

@app.route("/<user>/<blog>/<entry>")
def entryPage(user):
    return "entry page"



if __name__ == "__main__":
    app.debug = True
    app.run()

from flask import Flask, render_template, request, session, redirect, url_for
import os
app.secret_key = os.urandom(32) #generates a secret key for session to start
def checkIfLoggedIn():
    if (session):
        if (session['username'] == "hello"):                # checks if user is logged in
            if (session['password'] == "world"):            #               ^
                return redirect(url_for("welcome"))         # if logged in redirects to welcome page
    #print('Cookies Not Found')
    return render_template(                                 # if not then render login page
        'login.html',
        message = "Hello user! Please enter your username and password:"
    )

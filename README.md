# TOPZ BLOGS by TOPZ

Connor Oh: HTML related methods
* Utilize Jinja/Flask
* Login methods
* Make methods to display/format user page, blogs, entries

Winston Peng: Facilitating data entry into DB
* Adding/Remove/Editing blog entries
* Sends entry to database, request entries

Manfred: Project Manager, HTML designer
* HTML for web pages

Jackson Zou: managing DB
* Formatting Databases
* Organizing data
* Methods to properly store data


### Instructions on how to run project

First run the commands to install the dependencies in the terminal. Then clone the
repo and run: ```pip3 install flask``` to start the website. Find the local host url
and enter that url into a browser. In order to access the site, a user must create
an account. Create a unique username and password in the register page. After
making the new account, you may now create a new blog and add entries to the new
blog.

#### Dependencies
* flask: ```pip3 install flask```
http://flask.palletsprojects.com/en/1.1.x/
* SQLite: ```pip3 install pysqlite3```
https://www.sqlite.org/doclist.html

#### Special modules/libraries
```
from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
```

- "Flask" creates web pages that we can host on our local server. This is the backbone of our code, as we would not be able to "turn on" the website without flask. Our code utilizes the route methods to create new routes within the website.
http://flask.palletsprojects.com/en/1.1.x/
- "render_template" allows python functions to open and display HTML files onto a
specified url. This creates a user interface that a user can interact with, which
is essential for our website to work. Each python function of each route utilizes the render_template function to display the corresponding HTML file.
http://flask.palletsprojects.com/en/1.1.x/quickstart/#rendering-templates
- "request" allows arguments sent from the user to reach our python functions. We
use the request function to get the form data of the user, such as the username and
password they submit to us. It is necessary for us to check the user's session and
log them into their accounts. We also use it as the backbone of adding blogs and entries.
http://flask.palletsprojects.com/en/1.1.x/quickstart/#accessing-request-data
- "redirect" sends users from one url to another url. It sends the user to a new
route, which is necessary since users must be able to move from page to page and
view other blogs. Our project has links and buttons that lead to other users' blogs
which utilize the redirect function.
http://flask.palletsprojects.com/en/1.1.x/quickstart/#redirects-and-errors
- "url_for" finds the corresponding url of a python function. It finds the route
associated with the python function underneath it. We use this in app.py in order to
change urls and send data from one function to another.
http://flask.palletsprojects.com/en/1.1.x/quickstart/#unique-urls-redirection-behavior

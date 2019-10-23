# Jackson Zou
# SoftDev1 PD 9
# p00


from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from utl import createDB
app = Flask(__name__)

@app.route("/")
def hello_world():
    createDB.createTable() #always create tables when first run, just in case tables don't exist
    return "hi"

if __name__ == "__main__":
    app.debug = True
    app.run()

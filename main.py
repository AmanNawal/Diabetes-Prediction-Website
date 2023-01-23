from flask import Flask
from flask import render_template
app = Flask(__name__)
#PS J:\0. 8th sem project> set FLASK_APP=main.py
#$env:FLASK_DEBUG = "1"
#PS J:\0. 8th sem project> $env:FLASK_APP = "main.py"
#PS J:\0. 8th sem project> flask run
@app.route("/")
@app.route("/home")
def home_page():
    return render_template("home.html")

@app.route("/about") #static routing
def aboutProject():
    return render_template("/about.html")

#@app.route("/about/<username>")         #Dynamic routing
#def userInfo(username):
#    return "hello the name of the about person is {}".format(username)

@app.route("/acetone")
def predict():
    return render_template("acetone.html")

@app.route("/login")
def userLogin():
    return render_template("login.html")

@app.route("/register")
def userRegister():
    return render_template("register.html")

@app.route("/nav")
def navigation():
    return render_template("navigation.html")

@app.route("/acetone")
def predictAcetone():
    return render_template("acetone.html")

@app.route("/normalprediction")
def normalPrediction():
    return render_template("normalprediction.html")

@app.route("/device")
def iotDevice():
    return render_template("device.html")




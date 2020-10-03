from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    print ("Handeling request to home page")
    return "Hello Azure!"

@app.route("/login")
def login():
    print ("Handeling request to login page")
    return "login page"

@app.route("/logout")
def logout():
    print ("Handeling request to logout page")
    return "logout page"
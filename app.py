from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    print ("Handeling request to home page")
    return "Hello Azure!"

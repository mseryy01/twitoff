""" Minimal Flask App"""
from flask import flask

#Make App
app = Flask(__name__)

# Make the route
@app.route("/")

#Define function
def hello():
    return "Hello World!"

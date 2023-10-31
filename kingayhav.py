a=2 
from flask import Flask
app=Flask(__name__)
@app.route("/")
def home():
    return "Hello, Flask!"

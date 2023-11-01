from flask import Flask, render_template, request, jsonify, Blueprint
views=Blueprint("views","__name__")
@views.route("/")
def index():
    return render_template('index.html')
@views.route('/result') #type: ignore
def payhav():
    return render_template("result.html")


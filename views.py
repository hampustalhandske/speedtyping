from flask import Blueprint, render_template



views = Blueprint(__name__, "views")

@views.route("/")
def home():
    return render_template("index.html")

@views.route("/main.html") 
def main():
    return render_template("main.html")

@views.route("result.html")
def result():
    return render_template("/result.html")


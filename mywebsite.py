from flask import Flask,render_template
from flask_bootstrap import Bootstrap


myflask = Flask(__name__)
Bootstrap(myflask)

@myflask.route("/")
def home():
    return render_template("welcome.html")

@myflask.route("/demo1")
def demo1():
    return render_template("demo1.html")

@myflask.route("/demo2")
def demo2():
    return render_template("demo2.html")

@myflask.route("/login",methods=['GET','POST'])
def login():
    return render_template("login.html")

if __name__ == "__main__":
    myflask.run()
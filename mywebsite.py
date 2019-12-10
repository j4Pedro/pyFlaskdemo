from flask import Flask
from flask import render_template
myflask = Flask(__name__)

@myflask.route("/")
def home():
    return render_template("demo1.html")

@myflask.route("/demo1")
def demo1():
    return render_template("demo1.html")

if __name__ == "__main__":
    myflask.run()
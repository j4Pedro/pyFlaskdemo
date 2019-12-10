from flask import Flask
from flask import render_template
myflask = Flask(__name__)

@myflask.route("/")
def home():
    return render_template("welcome.html")


if __name__ == "__main__":
    myflask.run()
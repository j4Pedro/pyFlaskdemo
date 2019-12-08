from flask import Flask
myflask = Flask(__name__)

@myflask.route("/")
def home():
    return "Flask app test!!"

if __name__ == "__main__":
    myflask.run()
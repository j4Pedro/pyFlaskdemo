from flask import Flask
mflask = Flask(__name__)

@mflask.route("/")
def home():
    return "Flask app test!!"

if __name__ == "__main__":
    mflask.run()
import sqlite3
from flask import Flask,render_template,redirect,request
from model import db
import bcrypt
from helper import hashpw

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:/// database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 

db.init_app(app)

messageList = ["this","that"]
topicList=["one","two", "three"]

# @app.route("/")
# def hello_world():
#     return render_template ("index.html")

@app.route('/', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':

        username = request.form['username']
        password = request.form['password']

        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        

        cursor.execute("SELECT * FROM User WHERE name=?", (username,))
        is_user = cursor.fetchone()

        if is_user:
            return render_template('dashboard.html')

        if hashpw(username,password):
            return render_template('dashboard.html')
        else:
            error = 'Invalid username/password combination'


    return render_template('index.html', error=error)


@app.route("/blog")
def blog():
    return render_template("blog.html")

@app.route("/dashboard", methods=["POST"])
def news():
    return render_template("dashboard.html")

@app.route("/message", methods=["POST", "GET"])
def message():
    return render_template("message.html",len = len(messageList), messageList = messageList)

@app.route("/topic", methods=["POST", "GET"])
def topic():
    return render_template("topic.html",len = len(topicList), topicList = topicList)


if __name__ == "__main__":
    app.run()
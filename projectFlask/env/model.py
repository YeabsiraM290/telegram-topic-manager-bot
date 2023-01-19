from flask import Flask,render_template,redirect,request
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:/// database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 

db= SQLAlchemy(app)



class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(50), unique=True)

    def __repr__(self):
        return f'<User: {self.email}>'

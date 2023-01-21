import bcrypt
import sqlite3
from flask import Flask,render_template,redirect,request
from model import db

def hashpw(username,password):

    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    new_pass=cursor.execute("SELECT password FROM User WHERE name=?", (username,))

    bcrypt.checkpw(password, new_pass )
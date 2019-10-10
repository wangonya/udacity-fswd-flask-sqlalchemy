#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DB_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)


db.create_all()


@app.route("/")
def hello_world():
    person = Person.query.first()
    if person:
        return f"Hello {person.name}!"
    else:
        return "Hello World!"

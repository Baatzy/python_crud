from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/python_monster_trucks'
db = SQLAlchemy(app)
# app.config.from_object('config')

from app import routes

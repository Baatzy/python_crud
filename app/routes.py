from app import app, db
from flask import Flask, jsonify, render_template, redirect, request


class MonsterTruck (db.Model):
    __tablename__ = 'monster_trucks'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    color = db.Column(db.String(25))
    driver_name = db.Column(db.String(50))


    def __init__(self, name, color, driver_name):
        self.name = name
        self.color = color
        self.driver_name = driver_name

    def __repr__(self):
        return '<MonsterTruck %r>' % self.name






# from sqlalchemy import create_engine
# from sqlalchemy import Column, String
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker
#
# @app.route('/')
# @app.route('/index')
# def index():
#     user = { 'name': 'Stefan' }
#     return jsonify(**user)
#
#
# db_string = "postgresql://localhost/python_monster_trucks"
#
# db = create_engine(db_string)
# base = declarative_base()
#
# class MonsterTruck (base):
#     __tablename__ = 'monster_trucks'
#
#     name = Column(String, primary_key=True)
#     color = Column(String)
#     driver_name = Column(String)
#
# Session = sessionmaker(db)
# session = Session()
#
# base.metadata.create_all(db)
#
# # Create
# newTruck = MonsterTruck(name="Doctor Crush", color="Orange", driver_name="Bobus")
# session.add(newTruck)
# session.commit()
#
# # Read
# films = session.query(Film)
# for film in films:
#     print(film.title)
#
# # Update
# doctor_strange.title = "Some2016Film"
# session.commit()
#
# # Delete
# session.delete(doctor_strange)
# session.commit()

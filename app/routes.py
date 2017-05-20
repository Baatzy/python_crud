from app import app, db
from flask import Flask, jsonify, render_template, redirect, request


class MonsterTruck (db.Model):
    __tablename__ = 'monster_trucks'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    color = db.Column(db.String(25))

    def __init__(self, name, color):
        self.name = name
        self.color = color

    def __repr__(self):
        return '<MonsterTruck %r>' % self.name

#GET HOMEPAGE
@app.route('/')
def home ():
    return render_template('home.html')

#GET ALL TRUCKS
@app.route('/monster_trucks')
def index ():
    trucks = MonsterTruck.query.all()
    return render_template('index.html', trucks=trucks)

#GET ONE TRUCK
@app.route('/monster_trucks/<page_id>/')
def show (page_id):
    truck = MonsterTruck.query.filter_by(id=page_id)
    return render_template('show.html', truck=truck)

#GET NEW TRUCK FORM
@app.route('/monster_trucks/new')
def new ():
    return render_template('new.html')

#POST NEW TRUCK
@app.route('/new', methods=['POST'])
def postTruck ():
    newTruck = MonsterTruck(request.form['name'], request.form['color'])
    db.session.add(newTruck)
    db.session.commit()
    return redirect('/monster_trucks')

#GET EDIT TRUCK FORM
@app.route('/monster_trucks/<page_id>/edit')
def edit (page_id):
    truck = MonsterTruck.query.filter_by(id=page_id)
    return render_template('edit.html', truck=truck)

#UPDATE ONE TRUCK
@app.route('/new', methods=['PUT'])
def putTruck ():
    newTruck = MonsterTruck(request.form['name'], request.form['color'])
    db.session.add(newTruck)
    db.session.commit()
    return redirect('/monster_trucks')

#DELETE ONE TRUCK

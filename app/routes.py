from app import app, db
from flask import Flask, jsonify, render_template, redirect, request, url_for


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
@app.route('/monster_trucks/<id>/')
def show (id):
    truck = MonsterTruck.query.filter_by(id=id).first()
    return render_template('show.html', truck=truck)

#GET NEW TRUCK FORM
@app.route('/monster_trucks/new')
def new ():
    return render_template('new.html')

#POST NEW TRUCK
@app.route('/new_truck', methods=['POST'])
def postTruck ():
    newTruck = MonsterTruck(request.form['name'], request.form['color'])
    db.session.add(newTruck)
    db.session.commit()
    return redirect('/monster_trucks')

#GET EDIT TRUCK FORM
@app.route('/monster_trucks/<id>/edit')
def edit (id):
    truck = MonsterTruck.query.filter_by(id=id).first()
    return render_template('edit.html', truck=truck)

#UPDATE ONE TRUCK
@app.route('/update_truck/<id>/', methods=['GET', 'PUT'])
def putTruck (id):
    if request.method == 'GET':
        print('Hit GET for the PUT route.')

    if request.method == 'DELETE':
        print('Hit PUT for the PUT route!!!')

    truck = MonsterTruck.query.filter_by(id=id).first()
    truck.name = request.form['name']
    truck.color = request.form['color']
    db.session.commit()
    return redirect(f'/monster_trucks/{id}')

#DELETE ONE TRUCK
@app.route('/delete_truck/<id>/', methods=['GET', 'DELETE'])
def deleteTruck (id):
    if request.method == 'GET':
        print('Hit GET for the DELETE route.')

    if request.method == 'DELETE':
        print('Hit DELETE for the DELETE route!!!')
        
    MonsterTruck.query.filter_by(id=id).delete()
    db.session.commit()
    return redirect(url_for('index'))

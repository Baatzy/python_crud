from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import render_template, request, redirect, url_for

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/python_monster_trucks'
app.debug = True
db = SQLAlchemy(app)

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
@app.route('/monster_trucks/edit/<id>/')
def edit (id):
    truck = MonsterTruck.query.filter_by(id=id).first()
    return render_template('edit.html', truck=truck)

#UPDATE ONE TRUCK
@app.route('/monster_trucks/edit/<id>/update', methods=['POST'])
def putTruck (id):
    truck = MonsterTruck.query.filter_by(id=id).first()
    truck.name = request.form['name']
    truck.color = request.form['color']
    db.session.commit()
    return redirect(f'/monster_trucks/{id}')

#DELETE ONE TRUCK
@app.route('/delete_truck/<id>', methods=['POST'])
def deleteTruck (id):
    MonsterTruck.query.filter_by(id=id).delete()
    db.session.commit()
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run()

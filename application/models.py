from application import db # import the sqlalchemy object (db) created for our app

#  will need to change these to our relevant things
#  need to change these classes to plants and customers?? Will change once we have the database info
class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)
    cars = db.relationship('Car', backref='person')


class Car(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    number_plate = db.Column(db.String(7), nullable=False)
    colour = db.Column(db.String(10), nullable=False)
    make = db.Column(db.String(20), nullable=False)
    model = db.Column(db.String(20), nullable=False)
    person_id = db.Column(db.Integer, db.ForeignKey('person.id'), nullable=False)


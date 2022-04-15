from flask import render_template, request
from application import app, db
from application.forms import BasicForm
from application.models import Person, Car


@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def register():
    error = ""
    form = BasicForm()

    if request.method == 'POST':
        first_name = form.first_name.data
        last_name = form.last_name.data

        if len(first_name) == 0 or len(last_name) == 0:
            error = "Please supply both first and last name"
        else:
            person = Person(first_name=first_name, last_name=last_name)
            db.session.add(person)
            db.session.commit()
            return 'Thank you!'
    return render_template('home.html', form=form, message=error, title='home')

# made this simple home route to try and get it working
# @app.route('/home', methods=['GET'])
# def home():
#     return render_template('home.html', title='home')


@app.route('/people', methods=['GET'])
def show_people():
    error = ""
    people = Person.query.all()
    if len(people) == 0:
        error = "There are no people to display"
        print(people)
    return render_template('people.html', people=people, message=error)

@app.route('/cars', methods=['GET'])
def show_cars():
    error = ""
    cars = Car.query.all()
    if len(cars) == 0:
        error = "There are no cars to display"
        print(cars)
    return render_template('cars.html', cars=cars, message=error, title="Car")


@app.route('/people/<int:person_id>', methods=['GET'])
def show_person(person_id):
    error = ""
    # use filter_by for any column
    # person = Person.query.filter_by(id=person_id).first()
    #  use get for the PK
    person = Person.query.get(person_id)

    # simpsons = Person.query.filter_by(last_name="simpson").all()

    # to sort
    # simpsons = Person.query.filter_by(last_name="simpson").order_by(Person.first_name).all()
    # descending sort
    # simpsons = Person.query.filter_by(last_name="simpson").order_by(Person.first_name.desc()).all()
    # limit to top 2 simpsons
    simpsons = Person.query.filter_by(last_name="simpson").order_by(Person.first_name).limit(2).all()
    if not person:
        error = "There is no person with ID: " + str(person_id)
        print(person)
    return render_template('person.html', person=person, message=error, title="Person", family=simpsons)


@app.route('/people/<int:person_id>', methods=['PUT'])
def update_person(person_id):
    error = ""
    person = Person.query.get(person_id)
    person.last_name = "Flanders"
    db.session.commit()
    if not person:
        error = "There is no person with ID: " + str(person_id)
        print(person)
    return render_template('person.html', person=person, message=error, title="Person", family=[])


@app.route('/people/<int:person_id>/<string:new_last_name>', methods=['PUT'])
def update_person_with_name(person_id, new_last_name):
    error = ""
    person = Person.query.get(person_id)
    person.last_name = new_last_name
    db.session.commit()
    if not person:
        error = "There is no person with ID: " + str(person_id)
        print(person)
    return render_template('person.html', person=person, message=error, title="Updated Person", family=[])


@app.route('/people/<int:person_id>', methods=['DELETE'])
def delete_person(person_id):
    error = ""
    person = Person.query.get(person_id)
    db.session.delete(person)
    db.session.commit()
    people = Person.query.all()
    if not person:
        error = "There is no person with ID: " + str(person_id)
        # print(person)
    return render_template('people.html', people=people, message=error, title="People")


@app.route('/personandcars/<int:person_id>', methods=['GET'])
def people_and_cars(person_id):
    error = ""
    person = Person.query.get(person_id)
    # cars= person.cars
    if not person:
        error = "There is no person with ID: " + str(person_id)
        print(person)
        # print(person_and_carinfo)
    return render_template('person_and_cars.html', person=person, message=error, title="Person and Car Info")

    # return render_template('home.html', form=form, message=error)


@app.route('/about', methods=['GET'])
def about():
    return render_template('about.html', title='About')


@app.route('/contact_us', methods=['GET'])
def contact():
    return render_template('contact_us.html', title='Contact Us')


@app.route('/plant_care', methods=['GET'])
def plant_care():
    return render_template('plant_care.html', title='Plant Care')


@app.route('/shop', methods=['GET'])
def shop():
    return render_template('shop.html', title='Shop')


@app.route('/plant1', methods=['GET'])
def plant1():
    return render_template('plant1.html', title='Plant 1')


@app.route('/plant2', methods=['GET'])
def plant2():
    return render_template('plant2.html', title='Plant 2')


@app.route('/plant3', methods=['GET'])
def plant3():
    return render_template('plant3.html', title='Plant 3')


@app.route('/plant4', methods=['GET'])
def plant4():
    return render_template('plant4.html', title='Plant 4')


@app.route('/plant5', methods=['GET'])
def plant5():
    return render_template('plant5.html', title='Plant 5')


@app.route('/plant6', methods=['GET'])
def plant6():
    return render_template('plant6.html', title='Plant 6')


@app.route('/plant7', methods=['GET'])
def plant7():
    return render_template('plant7.html', title='Plant 7')


@app.route('/plant8', methods=['GET'])
def plant8():
    return render_template('plant8.html', title='Plant 8')


@app.route('/plant9', methods=['GET'])
def plant9():
    return render_template('plant9.html', title='Plant 9')


@app.route('/plant10', methods=['GET'])
def plant10():
    return render_template('plant10.html', title='Plant 10')
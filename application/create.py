# This file should be run manually (directly) to pre-populate
# the database
# NOTE! The database MUST exist before we try to connect to it

from application import db
from application.models import Person, Car # Victoria's code
from application.models import PlantType

# these are the 11 tables we want to create, UserLogin, OrderHistory currently causing errors so not included
# Staff, Address, Customer,  OrderStatus, Category, Size, Product, Order add to import statement once created

# create our database schema
# db.create_all()

db.drop_all()
db.create_all()

# will need to use the db.session.add() code below to add the data - use lists as Victoria has below to make it easier?
# then need db.session.commit() to actually save it to the database
# once this code is populated, running it seperately should make everything appear in the database!


plant1 = PlantType(plant_type_description='Cacti/Succulent')
plant2 = PlantType(plant_type_description='Hanging')
plant3 = PlantType(plant_type_description='Flowering')
plant4 = PlantType(plant_type_description='Palms')
plant5 = PlantType(plant_type_description='Ferns')
plant_types = [plant1, plant2, plant3, plant4, plant5]

db.session.add_all(plant_types)
db.session.commit()

# Victoria's Code:

testPerson1 = Person(first_name='Julie',last_name='Dooley')
testPerson2 = Person(first_name='Victoria',last_name='Lloyd')

car1 = Car(number_plate='JU21DOO', person_id=1, colour='Red', make="Ferrari", model='V12')
car2 = Car(number_plate='JU20XXX', person_id=1, colour='Black', make="Mercedes-Benz", model='CLS')
car3 = Car(number_plate='VL21LLO', person_id=2, colour='Grey', make="Ford", model='Focus')

cars = [car1, car2, car3]
# car4 = Car(number_plate='BART21', person_id=3)

db.session.add(testPerson1)
db.session.add(testPerson2)
# db.session.add(car1)
# db.session.add(car2)
# db.session.add(car3)

db.session.add_all(cars)
# db.session.add(car4)
db.session.commit()

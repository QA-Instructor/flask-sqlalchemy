# This file should be run manually (directly) to pre-populate
# the database
# NOTE! The database MUST exist before we try to connect to it

# add one extra table for newsletter signup - just email

from application import db
# from application.models import Person, Car  # Victoria's code
from application.models import PersonType, UserLogin,  Address, Person, OrderStatus, Category, PlantType, Size,\
    Product, OrderHeader, OrderLine

# Staff,Customer,
# these are the 12 tables we want to create in order:
# PersonType, UserLogin, Address, Person, OrderStatus, Category, PlantType, Size, Product,
# OrderHeader, OrderLine

# create our database schema
# db.create_all()

db.drop_all()
db.create_all()

# will need to use the db.session.add() code below to add the data - use lists as Victoria has below to make it easier?
# then need db.session.commit() to actually save it to the database
# once this code is populated, running it seperately should make everything appear in the database!

# PersonType table
person_type1 = PersonType(person_type_description='Staff')
person_type2 = PersonType(person_type_description='Customer')
person_types = [person_type1, person_type2]

# user login without person type
user1 = UserLogin(username='tedlikesplants', password='1buyingaPLANT!')
user2 = UserLogin(username='rebecca_w', password='Panda42')
user3 = UserLogin(username='keeley.jones', password='passworDx4')
user4 = UserLogin(username='roy.kent', password='Richmond12')
user5 = UserLogin(username='sam_obisanya', password='FootballandPlants1')
user6 = UserLogin(username='natasha', password='staffaccess4')
user7 = UserLogin(username='jodie', password='staffaccess4')
user8 = UserLogin(username='jody', password='staffaccess4')
user9 = UserLogin(username='isabel', password='staffaccess4')
users = [user1, user2, user3, user4, user5, user6, user7, user8, user9]


# address table
address1 = Address(address_line_one='AFC Richmond Club House', address_line_two='Nelson Road',
                   address_line_three='London', postcode='TW9 4RP')
address2 = Address(address_line_one='49 Kings Road', address_line_two='Chelsea', address_line_three='London',
                   postcode='SW3 5TT')
address3 = Address(address_line_one='4 Portland Terrace', address_line_two='The Green', address_line_three='Richmond',
                   postcode='TW9 1QQ')
address4 = Address(address_line_one='The Plant Emporium', address_line_two='Sky Studios', postcode='TW7 5QD')
addresses = [address1, address2, address3, address4]


# person table
person1 = Person(first_name='Ted', last_name='Lasso', email='ted.lasso@afc_richmond.co.uk', address_id=1,
                     phone_number='07384957162', user_login_id=1, person_type_id=2)
person2 = Person(first_name='Rebecca', last_name='Welton', email='rebecca_welton@gmail.com', address_id=1,
                     phone_number='07492750173', user_login_id=2, person_type_id=2)
person3 = Person(first_name='Keeley', last_name='Jones', email='keeley_jones@gmail.com', address_id=2,
                     phone_number='07553630090', user_login_id=3, person_type_id=2)
person4 = Person(first_name='Roy', last_name='Kent', email='roy.kent@afc_richmond.co.uk', address_id=3,
                     phone_number='07554124856', user_login_id=4, person_type_id=2)
person5 = Person(first_name='Sam', last_name='Obisanya', email='sam.obisanya@afc_richmond.co.uk', address_id=1,
                     phone_number='07889578112', user_login_id=5, person_type_id=2)
person6 = Person(first_name='Natasha', last_name='Edun', email='natasha@plantemporium.com', address_id=4,
                     phone_number='07777777777',user_login_id=6, person_type_id=1)
person7 = Person(first_name='Jodie', last_name='Smith', email='jodie@plantemporium.com', address_id=4,
                     phone_number='07777777777', user_login_id=7, person_type_id=1)
person8 = Person(first_name='Jody', last_name='Broad', email='jody@plantemporium.com', address_id=4,
                     phone_number='07777777777', user_login_id=8, person_type_id=1)
person9 = Person(first_name='Isabel', last_name='Tulloch', email='isabel@plantemporium.com', address_id=4,
                     phone_number='07777777777', user_login_id=9, person_type_id=1)
persons = [person1, person2, person3, person4, person5, person6, person7, person8, person9]


# order status
status1 = OrderStatus(status_description='Ordered')
status2 = OrderStatus(status_description='Processing')
status3 = OrderStatus(status_description='Shipped')
status4 = OrderStatus(status_description='Collected')
status5 = OrderStatus(status_description='Returned')
status = [status1, status2, status3, status4, status5]


# category
category1 = Category(category_description='Indoor')
category2 = Category(category_description='Outdoor')
categories = [category1, category2]


# plant type table
plant1 = PlantType(plant_type_description='Cacti/Succulent')
plant2 = PlantType(plant_type_description='Hanging')
plant3 = PlantType(plant_type_description='Flowering')
plant4 = PlantType(plant_type_description='Palms')
plant5 = PlantType(plant_type_description='Ferns')
plant_types = [plant1, plant2, plant3, plant4, plant5]


# size
size1 = Size(size_description='Tiny')
size2 = Size(size_description='Small')
size3 = Size(size_description='Medium')
size4 = Size(size_description='Tall')
sizes = [size1, size2, size3, size4]

# product table
product1 = Product(species='Boston Fern', price=12, stock=8, category_id=1, plant_type_id=5, size_id=1)
product2 = Product(species='Aloe Vera', price=4, stock=10, category_id=1, plant_type_id=1, size_id=2)
product3 = Product(species='Parlour Palm', price=8.99, stock=3, category_id=1, plant_type_id=4, size_id=2)
product4 = Product(species='Anthurium', price=20, stock=5, category_id=1, plant_type_id=3, size_id=3)
product5 = Product(species='Swiss Cheese Plant', price=85.5, stock=1, category_id=1, plant_type_id=4, size_id=4)
product6 = Product(species='Sweet Orange Tree', price=65, stock=4, category_id=2, plant_type_id=3, size_id=4)
product7 = Product(species='Climbing Rose', price=30, stock=3, category_id=2, plant_type_id=3, size_id=3)
product8 = Product(species='Fatsia Japonica', price=55, stock=2, category_id=2, plant_type_id=5, size_id=3)
product9 = Product(species='Hydrangea Macrophylla', price=29.99, stock=5, category_id=2, plant_type_id=4, size_id=2)
product10 = Product(species='Alstroemeria', price=27, stock=8, category_id=2, plant_type_id=4, size_id=1)
products = [product1, product2, product3, product4, product5, product6, product7, product8, product9, product10]


# OrderHeader linking to person only (as customer) without dates
order1 = OrderHeader(person_id=1, status_id=1, total_cost=54.00)
order2 = OrderHeader(person_id=2, status_id=4, total_cost=26.97)
order3 = OrderHeader(person_id=3, status_id=3, total_cost=197.97)
order4 = OrderHeader(person_id=4, status_id=4, total_cost=20.00)
order5 = OrderHeader(person_id=1, status_id=4, total_cost=195.00)
plant_orders = [order1, order2, order3, order4, order5]


# orderLine
order_line1 = OrderLine(order_header_id=1, product_id=10, quantity=2, price_paid=54.00)
order_line2 = OrderLine(order_header_id=2, product_id=3, quantity=1, price_paid=26.97)
order_line3 = OrderLine(order_header_id=3, product_id=5, quantity=2, price_paid=171.00)
order_line4 = OrderLine(order_header_id=3, product_id=4, quantity=4, price_paid=80.00)
order_line5 = OrderLine(order_header_id=4, product_id=2, quantity=2, price_paid=8.00)
order_line6 = OrderLine(order_header_id=4, product_id=1, quantity=1, price_paid=12.00)
order_line7 = OrderLine(order_header_id=5, product_id=6, quantity=3, price_paid=195.00)
order_lines = [order_line1, order_line2, order_line3, order_line4, order_line5, order_line6, order_line7]

db.session.add_all(person_types)
db.session.add_all(users)
db.session.add_all(addresses)
db.session.add_all(persons)
db.session.add_all(status)
db.session.add_all(categories)
db.session.add_all(plant_types)
db.session.add_all(sizes)
db.session.add_all(products)
db.session.add_all(plant_orders)
db.session.add_all(order_lines)



db.session.commit()

# Victoria's Code:

# testPerson1 = Person(first_name='Julie', last_name='Dooley')
# testPerson2 = Person(first_name='Victoria', last_name='Lloyd')
#
# car1 = Car(number_plate='JU21DOO', person_id=1, colour='Red', make="Ferrari", model='V12')
# car2 = Car(number_plate='JU20XXX', person_id=1, colour='Black', make="Mercedes-Benz", model='CLS')
# car3 = Car(number_plate='VL21LLO', person_id=2, colour='Grey', make="Ford", model='Focus')
#
# cars = [car1, car2, car3]
# # car4 = Car(number_plate='BART21', person_id=3)
#
# db.session.add(testPerson1)
# db.session.add(testPerson2)
# # db.session.add(car1)
# # db.session.add(car2)
# # db.session.add(car3)
#
# db.session.add_all(cars)
# # db.session.add(car4)
# db.session.commit()

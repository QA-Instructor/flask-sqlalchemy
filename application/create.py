# This file should be run manually (directly) to pre-populate
# the database
# NOTE! The database MUST exist before we try to connect to it

from application import db
from application.models import Person, Car # Victoria's code
from application.models import Staff, Address, Customer, OrderStatus, Category, PlantType, Size, Product, Order
# add in UserLogin, OrderHistory

# these are the 11 tables we want to create, UserLogin, OrderHistory currently causing errors so not included
# Staff, Address, Customer,  OrderStatus, Category, Size, Product, Order add to import statement once created

# create our database schema
# db.create_all()

db.drop_all()
db.create_all()

# will need to use the db.session.add() code below to add the data - use lists as Victoria has below to make it easier?
# then need db.session.commit() to actually save it to the database
# once this code is populated, running it seperately should make everything appear in the database!

#staff table
staff1 = Staff(first_name='Natasha', last_name='Edun', email='natasha@plantemporium.com', password='staffaccess4')
staff2 = Staff(first_name='Jodie', last_name='Smith', email='jodie@plantemporium.com', password='staffaccess4')
staff3 = Staff(first_name='Jody', last_name='Broad', email='jody@plantemporium.com', password='staffaccess4')
staff4 = Staff(first_name='Isabel', last_name='Tulloch', email='isabel@plantemporium.com', password='staffaccess4')
staff = [staff1, staff2, staff3, staff4]

# address table
address1 = Address(address_line_one='AFC Richmond Club House', address_line_two='Nelson Road', address_line_three='London', postcode='TW9 4RP')
address2 = Address(address_line_one='49 Kings Road', address_line_two='Chelsea', address_line_three='London', postcode='SW3 5TT')
address3 = Address(address_line_one='4 Portland Terrace', address_line_two='The Green', address_line_three='Richmond', postcode='TW9 1QQ')
addresses = [address1, address2, address3]


# customer table
customer1 = Customer(first_name='Ted', last_name='Lasso', email='ted.lasso@afc_richmond.co.uk', address_id=1)
customer2 = Customer(first_name='Rebecca', last_name='Welton', email='rebecca_welton@gmail.com', address_id=1)
customer3 = Customer(first_name='Keeley', last_name='Jones', email='keeley_jones@gmail.com', address_id=2)
customer4 = Customer(first_name='Roy', last_name='Kent', email='roy.kent@afc_richmond.co.uk', address_id=3)
customer5 = Customer(first_name='Sam', last_name='Obisanya', email='sam.obisanya@afc_richmond.co.uk', address_id=1)
customers = [customer1, customer2, customer3, customer4, customer5]

# user login - currently commented out as table is also commented out on models.py
# user1 = UserLogin(username='tedlikesplants', password='1buyingaPLANT!')
# user2 = UserLogin(username='rebecca_w', password='Panda42')
# user3 = UserLogin(username='keeley.jones', password='passworDx4')
# user4 = UserLogin(username='roy.kent', password='Richmond12')
# user5 = UserLogin(username='sam_obisanya', password='FootballandPlants1')
# users = [user1, user2, user3, user4, user5]

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


#plant type table
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

# order
order1 = Order(product_id=10, quantity=2, status_id=1, staff_id=1)
order2 = Order(product_id=3, quantity=1, status_id=4, staff_id=2)
order3 = Order(product_id=4, quantity=4, status_id=3, staff_id=3)
order4 = Order(product_id=2, quantity=2, status_id=4, staff_id=4)
order5 = Order(product_id=1, quantity=1, status_id=4, staff_id=1)
plant_orders = [order1, order2, order3, order4, order5]

# order history
# order_history1 = OrderHistory(customer_id=1, order_id=1)
# order_history2 = OrderHistory(customer_id=2, order_id=2)
# order_history3 = OrderHistory(customer_id=3, order_id=3)
# order_history4 = OrderHistory(customer_id=4, order_id=4)
# order_history5 = OrderHistory(customer_id=5, order_id=5)
# order_history = [order_history1, order_history2, order_history3, order_history4, order_history5]

db.session.add_all(staff)
db.session.add_all(addresses)
db.session.add_all(customers)
# db.session.add_all(users)
db.session.add_all(status)
db.session.add_all(categories)
db.session.add_all(plant_types)
db.session.add_all(sizes)
db.session.add_all(products)
db.session.add_all(plant_orders)
# db.session.add_all(order_history)


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

from application import db  # import the sqlalchemy object (db) created for our app


# staff only links to orders in terms of who has responsibilty for packing them
class Staff(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)
# not sure if this line is correct in this instance
    email = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(30), nullable=False)
    orders = db.relationship('Order', backref='staff')


class Address(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    address_line_one = db.Column(db.String(50), nullable=False)
    address_line_two = db.Column(db.String(50), nullable=True)
    address_line_three = db.Column(db.String(50), nullable=True)
    address_line_four = db.Column(db.String(50), nullable=True)
    postcode = db.Column(db.String(50), nullable=False)
    # relationship between address and customer table - several people may have the same address
    address = db.relationship('Customer', backref='address')


class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    # address_id is the Foreign Key linking to the Address table
    address_id = db.Column(db.Integer, db.ForeignKey('address.id'), nullable=False)

# Currently causes an error so commented out, need to work out how we do this one
# class UserLogin(db.Model):
#     # this one is a FK so need to check how we do this, is it like this:
#     # id = db.Column(db.Integer, primary_key=False)
#     # or just this:
#     customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'), nullable=False)
#     Username = db.Column(db.String(50), nullable=False)
#     Password = db.Column(db.String(50), nullable=False)


class OrderStatus(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    status_description = db.Column(db.String(50), nullable=False)
    # not a field in the table, but OrderStatus table links back to Order
    order_status = db.relationship('Order', backref='order_status')


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category_description = db.Column(db.String(50), nullable=False)
    # not a field in the table, but Category table links back to Order
    category = db.relationship('Product', backref='category')


class PlantType(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    plant_type_description = db.Column(db.String(50), nullable=False)
    # not a field in the table, but Category table links back to Order
    plant_type = db.relationship('Product', backref='plant_type')


class Size(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    size_description = db.Column(db.String(50), nullable=False)
    # not a field in the table, but Size table links back to Order
    size = db.relationship('Product', backref='size')


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    species = db.Column(db.String(50), nullable=False)
    # is this the right data type to store number to 2 decimal places?
    price = db.Column(db.Integer, nullable=False)
    stock = db.Column(db.Integer, nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)
    plant_type_id = db.Column(db.Integer, db.ForeignKey('plant_type.id'), nullable=False)
    size_id = db.Column(db.Integer, db.ForeignKey('size.id'), nullable=False)
    # not a field in the table, but Order table links back to Product
    product = db.relationship('Order', backref='product')


class Order(db.Model):
    # this one may change as we are not sure on best method to record orders with more than one productID on them!
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    status_id = db.Column(db.Integer, db.ForeignKey('order_status.id'), nullable=False)
    staff_id = db.Column(db.Integer, db.ForeignKey('staff.id'), nullable=False)
# need to know how we do this one - with a stored proceedure to calculate? also what is best data type for price data?
    # total_cost = db.Column(db.Integer)

# Currently causes an error so commented out, need to work out how we do this one
# class OrderHistory(db.Model):
#     # a bridging table made up of 2 Foreign Keys, so should this just be:
#     customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'), nullable=False)
#     order_id = db.Column(db.Integer, db.ForeignKey('order.id'), nullable=False)


# Victoria's code:

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

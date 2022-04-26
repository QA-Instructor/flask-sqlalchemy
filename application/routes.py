from flask import render_template, request, flash, redirect, url_for, session
from application import app, db
from application.forms import EmailSignUpForm, CustomerRegistrationForm, StaffRegistrationForm, PlantForm, \
    NewBlogPostForm, LogInForm, SearchForm
from application.models import Person, Address, Newsletter, UserLogin, StaffInfo, Product, BlogPosts,\
    Category, PlantType, Size
from datetime import date


# newsletter sign up form for homepage
@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])

def email_signup_form():
    error = ""
    form = EmailSignUpForm()

    if request.method == 'POST':
        email = form.email.data
        if len(email) == 0:
            error = "Please supply email address"
        else:
            news = Newsletter(newsletter_email=email)
            db.session.add(news)
            db.session.commit()
            return 'Thank you!'
    return render_template('home.html', form=form, message=error, title='home')


# LINKS TO PLANT HTML PAGES

@app.route('/about', methods=['GET'])
def about():
    return render_template('about.html', title='About')


@app.route('/contact_us', methods=['GET'])
def contact():
    return render_template('contact_us.html', title='Contact Us')


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


# CUSTOMER RELATED ROUTES:

# REGISTERING A NEW CUSTOMER:


@app.route('/register', methods=['GET', 'POST'])
def register():
    error = ""
    form = CustomerRegistrationForm()

    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')

    if request.method == 'POST':
        username = form.username.data
        password = form.password.data
        first_name = form.first_name.data
        last_name = form.last_name.data
        email = form.email.data
        address_line_one = form.address_line_one.data
        address_line_two = form.address_line_two.data
        address_line_three = form.address_line_three.data
        postcode = form.postcode.data
        phone_number = form.phone_number.data

        if request.method == 'POST':
            username = form.username.data
            password = form.password.data
            first_name = form.first_name.data
            last_name = form.last_name.data
            email = form.email.data
            address_line_one = form.address_line_one.data
            address_line_two = form.address_line_two.data
            address_line_three = form.address_line_three.data
            postcode = form.postcode.data
            phone_number = form.phone_number.data

        if len(first_name) == 0 \
                or len(last_name) == 0 \
                or len(email) == 0\
                or len(address_line_one) == 0\
                or len(postcode) == 0\
                or len(password) < 4\
                or len(username) == 0:
            error = "Please complete each section of this form"
        else:
            user_login = UserLogin(username=username,
                                   password=password)
            address = Address(address_line_one=address_line_one,
                              address_line_two=address_line_two,
                              address_line_three=address_line_three,
                              postcode=postcode)
            person = Person(first_name=first_name,
                            last_name=last_name,
                            email=email,
                            address=address,
                            phone_number=phone_number,
                            person_type_id=2,
                            user_login=user_login)

            db.session.add(user_login)
            db.session.add(address)
            db.session.add(person)
            db.session.commit()
            return render_template('home.html', title='Home', message=error, form=form)
    return render_template('register.html', title='Register', message=error, form=form)


# ACCESSING A LIST OF CUSTOMERS
# This is functional


@app.route('/customer_list', methods=['GET'])
def show_customers():
    error = ""
    customer = Person.query.filter_by(person_type_id=2)
    # if len(customer) == 0:
    #     error = "There are no people to display"
    #     print(customer)
    return render_template('customer_list.html', customer=customer, message=error)


# STAFF RELATED ROUTES

# REGISTERING A NEW MEMBER OF STAFF:


@app.route('/register_staff', methods=['GET', 'POST'])
def register_staff():
    error = ""
    form = StaffRegistrationForm()

    if form.validate_on_submit():
        flash(f' Staff account created for {form.username.data}!', 'success')

    if request.method == 'POST':
        username = form.username.data
        password = form.password.data
        first_name = form.first_name.data
        last_name = form.last_name.data
        email = form.email.data
        address_line_one = form.address_line_one.data
        address_line_two = form.address_line_two.data
        address_line_three = form.address_line_three.data
        postcode = form.postcode.data
        phone_number = form.phone_number.data
        job_title = form.job_title.data
        date_of_birth = form.date_of_birth.data

        # if messages left in for all form routes because may need to raise error here for validations that aren't currently showing
        if len(first_name) == 0 \
                or len(last_name) == 0 \
                or len(email) == 0\
                or len(address_line_one) == 0\
                or len(postcode) == 0\
                or len(password) < 4\
                or len(username) == 0:
            error = "Please complete each section of this form"
        else:
            user_login = UserLogin(username=username,
                                   password=password)
            address = Address(address_line_one=address_line_one,
                              address_line_two=address_line_two,
                              address_line_three=address_line_three,
                              postcode=postcode)
            staff_info = StaffInfo(job_title=job_title,
                                   date_of_birth=date_of_birth)
            person = Person(first_name=first_name,
                            last_name=last_name,
                            email=email,
                            address=address,
                            phone_number=phone_number,
                            person_type_id=1,
                            user_login=user_login,
                            staff_info=staff_info)
            db.session.add(user_login)
            db.session.add(address)
            db.session.add(staff_info)
            db.session.add(person)
            db.session.commit()
            return render_template('home.html', title='Home', message=error, form=form)
    return render_template('register_staff.html', title='Register New Staff', message=error, form=form)


# ACCESSING A LIST OF CURRENT STAFF

@app.route('/staff_list', methods=['GET'])
def show_staff():
    error = ""
    staff = Person.query.filter_by(person_type_id=1)
    # if len(customer) == 0:
    #     error = "There are no people to display"
    #     print(customer)
    return render_template('staff_list.html', staff=staff, message=error)


# DELETE STAFF ACCOUNTS - currently provides error message 'method not allowed'
# @app.route('/staff/<int:staff_id>', methods=['DELETE'])
# def delete_staff(staff_id):
#     error = ""
#     staff = Staff.query.get(staff_id)
#     db.session.delete(staff)
#     db.session.commit()
#     staff = Staff.query.all()
#     if not staff:
#         error = "There is no staff with ID: " + str(staff_id)
#         print(staff)
#     return render_template('staff_deletion.html', staff=staff, message=error, title="Delete Staff")

# REGISTERING A NEW PLANT:


@app.route('/plant_form', methods=['GET', 'POST'])
def plant_form():
    error = ""
    form = PlantForm()

    if form.validate_on_submit():
        flash(f' Plant added!', 'success')

    if request.method == 'POST':
        # plant_name = form.plant_name.data
        plant_category = form.plant_category.data
        plant_species = form.plant_species.data
        plant_price = form.plant_price.data
        plant_stock = form.plant_stock.data
        plant_type = form.plant_type.data
        plant_size = form.plant_size.data

        if len(plant_category) == 0 \
                or plant_species == 0\
                or plant_price == 0\
                or plant_stock == 0:
            error = "Please complete the fields"
        else:
            product = Product(species=plant_species,
                              price=plant_price,
                              stock=plant_stock,
                              category_id=plant_category,
                              plant_type_id=plant_type,
                              size_id=plant_size)
            db.session.add(product)
            db.session.commit()
            return render_template('plant_form.html', title='Register a Plant', message=error, form=form)
    return render_template('plant_form.html', title='Register a Plant', message=error, form=form)

# ACCESSING A LIST OF PLANTS:
# to do
# DELETING PLANTS WE NO LONGER STOCK:
# to do



@app.route('/plant_care', methods=['GET'])
def plant_care():
    posts = BlogPosts.query.order_by(BlogPosts.date_posted.desc()).all()
    return render_template('plant_care.html', title='Plant Care', posts=posts)

@app.route('/addpost', methods=['GET', 'POST'])
def addpost():
    error = ""
    form = NewBlogPostForm()

    if form.validate_on_submit():
        flash(f' New Blog Post created called {form.title.data}!', 'success')

    if request.method == 'POST':
        title = form.title.data
        author = form.author.data
        post_content = form.post_content.data
        if len(title) == 0\
                or len(author) == 0\
                or len(post_content) == 0:
            error = "Please complete the fields"
        else:
            post = BlogPosts(title=title, author=author, post_content=post_content, date_posted=date.today())
            db.session.add(post)
            db.session.commit()
            posts = BlogPosts.query.order_by(BlogPosts.date_posted.desc()).all()
            return render_template('plant_care.html', title='Plant Care', posts=posts)

    return render_template('addpost.html', message= error, form=form)

@app.route('/post/<int:post_id>')
def post(post_id):
    post = BlogPosts.query.filter_by(id=post_id).one()

    return render_template('post.html', post=post)

# session variables

@app.route('/login', methods=['GET', 'POST'])
@app.route('/log_in', methods=['GET', 'POST'])
def login():
    form = LogInForm()
    error = ""
    # login_redirect = url_for('login')
    if request.method == 'POST':
        # pop previous session in case someone was already logged in
        session.pop('logged_in_username', default=None)

        # if form.validate_on_submit():

        # # taking the username and password from the form so we can compare to the db
        form_username = request.form['username']
        form_password = request.form['password']

        # need to do the validation here to check if username and password match the database

        # this is looking for a record on the database where both the username and password match

        db_username_password = UserLogin.query.filter_by(username=form_username, password=form_password).all()

        # user_and_persontype = db.session.query(UserLogin, Person, StaffInfo).select_from(UserLogin).join(Person).join(StaffInfo).all()
        # print(user_and_persontype)
        # setting initial value of pw_check to false:
        pw_check = False

        if db_username_password != []:
            pw_check = True
        else:
            pw_check = False

        if pw_check == True:
        # if validation has passed, save the username to the session object
            session['logged_in_username'] = request.form['username']
            session['logged_in'] = True

        # also need to check if they are a customer or staff, so need a second session variable
        # some sort of if statement needed here to check db and then:
        # not currently checking db, but will take the form input instead as a starting point:
            if request.form['type'] == '1':
                # if person_type = 1 then:
                session['typesession'] = 'staff'
            else:
                session['typesession'] = 'customer'

            # will then need to return different nav/functionality depending on which type of log in it is

            # will show shop page plus session variable specific text
                return redirect(url_for('shop'))

        else:
            flash(f' Login failed, please try again', 'danger')
            # will just show basic shop page, no session data
            return redirect(url_for('shop'))
        # will display welcome message/session data and also navigation will change
        return redirect(url_for('shop'))

    #     if validation fails, return to log in page and flash message that it has failed
    #     return redirect(url_for('login'))

    return render_template('login.html', message= error, form=form)


@app.route('/log_out')
@app.route('/logout')
def delete_session():
    error = ""
    form = EmailSignUpForm()
    # Clear the username stored in the session object
    session.pop('logged_in_username', default=None)
    session.pop('typesession', default=None)
    session.pop('logged_in', default=None)

    flash(f' You have logged out!', 'success')
    return render_template('home.html', title='Home', form=form, message=error,)


# Pass Stuff to Nav
@app.context_processor
def layout():
    form = SearchForm()
    return dict(form=form)


# create search function
@app.route('/search', methods=["POST"])
def search():
    form = SearchForm()
    posts = BlogPosts.query
    if form.validate_on_submit():

        # get data from submitted form
        post.searched = form.searched.data
        # Query the database
        posts = posts.filter(BlogPosts.post_content.like('%' + post.searched + '%'))
        posts = posts.order_by(BlogPosts.title).all()

        return render_template("search.html", form=form, searched=post.searched, posts=posts)



# Victoria's code
# def register_basic_form():
#     error = ""
#     form = BasicForm()
#
#     if request.method == 'POST':
#         first_name = form.first_name.data
#         last_name = form.last_name.data
#
#         if len(first_name) == 0 or len(last_name) == 0:
#             error = "Please supply both first and last name"
#         else:
#             person = Person(first_name=first_name, last_name=last_name)
#             db.session.add(person)
#             db.session.commit()
#             return 'Thank you!'
#     return render_template('home.html', form=form, message=error, title='home')

# @app.route('/cars', methods=['GET'])
# def show_cars():
#     error = ""
#     cars = Car.query.all()
#     if len(cars) == 0:
#         error = "There are no cars to display"
#         print(cars)
#     return render_template('cars.html', cars=cars, message=error, title="Car")

# @app.route('/people', methods=['GET'])
# def show_people():
#     error = ""
#     people = Person.query.all()
#     if len(people) == 0:
#         error = "There are no people to display"
#         print(people)
#     return render_template('people.html', people=people, message=error)
#
#
# @app.route('/people/<int:person_id>', methods=['GET'])
# def show_person(person_id):
#     error = ""
#     # use filter_by for any column
#     # person = Person.query.filter_by(id=person_id).first()
#     #  use get for the PK
#     person = Person.query.get(person_id)
#
#     # simpsons = Person.query.filter_by(last_name="simpson").all()
#
#     # to sort
#     # simpsons = Person.query.filter_by(last_name="simpson").order_by(Person.first_name).all()
#     # descending sort
#     # simpsons = Person.query.filter_by(last_name="simpson").order_by(Person.first_name.desc()).all()
#     # limit to top 2 simpsons
#     simpsons = Person.query.filter_by(last_name="simpson").order_by(Person.first_name).limit(2).all()
#     if not person:
#         error = "There is no person with ID: " + str(person_id)
#         print(person)
#     return render_template('person.html', person=person, message=error, title="Person", family=simpsons)
#
#
# @app.route('/people/<int:person_id>', methods=['PUT'])
# def update_person(person_id):
#     error = ""
#     person = Person.query.get(person_id)
#     person.last_name = "Flanders"
#     db.session.commit()
#     if not person:
#         error = "There is no person with ID: " + str(person_id)
#         print(person)
#     return render_template('person.html', person=person, message=error, title="Person", family=[])
#
#
# @app.route('/people/<int:person_id>/<string:new_last_name>', methods=['PUT'])
# def update_person_with_name(person_id, new_last_name):
#     error = ""
#     person = Person.query.get(person_id)
#     person.last_name = new_last_name
#     db.session.commit()
#     if not person:
#         error = "There is no person with ID: " + str(person_id)
#         print(person)
#     return render_template('person.html', person=person, message=error, title="Updated Person", family=[])
#
#
# @app.route('/people/<int:person_id>', methods=['DELETE'])
# def delete_person(person_id):
#     error = ""
#     person = Person.query.get(person_id)
#     db.session.delete(person)
#     db.session.commit()
#     people = Person.query.all()
#     if not person:
#         error = "There is no person with ID: " + str(person_id)
#         # print(person)
#     return render_template('people.html', people=people, message=error, title="People")
#
#
# @app.route('/personandcars/<int:person_id>', methods=['GET'])
# def people_and_cars(person_id):
#     error = ""
#     person = Person.query.get(person_id)
#     # cars= person.cars
#     if not person:
#         error = "There is no person with ID: " + str(person_id)
#         print(person)
#         # print(person_and_carinfo)
#     return render_template('person_and_cars.html', person=person, message=error, title="Person and Car Info")
#
#     # return render_template('home.html', form=form, message=error)
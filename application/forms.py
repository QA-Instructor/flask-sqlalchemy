from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField, SelectMultipleField, DateField, IntegerField


# from wtforms.validators import DataRequired, Length, Email, EqualTo

# need form to do email newsletter sign up

class EmailSignUpForm(FlaskForm):
    email = StringField('Email')
    submit = SubmitField('Sign Up')

# new form needs to link to userlogin person and address tables for registering customers (is set in the route to set the
# persontype to '2' which is customer
class CustomerRegistrationForm(FlaskForm):
    # userlogin elements
    username = StringField('Username')
    password = PasswordField('Password')

    # person elements
    first_name = StringField('First Name')
    last_name = StringField('Last Name')
    email = StringField('Email')

    # address elements
    address_line_one = StringField('Address Line 1')
    address_line_two = StringField('Address Line 2')
    address_line_three = StringField('Address Line 3')
    postcode = StringField('Postcode')
    phone_number = StringField('Phone Number')
    # submit
    submit = SubmitField('Sign Up')

# added here: first name, last name
# commented out: username, needs to be added in create.py
# class RegistrationForm(FlaskForm):
#     first_name = StringField('First Name')
#     last_name = StringField('Last Name')
#     # username = StringField('Username')
#     email = StringField('Email')
#     # password = PasswordField('Password')
#     submit = SubmitField('Sign Up')
#     # address elements
#     address_line_one = StringField('Address Line 1')
#     address_line_two = StringField('Address Line 2')
#     address_line_three = StringField('Address Line 3')
#     postcode = StringField('Postcode')


class LoginForm(FlaskForm):
    email = StringField('Email')
    password = PasswordField('Password')
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')


# as staff are now a type of person, this form gets a bit more complicated, needs to link to userlogin, address,
# person and staff info tables to be functional (can set persontype to '1' which is staff in the routes)
class StaffRegistrationForm(FlaskForm):
    # userlogin elements
    username = StringField('Username')
    password = PasswordField('Password')

    # person elements
    first_name = StringField('First Name')
    last_name = StringField('Last Name')
    email = StringField('Email')

    # address elements
    address_line_one = StringField('Address Line 1')
    address_line_two = StringField('Address Line 2')
    address_line_three = StringField('Address Line 3')
    postcode = StringField('Postcode')
    phone_number = StringField('Phone Number')

    # staff info elements
    job_title = StringField('Job title')
    date_of_birth = DateField('Date of birth')
    # submit
    submit = SubmitField('Register New Staff Member')


# class StaffForm(FlaskForm):
#     first_name = StringField('First Name')
#     last_name = StringField('Last Name')
#     email = StringField('Email')
#     password = PasswordField('Password')
#     remember = BooleanField('Remember Me')
#     submit = SubmitField('Login')


class PlantForm(FlaskForm):
    plant_name = StringField('Plant Name')
    plant_type = SelectMultipleField('Type', choices=['Cacti/Succulent', 'Hanging', 'Flowering', 'Palms', 'Ferns'])
    plant_category = SelectMultipleField('Categories', choices=['Indoor', 'Outdoor'])
    plant_species = StringField('Plant Species')
    plant_price = IntegerField('Plant Price')
    plant_stock = IntegerField('Number in Stock')
    plant_size = SelectMultipleField('Size', choices=['Tiny', 'Small', 'Medium', 'Tall'])
    submit = SubmitField('Register Plant')



#wanted to try add in wft validators but kept throwing up error, will do a basic form for now to just get it running then will try and add validators after
# # class RegistrationForm(FlaskForm):
# #     username = StringField('Username', validators=[DataRequired(), Length(min=2, max=30)])
# #     email = StringField('Email', validators=[DataRequired(), Email])
# #     password = PasswordField('Password', validators=[DataRequired(), Length(min=4)])
# #     confirm_password = PasswordField('Password', validators=[DataRequired(), Length(min=4), EqualTo('password')])
# #     submit = SubmitField('Sign Up')
#
#
# class LoginForm(FlaskForm):
#     email = StringField('Email', validators=[DataRequired(), Email])
#     password = PasswordField('Password', validators=[DataRequired()])
#     remember = BooleanField('Remember Me')
#     submit = SubmitField('Login')
#
#
# class StaffForm(FlaskForm):
#     email = StringField('Email', validators=[DataRequired(), Email])
#     password = PasswordField('Password', validators=[DataRequired()])
#     remember = BooleanField('Remember Me')
#     submit = SubmitField('Login')
#
#
# class PlantForm(FlaskForm):
#     plant_name = StringField('Plant', validators=[DataRequired()])
#     plant_category = SelectMultipleField('Categories', validators=[DataRequired()], choices=['Cacti/Succulent', 'Hanging', 'Flowering', 'Palms', 'Ferns'])
#     submit = SubmitField('Register Plant')




# Victoria's code
class BasicForm(FlaskForm):
    first_name = StringField('First Name')
    last_name = StringField('Last Name')
    submit = SubmitField('Add Name')

# additions below here:
class NewBlogPostForm(FlaskForm):
    title = StringField('Title')
    author = StringField('Author')
    post_content = StringField('Post Content')

    submit = SubmitField('Add post')

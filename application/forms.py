from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField, SelectMultipleField
# from wtforms.validators import DataRequired, Length, Email, EqualTo


class RegistrationForm(FlaskForm):
    username = StringField('Username')
    email = StringField('Email')
    password = PasswordField('Password')
    submit = SubmitField('Sign Up')


class LoginForm(FlaskForm):
    email = StringField('Email')
    password = PasswordField('Password')
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')


class StaffForm(FlaskForm):
    email = StringField('Email')
    password = PasswordField('Password')
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')


# class PlantForm(FlaskForm):
#     plant_name = StringField('Plant')
#     plant_category = SelectMultipleField('Categories', choices=['Cacti/Succulent', 'Hanging', 'Flowering', 'Palms', 'Ferns'])
#     submit = SubmitField('Register Plant')



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



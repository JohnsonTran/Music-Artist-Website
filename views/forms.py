from flask_wtf import FlaskForm
from wtforms import Form, StringField, PasswordField, BooleanField, validators

# Flask forms for the login and register pages
class LoginForm(FlaskForm):
    email = StringField('Email Address', [validators.DataRequired()])
    password = PasswordField('Password', [validators.DataRequired(), validators.EqualTo('confirm', message='Passwords must match')])
    remember = BooleanField('Remember me')

class RegisterForm(FlaskForm):
    name = StringField('Name', [validators.DataRequired()])
    email = StringField('Email Address', [validators.DataRequired()])
    password = PasswordField('New Password', [validators.DataRequired(), validators.EqualTo('confirm', message='Passwords must match')])
    confirm = PasswordField('Repeat Password')

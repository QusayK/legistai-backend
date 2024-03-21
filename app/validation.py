from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, validators

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[validators.Email(), validators.DataRequired()])
    password = PasswordField('Password', validators=[validators.Length(min=6), validators.DataRequired()])
from flask_wtf import FlaskForm
from wtforms import (StringField, PasswordField, SubmitField)
from wtforms.validators  import input_required, length, ValidationError, email
from Project.model import Gebruikers

class RegisterForm(FlaskForm):
    Email = StringField(validators=[input_required(), email()], render_kw={"placeholder":"Email"})
    Wachtwoord = PasswordField(validators=[input_required()], render_kw={"placeholder":"Wachtwoord"})
    Naam = StringField(validators=[input_required()], render_kw={"placeholder":"Naam"})
    submit = SubmitField("Register")

#    def validate_email(self, email):
#        if Users.query.filter_by(email=field.data).first():
#            raise ValidationError("Email staat al gerigsteerd")

class LoginForm(FlaskForm):
    Email = StringField(validators=[input_required(), email()], render_kw={"placeholder":"Email"})
    Wachtwoord = PasswordField(validators=[input_required()], render_kw={"placeholder":"Wachtwoord"})
    submit = SubmitField("Login")

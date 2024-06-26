from flask_wtf import FlaskForm
from wtforms import (StringField, PasswordField, SubmitField, IntegerField)
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

class AddFilmForm(FlaskForm):
    Titel = StringField(validators=[input_required()], render_kw={"placeholder":"Titel"})
    RegID = StringField(validators=[input_required()])
    Jaar = IntegerField(validators=[input_required()], render_kw={"placeholder":"Jaar"})
    Leuk = StringField(render_kw={"placeholder":"Iets leuks"})
    submit = SubmitField("Voeg toe")

class DeleteFilmForm(FlaskForm):
    ID = StringField(validators=[input_required()], render_kw={"placeholder":"Titel"})
    submit = SubmitField("Verwijder Film")

class AddRegForm(FlaskForm):
    Naam = StringField(validators=[input_required()], render_kw={"placeholder":"Naam"})
    submit = SubmitField("Voeg toe")

class DeleteRegForm(FlaskForm):
    ID = StringField(validators=[input_required()], render_kw={"placeholder":"Voornaam"})
    submit = SubmitField("Verwijder Film")
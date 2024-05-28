from Project import app, db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


class Gebruikers(db.Model, UserMixin):
    __tablename__ = 'Gebruikers'
    ID = db.Column(db.Integer,primary_key=True)
    Email = db.Column(db.String(50),nullable=False, unique=True)
    Wachtwoord = db.Column(db.String(255),nullable=False)
    Naam = db.Column(db.String(50),nullable=False)

    def __init__(self,Email,Wachtwoord,Naam):
        self.Email=Email
        self.Wachtwoord= generate_password_hash(Wachtwoord)
        self.Naam=Naam

    def check_Wachtwoord(self, Wachtwoord):
        return check_password_hash(self.Wachtwoord, Wachtwoord)
    
    def get_id(self):
           return (self.ID)

class Acteur(db.Model):
    __tablename__ = 'Acteur'
    ID = db.Column(db.Integer,primary_key=True)
    Voornaam = db.Column(db.String(50),nullable=False)
    Achternaam = db.Column(db.String(50))

    def __init__(self,Voornaam,Achternaam):
        self.Voornaam=Voornaam
        self.Achternaam=Achternaam

class Regisseur(db.Model):
    __tablename__ = 'Regisseur'
    ID = db.Column(db.Integer,primary_key=True)
    Voornaam = db.Column(db.String(50),nullable=False)
    Achternaam = db.Column(db.String(50))
    Films = db.relationship('Film', backref='regisseur')

    def __init__(self,Voornaam,Achternaam):
        self.Voornaam=Voornaam
        self.Achternaam=Achternaam

class Film(db.Model):
    __tablename__ = 'Film'
    ID = db.Column(db.Integer,primary_key=True)
    Titel = db.Column(db.String(255),nullable=False, unique=True)
    RegID = db.Column(db.Integer, db.ForeignKey('Regisseur.ID'))
    Jaar = db.Column(db.Integer,nullable=False)
    Leuk = db.Column(db.String(255),nullable=True)

    def __init__(self,Titel,RegID,Jaar,Leuk):
        self.Titel=Titel
        self.RegID=RegID
        self.Jaar=Jaar
        self.Leuk=Leuk

class Rol(db.Model):
    __tablename__ = 'Rol'
    ID = db.Column(db.Integer,primary_key=True)
    ActID = db.Column(db.Integer,nullable=False)
    FilmID = db.Column(db.Integer,nullable=False)
    Personage = db.Column(db.String(50),nullable=False)

    def __init__(self,ActID,FilmID,Personage):
        self.ActID=ActID
        self.FilmID=FilmID
        self.Personage=Personage





from Project import app, db


class Users(db.Model):
    __tablename__ = 'Gebruikers'
    ID = db.Column(db.Integer,primary_key=True)
    Email = db.Column(db.String(50),nullable=False)
    Wachtwoord = db.Column(db.String(50),nullable=False)
    Naam = db.Column(db.String(50),nullable=False)

    def __init__(self,Email,Wachtwoord,Naam):
        self.Email=Email
        self.Wachtwoord=Wachtwoord
        self.Naam=Naam

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

    def __init__(self,Voornaam,Achternaam):
        self.Voornaam=Voornaam
        self.Achternaam=Achternaam

class Film(db.Model):
    __tablename__ = 'Film'
    ID = db.Column(db.Integer,primary_key=True)
    Titel = db.Column(db.String(255),nullable=False)
    RegID = db.Column(db.Integer)
    Jaar = db.Column(db.Integer,nullable=False)

    def __init__(self,Titel,RegID,Jaar):
        self.Titel=Titel
        self.RegID=RegID
        self.Jaar=Jaar

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





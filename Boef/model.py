from Boef import db

class Users(db.Model):
    __tablename__ = 'Gebruikers'
    ID = db.Column(db.Integer,primary_key=True)
    Email = db.Column(db.String(50))
    Wachtwoord = db.Column(db.String(50))
    Naam = db.Column(db.String(50))

    def __init__(self,Email,Wachtwoord,Naam):
        self.Email=Email
        self.Wachtwoord=Wachtwoord
        self.Naam=Naam


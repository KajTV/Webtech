from Project import app, db
from flask import Flask
from Project.model import *




def create_app():

    Regisseur1 = Regisseur('Kaj ter Velde')
    Regisseur2 = Regisseur('Sufjan Ismaili')
    Regisseur3 = Regisseur('Niels Faber')
    with app.app_context():
        db.create_all()
        db.session.commit()
        Seeddb()

    return app

def Seeddb():

    Regisseur1 = Regisseur('Kaj ter Velde')
    Regisseur2 = Regisseur('Sufjan Ismaili')
    Regisseur3 = Regisseur('Steven Spielberg')
    Regisseur4 = Regisseur('Quentin Tarantino')
    Regisseur5 = Regisseur('Alfred Hitchcock')
    Regisseur6 = Regisseur('Stanley Kubrick')
    Regisseur7 = Regisseur('Martin Scorsese')
    Regisseur8 = Regisseur('Cristopher Nolan')
    Movie1 = Film('Pulp Fiction',4,1994,'I want to dance')
    Movie2 = Film('Jurrasic Park',3,1993,'Wanneer de trex ontsnapt')
    Movie3 = Film('Vertigo',5,1958,' ')
    Movie4 = Film('The shining',6,1980,'Heres johhny')
    Movie5 = Film('The wolf of wall street',7,2013,'Waneer ze coke snuiven')
    Movie6 = Film('Oppenheimer',8,2024,'Wanneer de bom ontploft')

    with app.app_context():
        db.session.add_all([Regisseur1, Regisseur2,Regisseur3,Regisseur4,Regisseur5,Regisseur6,Regisseur7,Regisseur8,Movie1,Movie2,Movie3,Movie4,Movie5,Movie6])
        db.session.commit()

    return app

create_app()
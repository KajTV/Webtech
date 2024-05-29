from Project import app, db
from flask import Flask
from Project.model import *




def create_app():

    Regisseur1 = Regisseur('Kaj ter Velde')
    Regisseur2 = Regisseur('Sufjan Ismaili')
    Regisseur3 = Regisseur('Niels Faber')
    with app.app_context():
        db.create_all()
        db.session.add_all([Regisseur1, Regisseur2,Regisseur3])
        db.session.commit()

    return app

create_app()
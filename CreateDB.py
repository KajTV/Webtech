from Project import app, db
from flask import Flask
from Project.model import *




def create_app():

    Regisseur1 = Regisseur('Kaj','de pro')
    with app.app_context():
        db.create_all()
        db.session.add_all([Regisseur1])
        db.session.commit()

    return app

create_app()
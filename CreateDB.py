from Project import app, db
from flask import Flask
from Project.model import *




def create_app():

    Regisseur1 = Regisseur('Kaj','de pro')
    AccDefault = Gebruikers('Kajtervelde@gmail.com','KajTV','KajTV')
    Film1 = Film('Peppa Big', 1, 1939, '')
    with app.app_context():
        db.create_all()
        db.session.add_all([Regisseur1, AccDefault, Film1])
        db.session.commit()

    return app

create_app()
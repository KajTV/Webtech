from Project import app, db
from flask import Flask




def create_app():

    import Project.model

    with app.app_context():
        db.create_all()

    return app

create_app()
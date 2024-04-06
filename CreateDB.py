from Boef import app, db
from Boef.model import *

Admin = Users('Admin@gmail.com', 'Test', 'Admin')

with app.app_context():
    db.create_all
    db.session.add_all([Admin])
    db.session.commit()



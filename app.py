from flask import Flask, redirect, render_template, url_for, session, request
from flask_login import login_user, login_required, logout_user, current_user, LoginManager
from Project.forms import RegisterForm, LoginForm
from Project.model import *
from Project import app, db, login_manager

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "Login"

@login_manager.user_loader 
def load_user(user): 
    return Gebruikers.query.get(int(user))

@app.route("/", methods=['GET', 'POST'])
def index():
    return render_template('Home.html')

@app.route("/Login", methods=['GET', 'POST'])
def Login():
    form = LoginForm()
    if form.validate_on_submit():
        print("scoop")
        user = Gebruikers.query.filter_by(Email=form.Email.data).first()

        if user:
            if check_password_hash(user.Wachtwoord, form.Wachtwoord.data):
                login_user(user)
                return redirect(url_for('Lijst'))

    return render_template('Login.html', form=form)

@app.route("/Register", methods=['GET', 'POST'])
def Register():
    form = RegisterForm()
    if request.method == 'POST':
        if form.submit():
            user = Gebruikers(form.Email.data,form.Wachtwoord.data,form.Naam.data)
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('Login'))
    return render_template('Register.html', form=form)

@app.route("/Lijst", methods=['GET', 'POST'])
@login_required
def Lijst():
    Films = Film.query.order_by('ID')
    return render_template('Lijst.html', Films=Films)

if __name__ == "__main__":
    app.run(debug=True)
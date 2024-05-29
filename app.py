from flask import Flask, flash, redirect, render_template, url_for, session, request
from flask_login import login_user, login_required, logout_user, current_user, LoginManager
from Project.forms import RegisterForm, LoginForm, AddFilmForm, DeleteFilmForm, AddRegForm, DeleteRegForm
from Project.model import *
from Project import app, db, login_manager
import re

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "Login"

@login_manager.user_loader 
def load_user(user): 
    return Gebruikers.query.get(int(user))

@app.route("/", methods=['GET', 'POST'])
@login_required
def index():
    return redirect(url_for('Login'))

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
    Films = Film.query.all()
    Regisseurs = Regisseur.query.all()
    return render_template('Lijst.html', Films=Films, Regisseurs=Regisseurs)

@app.route('/AddFilm', methods=['GET', 'POST'])
@login_required
def AddFilm():
    form = AddFilmForm()
    if request.method == 'POST':
        if form.submit():
            reg = Regisseur.query.filter_by(Naam = form.RegID.data).first()
            print(reg.ID)
            newFilm = Film(form.Titel.data,reg.ID,form.Jaar.data,form.Leuk.data)
            db.session.add(newFilm)
            db.session.commit()
            return redirect(url_for('Lijst'))
    return render_template('AddFilm.html', form=form)

@app.route('/DeleteFilm', methods=['GET', 'POST'])
@login_required
def DeleteFilm():
    form = DeleteFilmForm()
    try:
        if request.method == 'POST':
            if form.submit():
                Skkrt = form.ID.data
                dol = Film.query.filter_by(Titel = Skkrt).first()
                db.session.delete(dol)
                db.session.commit()
                return redirect(url_for('Lijst'))
    except:
        flash("Film bestaat niet")
    return render_template('DeleteFilm.html', form=form)

@app.route('/DeleteReg', methods=['GET', 'POST'])
@login_required
def DeleteReg():
    form = DeleteRegForm()
    if request.method == 'POST':
        try:
            if form.submit():
                Skkrt = form.ID.data
                print(Skkrt)
                dol = Regisseur.query.filter_by(Naam = Skkrt).first()
                db.session.delete(dol)
                db.session.commit()
                return redirect(url_for('Lijst'))
        except:
            flash("Regisseur bestaat niet")
    return render_template('DeleteReg.html', form=form)

@app.route('/AddReg', methods=['GET', 'POST'])
@login_required
def AddReg():
    form = AddRegForm()
    if request.method == 'POST':
        if form.submit():
            newReg = Regisseur(form.Naam.data)
            db.session.add(newReg)
            db.session.commit()
            return redirect(url_for('Lijst'))
    return render_template('AddReg.html', form=form)

@app.route('/Logout')
@login_required
def Logout():
    logout_user()
    return redirect(url_for('Login'))



if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask, render_template, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField


app = Flask(__name__)
app.config['SECRET_KEY'] = 'binkyboef'

@app.route("/")
def index():
    return render_template('Home.html')

@app.route("/Login")
def Login():
    return render_template('Login.html')

@app.route("/Register")
def Register():
    return render_template('Register.html')

if __name__ == "__main__":
    app.run(debug=True)
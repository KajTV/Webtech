from Boef import app, db
from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField



@app.route("/")
def index():
    # render de template Basic.html
    return "<h1>Welkom bij muziekschool Session</h1>"

if __name__ == "__main__":
    app.run()
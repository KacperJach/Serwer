from flask import render_template, flash, redirect, url_for
from app import app, db
from app.forms import LoginForm
from flask_login import current_user, login_user, logout_user
from app.models import User
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
from flask_sqlalchemy import get_debug_queries

@app.route('/')
@app.route('/index')
def index():
    user = {'username' : 'Admin'}
    return render_template('index.html', title="Strona Glowna", user=user)
@app.route('/login', methods = ['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(card_id=form.username.data).first()
        if form.username.data == '100' and form.password.data == 'efekt':
            login_user(user, remember=form.remember_me.data)
            return redirect(url_for('index'))
        else:
            flash('Invalid username or password')
            return redirect(url_for('login'))

    return render_template('login.html', title='Sign in', form=form)
@app.route('/database')
def database():
    if not current_user.is_authenticated:
        return redirect(url_for('login'))
    data = User.query.all()
    return render_template('database.html', title='Database', data=data)
@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

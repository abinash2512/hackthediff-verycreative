from flask import Blueprint, render_template, redirect, url_for, request
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from .models import User

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return render_template('login.html')

@auth.route('/signup')
def signup():
    return render_template('signup.html')

@auth.route('/signup', methods=['POST'])
def signup_post():
    # code to validate and add user to database goes here
    email = request.form.get('email')
    name = request.form.get('name')
    password = request.form.get('password')
    
    user = User.query.filter_by(email=email).first()
    if user:
        return redirect(url_for('auth.signup'))
    
    new_user = User(email=email, name=name, password=generate_password_hash(password, method='sha256'))
    
    db.session.add(new_user)
    db.session.commit()
    return redirect(url_for('auth.login'))

@auth.route('/logout')
def logout():
    return 'Logout'
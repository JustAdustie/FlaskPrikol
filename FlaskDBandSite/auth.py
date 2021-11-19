from flask import Blueprint, render_template, redirect, url_for, request, flash
from werkzeug.security import generate_password_hash, check_password_hash
from models import User
from flask_login import login_user, logout_user, login_required, current_user
from __init__ import db


auth = Blueprint('auth', __name__) 


@auth.route('/', methods=['GET', 'POST'])
def login():
    if request.method=='GET': 
        return render_template('index.html')
    else:
        login = request.form.get('login')
        password = request.form.get('password')
        user = User.query.filter_by(login=login).first()
       
        if not user:
            return redirect(url_for('auth.login'))
        elif not check_password_hash(user.password, password):
            return redirect(url_for('auth.login'))
        if user.priority == 1:
            login_user(user)
            return redirect(url_for('main.admin'))
        elif user.priority == 2:
            login_user(user)
            return redirect(url_for('main.guard'))
        

@auth.route('/logout', methods = ['POST'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))
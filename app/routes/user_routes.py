#!/usr/bin/python3


from flask import render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required, current_user
from app import db
from app.models.user import User
from werkzeug.security import generate_password_hash, check_password_hash

def register(blueprint):
    @blueprint.route('/register', methods=['GET', 'POST'])
    def register_user():
        if current_user.is_authenticated:
            return redirect(url_for('main.profile'))
        
        if request.method == 'POST':
            username = request.form.get('username')
            email = request.form.get('email')
            password = request.form.get('password')
            confirm_password = request.form.get('confirm_password')
            
            if password != confirm_password:
                flash('Passwords do not match!', 'danger')
                return redirect(url_for('main.register_user'))
            
            existing_user = User.query.filter_by(username=username).first() or User.query.filter_by(email=email).first()
            if existing_user:
                flash('Username or Email already exists.', 'danger')
                return redirect(url_for('main.register_user'))
            
            hashed_password = generate_password_hash(password, method='sha256')
            new_user = User(username=username, email=email, password_hash=hashed_password)
            db.session.add(new_user)
            db.session.commit()
            
            flash('Registration successful! You can now log in.', 'success')
            return redirect(url_for('main.login_user'))
        
        return render_template('register.html')

    @blueprint.route('/login', methods=['GET', 'POST'])
    def login_user():
        if current_user.is_authenticated:
            return redirect(url_for('main.profile'))
        
        if request.method == 'POST':
            email = request.form.get('email')
            password = request.form.get('password')
            user = User.query.filter_by(email=email).first()
            
            if user and check_password_hash(user.password_hash, password):
                login_user(user)
                flash('Login successful!', 'success')
                return redirect(url_for('main.profile'))
            else:
                flash('Login failed. Check your email and password.', 'danger')
        
        return render_template('login.html')

    @blueprint.route('/logout')
    @login_required
    def logout_user():
        logout_user()
        flash('You have been logged out.', 'info')
        return redirect(url_for('main.login_user'))

    @blueprint.route('/profile')
    @login_required
    def profile():
        return render_template('profile.html', user=current_user)

#!/usr/bin/python3

from flask import render_template
user_bp = Blueprint('user_bp', __name__)

@user_bp.route('/')
def index():
    return render_remplate('index.html')

@user_bp.route('/login')
def login():
    return render_template('login.html')

@user_bp.route('/register')
def register():
    return render_template('register.html')

@user_bp.route('/chat')
def chat():
    return render_template('chat.html')

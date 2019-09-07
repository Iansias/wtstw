from flask import render_template, flash, redirect, url_for
from app import app
import requests
from app.form import LoginForm, RegistrationForm, EditProfileForm, contactus
from flask_login import current_user, login_user
from app.models import User, tickets_db
from flask_login import logout_user
from flask_login import login_required
from flask import request
from werkzeug.urls import url_parse
from app import db
from datetime import datetime




@app.route('/')
@app.route('/index')
def index():
    #with APi should be quick

    return render_template('index.html', title='Home')

from flask import Flask, request, render_template, session, redirect, url_for
from flask_bcrypt import Bcrypt
import jwt
from flask_login import LoginManager, login_user, current_user, login_required, UserMixin, logout_user
from flask import flash
from models import db, User, Auction, Bid
from datetime import datetime
import secrets
from flask_session import Session
from functools import wraps

secret_key = secrets.token_hex(32)

secret_key = secrets.token_hex(32)

app = Flask(__name__)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)

app.config['SECRET_KEY'] = secret_key
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///auction.db'

app.config['SECRET_KEY'] = secret_key
app.config['SESSION_TYPE'] = 'filesystem'  # You can use other session types as well
app.config['SESSION_USE_SIGNER'] = True   # To sign session cookies for added security
app.config['SESSION_KEY_PREFIX'] = 'auction_app_'  # Prefix for session keys

db.init_app(app)
with app.app_context():
    db.create_all()
Session(app)

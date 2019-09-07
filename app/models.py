from app import db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from app import login
from flask_login import UserMixin


# dont forget, after any change in the DB: [flask db migrate -m "users table"] puis [flask db upgrade]

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    linked_url = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    lazy_coin = db.Column(db.Integer)
    profile = db.Column(db.String(120), index=True)
    last_seen = db.Column(db.DateTime, default=datetime.utcnow)
    where_search = db.Column(db.String(40), index=True)
    spec_keyword = db.Column(db.String(140), index=True)

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


@login.user_loader
def load_user(id):
    return User.query.get(int(id))


class tickets_db(db.Model):
    key_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True)
    email = db.Column(db.String(120), index=True)
    subject = db.Column(db.String(140), index=True)
    title = db.Column(db.String(140), index=True)
    content = db.Column(db.String(400), index=True)


class logs(db.Model):
    account_key= db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True)
    date = db.Column(db.DateTime, default=datetime.utcnow)
    action = db.Column(db.String(400), index=True)

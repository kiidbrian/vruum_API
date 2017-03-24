from app.__init__ import db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from app.__init__ import login_manager

import datetime


# BASE MODEL DEFINITION
class BaseModel(db.Model):
    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, default=db.func.current_timestamp())


# USER MODEL DEFINITION
class Superuser(BaseModel):
    __tablename__ = 'superusers'

    email = db.Column(db.String(255), nullable=False, unique=True)
    password_hash = db.Column(db.String(255), nullable=False)
    fullname = db.Column(db.String(255), nullable=True)
    last_login_at = db.Column(db.DateTime, nullable=True)
    activities = db.relationship('Activity', backref='superuser', cascade='all, delete-orphan')

    @property
    def password(self):
        raise AttributeError('password is not a readable attribue')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.id

    def is_authenticated(self):
        return True


@login_manager.user_loader
def load_user(superuser_id):
    return User.query.get(int(superuser_id))


# ACTIVITY MODEL DEFINITION
class Activity(BaseModel):
    __tablename__ = 'activities'

    channel = db.Column(db.String(255), nullable=True)
    description = db.Column(db.String(255), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='CASCADE'))
    superuser_id = db.Column(db.Integer, db.ForeignKey('superusers.id', ondelete='CASCADE'))


class User(BaseModel):
    __tablename__ = 'users'

    fullname = db.Column(db.String(255), nullable=False)
    dob = db.Column(db.String(255), nullable=False)
    home_address = db.Column(db.String(255), nullable=True)
    work_address = db.Column(db.String(255), nullable=True)
    phone_number = db.Column(db.String(255), nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    occupation = db.Column(db.String(255), nullable=True)
    status = db.Column(db.String(255), nullable=True)
    last_login_at = db.Column(db.DateTime, nullable=True)
    last_logout_at = db.Column(db.DateTime, nullable=True)
    activities = db.relationship('Activity', backref='user', cascade='all, delete-orphan')

    @property
    def password(self):
        raise AttributeError('password is not a readable attribue')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    def is_anonymous(self):
        return False

    def get_id(self):
        return self.id






    

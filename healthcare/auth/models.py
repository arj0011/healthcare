from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from ..extensions import db,login_manager
# By inheriting the UserMixin we get access to a lot of built-in attributes
# which we will be able to call in our views!
# is_authenticated()
# is_active()
# is_anonymous()
# get_id()
# The user_loader decorator allows flask-login to load the current user
# and grab their id.

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(UserMixin, db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key=True)
    email = db.Column(db.String(64),unique=True)
    username = db.Column(db.String(64),unique=True)
    password_hash = db.Column(db.String(255))
    role = db.Column(db.String(20))
    is_active = db.Column(db.Boolean,nullable=True,default=True)
    doctor = db.relationship('Doctor', backref='user', uselist=False)
    #patient = db.relationship('Patient', backref='user', uselist=False)

    def __init__(self,email,username,password,role):
        self.username = username
        self.email = email
        self.password_hash = generate_password_hash(password)
        self.role = role
    
    def check_password(self,password):
        return check_password_hash(self.password_hash,password)    
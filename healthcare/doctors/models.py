from ..extensions import db

class Doctor(db.Model):
    __tablename__ = 'doctors'
    id = db.Column(db.Integer,primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    first_name = db.Column(db.String(50),nullable=False)
    last_name = db.Column(db.String(50),nullable=False)
    speciality = db.Column(db.String(50),nullable=False)        
    profile_pic = db.Column(db.String(50),nullable=False)
    email = db.Column(db.String(50),nullable=False)
    phone = db.Column(db.String(20),nullable=False)
    
    def __init__(self,user_id,first_name,last_name,speciality,profile_pic,email,phone):
        self.user_id = user_id
        self.first_name = first_name
        self.last_name = last_name
        self.speciality = speciality  
        self.profile_pic = profile_pic
        self.email = email
        self.phone = phone


class Patient(db.Model):
    __tablename__ = 'patients'
    id = db.Column(db.Integer,primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    first_name = db.Column(db.String(50),nullable=False)
    last_name = db.Column(db.String(50),nullable=False)
    email = db.Column(db.String(50),nullable=False)
    phone = db.Column(db.String(20),nullable=False)
    profile_pic = db.Column(db.String(50),nullable=False)
    
    def __init__(self,user_id,first_name,last_name,email,phone,profile_pic):
        self.user_id = user_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email  
        self.phone = phone
        self.profile_pic = profile_pic
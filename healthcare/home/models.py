from ..extensions import db

class ContactUs(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(50),nullable=False)
    email = db.Column(db.String(320),nullable=False)
    subject = db.Column(db.String(500),nullable=False)
    message = db.Column(db.Text,nullable=False)
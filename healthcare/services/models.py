from ..extensions import db

class Services(db.Model):

    __tablename__ = 'services'

    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(25),nullable=False)
    description = db.Column(db.Text,nullable=False)
    icon = db.Column(db.String(25),nullable=True)
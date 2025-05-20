from ..extensions import db

class Appointment(db.Model):
    __tablename__ = 'appointments'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(255),nullable=False)
    email = db.Column(db.String(255),nullable=False)
    phone = db.Column(db.String(15),nullable=False)
    appointment_datetime = db.Column(db.DateTime,nullable=False)
    doctor_id = db.Column(db.Integer,db.ForeignKey('doctors.id'),nullable=False)
    message = db.Column(db.Text,nullable=False)
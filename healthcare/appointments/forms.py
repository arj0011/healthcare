from flask import current_app
from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,SelectField
from wtforms.validators import DataRequired,Email
from wtforms import ValidationError
from ..doctors.models import Doctor

class AppointmentForm(FlaskForm):
    name = StringField('Name',validators=[DataRequired(message='Name required')],render_kw={"class": "form-control border-0", "placeholder": "Name","style":"height: 55px;"})   
    email = StringField('Email',validators=[DataRequired(message='Email required')],render_kw={"class":"form-control border-0","placeholder":"Your Email","style":"height: 55px;"})   
    phone = StringField('Phone',validators=[DataRequired(message='Phone required')],render_kw={"class":"form-control border-0","placeholder":"Your Mobile","style":"height: 55px;"})
    doctor = SelectField('Doctor',choices=[],validators=[DataRequired(message='Doctor required')],render_kw={"class":"form-control border-0","placeholder":"Choose Doctor","style":"height: 55px;"})
    date = StringField('Date',validators=[DataRequired(message='Date required')],render_kw={"class":"form-control border-0 datetimepicker-input","placeholder":"Choose Date","style":"height: 55px;","data-target":"#date", "data-toggle":"datetimepicker"})
    time = StringField('Time',validators=[DataRequired(message='Time required')],render_kw={"class":"form-control border-0 datetimepicker-input","placeholder":"Choose Time","style":"height: 55px;","data-target":"#time", "data-toggle":"datetimepicker"})
    message = TextAreaField('Message',validators=[DataRequired(message='Message required')],render_kw={"class":"form-control","placeholder":"Describe your problem","rows":5})  
    submit = SubmitField('Book Appointment',render_kw={"class": "btn btn-primary w-100 py-3"})


    def __init__(self, *args, **kwargs):
        super(AppointmentForm, self).__init__(*args, **kwargs)
        # Fetch doctor from the database and populate choices
        with current_app.app_context():
            doctors = Doctor.query.all()
            self.doctor.choices = [('', 'Choose Doctor')] + [(d.id, d.first_name+''+d.last_name) for d in doctors]
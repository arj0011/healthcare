from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import DataRequired,Email
from wtforms import ValidationError

class ContactForm(FlaskForm):
    name = StringField('Name',validators=[DataRequired(message='Name required')],render_kw={"class": "form-control", "placeholder": "Name"})   
    email = StringField('Email',validators=[DataRequired(message='Email required'),Email('Invalid email')],render_kw={"class":"form-control","placeholder":"Email"})   
    subject = StringField('Subject',validators=[DataRequired(message='Subject required')],render_kw={"class":"form-control","placeholder":"Subject"})
    message = TextAreaField('Message',validators=[DataRequired(message='Message required')],render_kw={"class":"form-control","placeholder":"Leave a message here"})  
    submit = SubmitField('Send Message',render_kw={"class": "btn btn-primary w-100 py-3"})
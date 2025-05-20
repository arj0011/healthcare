from flask_wtf import FlaskForm
from flask_wtf.file import FileField,FileAllowed
from wtforms import StringField,PasswordField,TextAreaField,SelectField,SubmitField
from wtforms.validators import DataRequired,Email,EqualTo
from wtforms import ValidationError
from flask_login import current_user
from .models import User

class LoginForm(FlaskForm):
    email = StringField('Email',validators=[DataRequired(message='Email is required.'),Email(message='Invalid email format.')],render_kw={"class": "form-control border-0", "placeholder": "Email"})
    password = PasswordField('Password',validators=[DataRequired(message='Password is required.')],render_kw={"class": "form-control border-0", "placeholder": "Password"})
    submit = SubmitField('Log In',render_kw={"class": "btn btn-primary w-100 py-3"})

class RegistrationForm(FlaskForm):
    role_list = ['admin','doctor','patient']
    first_name = StringField('First Name',validators=[DataRequired(message='First Name is required.')],render_kw={"class": "form-control border-0", "placeholder": "First Name"})
    last_name = StringField('Last Name',validators=[DataRequired(message='Last Name is required.')],render_kw={"class": "form-control border-0", "placeholder": "Last Name"})
    email = StringField('Email',validators=[DataRequired(message='Email is required.'),Email(message='Invalid email format.')],render_kw={"class": "form-control border-0", "placeholder": "Email"})
    phone = StringField('Phone',validators=[DataRequired(message='Phone is required.')],render_kw={"class": "form-control border-0", "placeholder": "Phone"})
    username = StringField('Username',validators=[DataRequired(message='Username is required.')],render_kw={"class": "form-control border-0", "placeholder": "Username"})
    password = PasswordField('Password',validators=[DataRequired(message='Password is required.')],render_kw={"class": "form-control border-0", "placeholder": "Password"})
    pass_confirm = PasswordField('Confirm password',validators=[DataRequired(message='Confirm Password is required.'),EqualTo('password', message='Passwords Must Match!')],render_kw={"class": "form-control border-0", "placeholder": "Confirm Password"})
    role = SelectField('Role',choices=[('','Choose Role'),('admin', 'admin'),('doctor', 'doctor'),('patient', 'patient')],validators=[DataRequired(message='Role is required.')],render_kw={"class": "form-control border-0", "placeholder": "Choose Role","style":"height:55px;"})
    submit = SubmitField('Register',render_kw={"class": "btn btn-primary w-100 py-3"})
    
    # def __init__(self, *args, **kwargs):
    #     super(RegistrationForm, self).__init__(*args, **kwargs)
    #     self.role.choices = [('','Choose Role'),('admin', 'admin'),('doctor', 'doctor'),('patient', 'patient')]
    
    def check_email(self,field):
        #check if not None for that user email
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Email already exist')
    def check_username(self, field):
        # Check if not None for that username!
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Sorry, that username is taken!')    

class UpdateUserForm(FlaskForm):
    first_name = StringField('Last Name',validators=[DataRequired(message='First Name is required.')],render_kw={"class": "form-control border-0", "placeholder": "First Name"})
    last_name = StringField('Last Name',validators=[DataRequired(message='Last Name is required.')],render_kw={"class": "form-control border-0", "placeholder": "Last Name"})
    email = StringField('Email',validators=[DataRequired(message='Email is required.'),Email(message='Invalid email format.')],render_kw={"class": "form-control border-0", "placeholder": "Email"})
    username = StringField('Username',validators=[DataRequired(message='Username is required.')],render_kw={"class": "form-control border-0", "placeholder": "Username"})
    speciality = StringField('speciality',render_kw={"class": "form-control border-0", "placeholder": "Speciality"})
    picture = FileField('Update Profile Picture',validators=[FileAllowed(['jpg','png'])])
    phone = StringField('Phone',validators=[DataRequired(message='Phone is required.')],render_kw={"class": "form-control border-0", "placeholder": "Phone"})
    submit = SubmitField('Update Profile',render_kw={"class": "btn btn-primary w-100 py-3"})

    def __init__(self, role=None, *args, **kwargs):
        super(UpdateUserForm, self).__init__(*args, **kwargs)  # ✅ Must be first
        self.role = role  # ✅ Set custom properties after init

    def validate(self,extra_validators=None):
        rv = super(UpdateUserForm, self).validate(extra_validators=extra_validators)
        if not rv:
            return False

        if self.role == 'doctor' and not self.speciality.data.strip():
            self.speciality.errors.append('Speciality is required for doctors.')
            return False

        return True

    def check_email(self,field):
        #check if not None for that user email
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Email already exist')
    def check_username(self, field):
        # Check if not None for that username!
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Sorry, that username is taken!')    
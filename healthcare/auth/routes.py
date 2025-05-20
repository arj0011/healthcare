from flask import render_template,flash,url_for,redirect,request
from flask_login import login_user,current_user,logout_user,login_required
from . import auth_bp
from .forms import LoginForm,RegistrationForm,UpdateUserForm
from .models import User
from ..doctors.models import Doctor,Patient
from ..extensions import db
from .picture_handler import add_profile_pic

@auth_bp.route('/log-in',methods=['get','post'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data.strip()).first()
        if user.check_password(form.password.data.strip()):
            login_user(user)
            return redirect(url_for('home.index')) 
        else:
            flask('Invalid email or password','danger')
            redirect(url_for('auth.login'))
    return render_template('login.html',form=form)

@auth_bp.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home.index'))
    
@auth_bp.route('/account',methods=['GET','POST'])
def account():
    if current_user.role == 'doctor':
        userdata = db.session.query(User, Doctor).join(Doctor).filter(User.role == 'doctor').first()
    else:
        userdata = db.session.query(User, Patient).join(Patient).filter(User.role == 'patient').first()
    
    user,targetuser = userdata

    if user is None:
        flash('User not found.', 'danger')
        return redirect(url_for('home.index'))

    form = UpdateUserForm(role=user.role)
    if request.method == 'GET':
        form.first_name.data = targetuser.first_name
        form.last_name.data = targetuser.last_name
        form.email.data = user.email
        form.phone.data = targetuser.phone
        form.username.data = user.username
        if user.role == 'doctor':
            form.speciality.data = targetuser.speciality
    
    if form.validate_on_submit(): 
        if form.picture.data:
            username = user.username
            pic = add_profile_pic(form.picture.data,username)
            targetuser.profile_image = pic
        
        if user.role == 'doctor':
            targetuser.speciality = form.speciality.data.strip()
        
        targetuser.first_name = form.first_name.data.strip()
        targetuser.last_name = form.last_name.data.strip()
        targetuser.email = form.email.data.strip()
        targetuser.phone = form.phone.data.strip()
        user.email = form.email.data.strip()
        user.username = form.username.data.strip()

        db.session.commit()
        flash(f' {user.role.capitalize()} account updated')
        return redirect(url_for('auth.account'))   

    return render_template('account.html',form=form)
@auth_bp.route('/register',methods=['get','post'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(
            username = form.username.data.strip(),
            email = form.email.data.strip(),
            password = form.password.data.strip(),
            role = form.role.data.strip()
        )     
        try:
            db.session.add(user)
            db.session.flush()
            if user.id:
                if user.role == 'doctor':
                    doctor = Doctor(
                        user_id = user.id,
                        first_name = form.first_name.data.strip(),
                        last_name = form.last_name.data.strip(),
                        speciality = 'default',
                        profile_pic = 'default.jpg',
                        email = form.email.data.strip(),
                        phone=form.phone.data.strip()

                    )
                    db.session.add(doctor)
                elif user.role == 'patient':
                    patient = Patient(
                        user_id = user.id,
                        first_name = form.first_name.data.strip(),
                        last_name = form.last_name.data.strip(),
                        email = form.email.data.strip(),
                        phone = form.phone.data.strip(),
                        profile_pic = 'default.jpg',
                    )
                    db.session.add(patient)
                
            db.session.commit()   
            flash('User register successfully','success')
            return redirect(url_for('auth.register')) 
        except Exception as e:
            db.session.rollback()
            flash(f'Registration failed: {str(e)}', 'danger')
    return render_template('register.html',form=form)

@auth_bp.route('/profile')
def profile():
    return render_template('account.html')    
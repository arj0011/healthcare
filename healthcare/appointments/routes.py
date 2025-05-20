from flask import render_template,flash,redirect,url_for
from . import appointments_bp
from ..doctors.models import Doctor
from ..appointments.models import Appointment
from .forms import AppointmentForm
from ..extensions import db
from datetime import datetime 

@appointments_bp.route('/',methods=['get','post'])
def index():
    form = AppointmentForm()
    if form.validate_on_submit():
        datetime_str = f'{form.date.data} {form.time.data}'
        appointment_datetime = datetime.strptime(datetime_str,'%m/%d/%Y %I:%M %p')
        appointment = Appointment(
            name = form.name.data.strip(),
            email = form.email.data.strip(),
            phone = form.phone.data.strip(),
            appointment_datetime = appointment_datetime,
            doctor_id = form.doctor.data,
            message = form.message.data.strip()
        )
        db.session.add(appointment)
        db.session.commit()
        flash('Appointment booked successsully','success')
        return redirect(url_for('appointments.index'))
    doctors = Doctor.query.all()
    return render_template('appointments.html',form=form)

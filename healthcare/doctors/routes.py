from flask import current_app,render_template
from .models import Doctor
from . import doctors_bp

@doctors_bp.route('/<int:page>')
def index(page):
    doctors = Doctor.query.paginate(page=page, per_page=4, error_out=False)
    return render_template('doctors.html', doctors=doctors.items, pagination=doctors)

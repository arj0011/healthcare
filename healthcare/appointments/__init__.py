from flask import Blueprint,render_template

appointments_bp = Blueprint('appointments',__name__,template_folder='templates')

from . import routes   
from flask import Blueprint,render_template

doctors_bp = Blueprint('doctors',__name__,template_folder='templates')

from . import routes   
from flask import Blueprint,render_template

auth_bp = Blueprint('auth',__name__,template_folder='templates')

from . import routes   
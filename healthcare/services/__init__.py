from flask import Blueprint,render_template

services_bp = Blueprint('services',__name__,template_folder='templates')

from . import routes   
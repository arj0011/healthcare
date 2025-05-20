from flask import current_app,render_template
from .models import Services
from . import services_bp

@services_bp.route('/<int:page>',methods=['get','post'])
def index(page):
    services = Services.query.paginate(page=page, per_page=int(current_app.config['PER_PAGE']), error_out=False)
    return render_template('services.html', services=services.items, pagination=services)
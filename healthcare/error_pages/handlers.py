from flask import Blueprint,render_template

error_pages = Blueprint('error_pages',__name__,template_folder='templates')

@error_pages.app_errorhandler(404)
def error_404(error):
    return render_template('404.html')

@error_pages.app_errorhandler(500)
def error_500(error):
    return render_template('500.html')
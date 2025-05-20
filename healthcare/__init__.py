import logging
from flask import Flask
from .extensions import db,mail,login_manager
from .home import home_bp
from .doctors import doctors_bp
from .services import services_bp
from .appointments import appointments_bp
from .auth import auth_bp
from .config import Config
from .auth.cli import create_superuser
from .auth.hooks import load_user_from_header
from .error_pages.handlers import error_pages

logger = logging.getLogger(__name__)
def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    db.init_app(app)
    mail.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'

    app.register_blueprint(home_bp, url_prefix="/")
    app.register_blueprint(doctors_bp, url_prefix="/doctors")
    app.register_blueprint(services_bp, url_prefix="/services")
    app.register_blueprint(appointments_bp, url_prefix="/appointments")
    app.register_blueprint(auth_bp, url_prefix="/auth")

    # Register the custom command used in cron job may be
    app.cli.add_command(create_superuser)
    
    # Register the before_request function;It is a middleware;
    # Runs in sequential order if maultiple hooks
    app.before_request(load_user_from_header)

    #Error handlers 
    app.register_blueprint(error_pages)

    #set logging
    logging.basicConfig(
        filename='app.log',
        level=logging.ERROR,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )
    return app


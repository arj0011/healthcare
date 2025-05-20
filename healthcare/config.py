from os import getenv
from dotenv import load_dotenv

load_dotenv('.env')

class Config:
    SECRET_KEY = getenv('SECRET_KEY')
    JWT_SECRET_KEY = getenv('JWT_SECRET_KEY')
    RATELIMIT_DEFAULT = getenv('RATELIMIT_DEFAULT')
    SQLALCHEMY_DATABASE_URI = getenv('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = getenv('SQLALCHEMY_TRACK_MODIFICATIONS')
    CORS_HEADERS = getenv('CORS_HEADERS')       
    PER_PAGE = getenv('PER_PAGE',3)
    MAIL_SERVER = getenv('MAIL_SERVER','smtp.gmail.com')  # or your email provider
    MAIL_PORT = getenv('MAIL_PORT',587)  # For TLS
    MAIL_USE_TLS = getenv('MAIL_USE_TLS',True)
    MAIL_USE_SSL = getenv('MAIL_USE_SSL',False)
    MAIL_USERNAME = getenv('MAIL_USERNAME','test@example.com')  # Your email
    MAIL_PASSWORD = getenv('MAIL_PASSWORD','xxxxx')  # Your email password
    MAIL_DEFAULT_SENDER = getenv('MAIL_DEFAULT_SENDER','test@example.com')
    SUPER_USERNAME = getenv('SUPER_USERNAME')
    SUPERUSER_PASSWORD = getenv('SUPERUSER_PASSWORD')
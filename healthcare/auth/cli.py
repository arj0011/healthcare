import click
from flask import current_app,g
from werkzeug.security import generate_password_hash
from flask.cli import with_appcontext
from ..extensions import db
from .models import User

''' 
    This would allow you to run the command like:
    flask create-superuser --username john_doe --email john@example.com --password secretpassword 
'''

#@click.argument('email') simple argument
@click.command('create-superuser')
@click.option('--username', prompt='Username', help='The username of the new user.')
@click.option('--email', prompt='Email', help='The email of the new user.')
@click.option('--password', prompt='Password', help='The password of the new user.')
@with_appcontext
def create_superuser(username,email,password):
    hashed_password = generate_password_hash(password)
    user = User(username=username, email=email, password_hash=hashed_password)
    db.session.add(user)
    db.session.commit()
    click.echo(f"Superuser {username} created!")
# healthcare/auth/hooks.py ;kind of middleware
from flask import g, request
from healthcare.auth.models import User
from ..extensions import db

def load_user_from_header():
    username = 'john_doe'
    if username:
        # Example: extract user based on token (your logic here)
        user = db.session.query(User).filter_by(username=username).first()
        if user:
            g.user = user
        else:
            g.user = None
    else:
        g.user = None

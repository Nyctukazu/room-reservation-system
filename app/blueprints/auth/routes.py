from flask import render_template
from app.blueprints.auth import auth_bp

@auth_bp.route('/')
def login():
    return render_template('auth/index.html')

from flask import render_template
from app.blueprints.auth import auth_bp

@auth_bp.route('/')
@auth_bp.route('/login')
def login():
    return render_template('auth/index.html')

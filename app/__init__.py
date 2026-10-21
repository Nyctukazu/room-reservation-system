import os
from flask import Flask, render_template, url_for, redirect
from config import config_by_name
from app.extensions import db, cors

def create_app(config_name=None):
    """Application factory for Flask app."""
    if config_name is None:
        config_name = os.environ.get('FLASK_ENV', 'development')

    app = Flask(__name__)
    app.config.from_object(config_by_name.get(config_name, config_by_name['default']))

    # Ensure the instance directory exists for SQLite
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # Initialize Flask extensions
    db.init_app(app)
    cors.init_app(app)

    # Register Blueprints
    from app.blueprints.auth import auth_bp
    from app.blueprints.admin import admin_bp
    from app.blueprints.faculty import faculty_bp
    from app.blueprints.student import student_bp

    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(admin_bp, url_prefix='/admin')
    app.register_blueprint(faculty_bp, url_prefix='/faculty')
    app.register_blueprint(student_bp, url_prefix='/student')

    # Register Global Error Handlers
    @app.errorhandler(404)
    def page_not_found(e):
        return redirect(url_for('auth.login')), 404
    

    @app.errorhandler(500)
    def internal_server_error(e):
        return {"error": "Internal Server Error"}, 500

    # Auto-create database tables on start (great for quick hackathon prototyping)
    with app.app_context():
        # Import models so SQLAlchemy discovers them before create_all()
        from app.models import example
        db.create_all()

    return app

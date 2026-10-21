import os
from flask import Flask, render_template
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
    from app.blueprints.main import main_bp
    from app.blueprints.api import api_bp
    from app.blueprints.auth import auth_bp

    app.register_blueprint(main_bp)
    app.register_blueprint(api_bp, url_prefix='/api')
    app.register_blueprint(auth_bp, url_prefix='/auth')

    # Register Global Error Handlers
    @app.errorhandler(404)
    def page_not_found(e):
        return render_template('404.html'), 404

    @app.errorhandler(500)
    def internal_server_error(e):
        return {"error": "Internal Server Error"}, 500

    # Auto-create database tables on start (great for quick hackathon prototyping)
    with app.app_context():
        # Import models so SQLAlchemy discovers them before create_all()
        from app.models import example
        db.create_all()

    return app

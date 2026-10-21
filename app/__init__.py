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
        try:
            # Import models so SQLAlchemy discovers them before create_all()
            from app.models import example
            db.create_all()
            uri = app.config.get('SQLALCHEMY_DATABASE_URI', '')
            db_type = 'PostgreSQL (Supabase)' if 'postgres' in uri else 'SQLite'
            print(f"[Database] Successfully connected to {db_type} and verified tables.")
        except Exception as e:
            print(f"[Database] Warning: Could not connect to database: {e}")
            print("[Database] Check your DATABASE_URL in .env if you are connecting to Supabase.")

    return app

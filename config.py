import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

def get_database_url():
    """Format and normalize the database URL for SQLAlchemy 2.0+."""
    url = os.environ.get('DATABASE_URL')
    if not url:
        # Fallback to local SQLite if DATABASE_URL is not set
        return f"sqlite:///{os.path.join(basedir, 'instance', 'dev.db')}"

    # Normalize relative SQLite paths to absolute for Windows compatibility
    if url.startswith('sqlite:///') and not url.startswith('sqlite:////'):
        rel_path = url[len('sqlite:///'):]
        if not os.path.isabs(rel_path):
            url = f"sqlite:///{os.path.join(basedir, rel_path).replace(os.sep, '/')}"

    # Supabase / cloud providers sometimes provide URLs starting with postgres://
    # SQLAlchemy requires postgresql://
    if url.startswith('postgres://'):
        url = url.replace('postgres://', 'postgresql://', 1)

    return url

class Config:
    """Base configuration."""
    SECRET_KEY = os.environ.get('SECRET_KEY', 'default-fallback-hackathon-key')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = get_database_url()
    
    # Engine options for cloud databases (Supabase, Neon, RDS, etc.)
    # pool_pre_ping ensures stale/dropped connections are transparently reconnected
    SQLALCHEMY_ENGINE_OPTIONS = {
        'pool_pre_ping': True,
        'pool_recycle': 300,
    }

class DevelopmentConfig(Config):
    """Development configuration."""
    DEBUG = True

class ProductionConfig(Config):
    """Production configuration."""
    DEBUG = False

config_by_name = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}

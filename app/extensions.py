from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

# Initialize extensions without binding to an app yet
db = SQLAlchemy()
cors = CORS()

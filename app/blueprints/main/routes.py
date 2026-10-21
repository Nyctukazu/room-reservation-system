from flask import render_template
from app.blueprints.main import main_bp
from app.models.example import Project

@main_bp.route('/')
def index():
    # Pass sample or recent items to the home template
    projects = Project.query.order_by(Project.created_at.desc()).limit(6).all()
    return render_template('index.html', title='Hackathon App', projects=projects)

@main_bp.route('/about')
def about():
    return render_template('index.html', title='About This Project', projects=[])

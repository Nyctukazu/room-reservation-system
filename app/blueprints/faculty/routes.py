from flask import render_template
from app.blueprints.faculty import faculty_bp

@faculty_bp.route('/f')
def form():
    return render_template('faculty/reservation_form.html')

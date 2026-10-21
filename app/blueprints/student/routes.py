from flask import render_template
from app.blueprints.students import student_bp

@student_bp.route('/')
def form():
    return render_template('student/reservation_form.html')


def dashboard():
    return render_template('student/dashboard.html')

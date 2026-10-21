from flask import render_template
from app.blueprints.student import student_bp

@student_bp.route('/form')
def form():
    return render_template('student/reservationForm.html')

@student_bp.route('/dashboard')
def dashboard():
    return render_template('student/studentDashboard.html')

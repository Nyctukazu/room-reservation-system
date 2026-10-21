from flask import render_template, request
from app.blueprints.student import student_bp

@student_bp.route('/form', methods=['GET', 'POST'])
def form():
    submitted_data = None
    if request.method == 'POST':
        submitted_data = {
            'student_name': request.form.get('student_name', ''),
            'student_id': request.form.get('student_id', ''),
            'email': request.form.get('email', ''),
            'section': request.form.get('section', ''),
            'room': request.form.get('room', ''),
            'date': request.form.get('date', ''),
            'start_time': request.form.get('start_time', ''),
            'end_time': request.form.get('end_time', ''),
            'purpose': request.form.get('purpose', ''),
            'activity_title': request.form.get('activity_title', ''),
            'adviser': request.form.get('adviser', ''),
            'attendees': request.form.get('attendees', ''),
            'equipment': request.form.getlist('equipment'),
            'remarks': request.form.get('remarks', '')
        }
    selected_room = request.args.get('room', '')
    return render_template('student/reservationForm.html', 
                           selected_room=selected_room, 
                           submitted_data=submitted_data)

@student_bp.route('/dashboard')
def dashboard():
    return render_template('student/studentDashboard.html')

from flask import render_template
from app.blueprints.admin import admin_bp

@admin_bp.route('/dashboard')
def dashboard():
    return render_template('admin/dashboard.html')

from flask import jsonify, request
from app.blueprints.api import api_bp
from app.extensions import db
from app.models.example import Project
from app.services.ai_service import generate_ai_response

@api_bp.route('/health', methods=['GET'])
def health():
    """Health check endpoint for judging & deployment."""
    return jsonify({
        'status': 'healthy',
        'message': 'Hackathon Flask API is active!'
    }), 200

@api_bp.route('/projects', methods=['GET'])
def get_projects():
    """Retrieve all projects/records."""
    projects = Project.query.order_by(Project.created_at.desc()).all()
    return jsonify({
        'count': len(projects),
        'projects': [p.to_dict() for p in projects]
    }), 200

@api_bp.route('/projects', methods=['POST'])
def create_project():
    """Create a new project record."""
    data = request.get_json() or {}
    
    title = data.get('title', '').strip()
    if not title:
        return jsonify({'error': 'Title is required'}), 400

    new_project = Project(
        title=title,
        description=data.get('description', '').strip(),
        author=data.get('author', 'Hacker')
    )
    db.session.add(new_project)
    db.session.commit()

    return jsonify({
        'message': 'Project created successfully',
        'project': new_project.to_dict()
    }), 201

@api_bp.route('/ai/generate', methods=['POST'])
def ai_generate():
    """Endpoint to trigger AI service functions."""
    data = request.get_json() or {}
    prompt = data.get('prompt', '').strip()

    if not prompt:
        return jsonify({'error': 'Prompt cannot be empty'}), 400

    result = generate_ai_response(prompt)
    return jsonify({
        'prompt': prompt,
        'result': result
    }), 200

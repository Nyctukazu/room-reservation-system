from flask import jsonify, request
from app.blueprints.auth import auth_bp
from app.extensions import db
from app.models.example import User

@auth_bp.route('/register', methods=['POST'])
def register():
    """Simple user registration for hackathon demo."""
    data = request.get_json() or {}
    username = data.get('username', '').strip()
    email = data.get('email', '').strip()

    if not username or not email:
        return jsonify({'error': 'Username and email are required'}), 400

    if User.query.filter((User.username == username) | (User.email == email)).first():
        return jsonify({'error': 'User with this username or email already exists'}), 409

    user = User(username=username, email=email)
    db.session.add(user)
    db.session.commit()

    return jsonify({
        'message': 'User registered successfully',
        'user': user.to_dict()
    }), 201

@auth_bp.route('/login', methods=['POST'])
def login():
    """Mock login endpoint."""
    data = request.get_json() or {}
    username = data.get('username')

    if not username:
        return jsonify({'error': 'Username is required'}), 400

    return jsonify({
        'message': f'Logged in as {username}',
        'token': 'demo-hackathon-bearer-token'
    }), 200

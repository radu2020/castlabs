import os
from flask import Blueprint, request, jsonify, Flask
from flask_cors import CORS

from .url_validator import is_valid_url
from .qr_generator import generate_qr_code

main_bp = Blueprint('main', __name__)


# This route is used to generate QR Codes
@main_bp.route('/generate', methods=['POST'])
def generate_qr():
    # Try to read request payload
    try:
        data = request.get_json()
        url = data.get('url')
    except:
        return jsonify({"error": "Invalid JSON format or missing fields."}), 400
    
    # Validate received payload
    if not is_valid_url(url):
        return jsonify({"error": "Invalid or missing URL"}), 400
    
    # Try to generate QR code
    try:
        qr_code = generate_qr_code(url)
    except:
        return jsonify({"error": "Generate QR failed."}), 500

    # Send back data
    return jsonify({"qr_code": qr_code})

# Create flask app
def create_app():
    app = Flask(__name__)
    # Add cors for requests coming from local 8080
    CORS(app, origins="http://localhost:8080")
    app.config['DEBUG'] = os.getenv('API_DEBUG', 'False') == 'True'
    app.register_blueprint(main_bp)
    return app
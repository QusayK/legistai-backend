
from .utils.scrape_pdf_links import scrape_pdf_links
from .validation import LoginForm
from flask import Blueprint, jsonify, make_response, request
from flask_jwt_extended import create_access_token
from sqlalchemy import func
from sqlalchemy.orm.exc import NoResultFound

from .models import User

main = Blueprint('main', __name__)

@main.route('/api/login', methods=['POST'])
def login():
    try:
        data = request.get_json()
        if not data:
            return jsonify({'error': 'Missing JSON data'}), 400

        form = LoginForm()
        form.email.data = data.get('email', '')
        form.password.data = data.get('password', '')

        if form.validate_on_submit():
            email = form.email.data.strip()
            password = form.password.data 
        
            user = User.query.filter(func.lower(User.email) == func.lower(email)).filter_by(password=password).one()
            access_token = create_access_token(identity=user.id)

            response = make_response({'access_token': access_token})
            response.set_cookie('access_token', access_token, secure=True, httponly=True)

            return response
        else:
            error_messages = form.errors
            return jsonify({'error': 'Invalid input', 'details': error_messages}), 400

    except NoResultFound:
        return jsonify({'message': 'Invalid email or password'}), 401
    

@main.route('/api/scrape-pdf', methods=['GET'])
def scrape_pdf():
    url = 'https://www.pdfscripting.com/public/Free-Sample-PDF-Files-with-scripts.cfm'
    pdf_paths = scrape_pdf_links(url)

    base_url = 'https://www.pdfscripting.com/public/'
    full_pdf_links = [f'{base_url}{link}' for link in pdf_paths]

    return jsonify(full_pdf_links)
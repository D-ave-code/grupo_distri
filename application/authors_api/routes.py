from . import author_api_blueprint
from .. import db
from ..models import Author
from flask import jsonify, request
from fastapi.encoders import jsonable_encoder

@author_api_blueprint.route('/authors', methods=['GET'])
def authors():
    authors = Author.query.all()
    return jsonable_encoder(authors)

@author_api_blueprint.route('/authors', methods=['POST'])
def add_authors():
    datos = request.get_json()
    first_name = datos["first_name"]
    last_name = datos["last_name"]
    author = Author()
    author.first_name =first_name
    author.last_name =last_name
    db.session.add(author)
    db.session.commit()
    response =  author.to_json()
    return response, 201

@author_api_blueprint.route('/authors/<id>', methods=['DELETE'])
def delete_author(id):
    status = 200
    try:
        a = Author.query.get(id)
        db.session.delete(a)
        db.session.commit()
    except:
        status = 204

    return ("",status)

@author_api_blueprint.route('/authors/<id>', methods=['GET'])
def get_author_id(id):
    response=""
    status = 200
    try:
         a = Author.query.get(id)
         response =  a.to_json()
    except:
        status = 204        
    
    return response, status

@author_api_blueprint.route('/authors/<id>', methods=['PUT'])
def update_authors(id):
    datos = request.get_json()
    status = 200
    try:
        a = Author.query.get(id)
        a.first_name = datos["first_name"]
        a.last_name = datos["last_name"]
        db.session.commit()
    except:
        status = 204
    return "", status

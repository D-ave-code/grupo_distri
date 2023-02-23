from . import author_api_blueprint
from .. import db
from ..models import Author
from flask import jsonify, request

@author_api_blueprint.route('/api/authors', methods=['GET'])
def authors():
    authors = []
    for row in Author.query.all():
        authors.append(row.to_json())

    response = jsonify({'results' : authors})
    return response


@author_api_blueprint.route('/api/authors', methods=['POST'])
def add_authors():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    author = Author()
    author.first_name =first_name
    author.last_name =last_name
    db.session.add(author)
    db.session.commit()
    response = jsonify({'message' : "author agregado", 'author': author.to_json()})
    return response
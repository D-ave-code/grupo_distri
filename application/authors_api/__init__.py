from flask import Blueprint
author_api_blueprint = Blueprint('authors_api', __name__)

from . import routes
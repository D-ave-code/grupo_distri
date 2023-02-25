from flask import Blueprint
from flask_swagger_ui import get_swaggerui_blueprint
author_api_blueprint = Blueprint('authors_api', __name__)

SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'
SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(
        SWAGGER_URL,
        API_URL,
        config={
         'app_name': "application"
        }
    )

from . import routes
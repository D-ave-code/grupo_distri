import config
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from .models import Author

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    enviroment_configuration = os.environ['CONFIGURATION_SETUP']

    app.config.from_object(enviroment_configuration)

    db.init_app(app)
    migrate = Migrate(app, db)
    
    with app.app_context():
        from .authors_api import author_api_blueprint
        from flask_migrate import upgrade
        
        upgrade()
        app.register_blueprint(author_api_blueprint)
        return app
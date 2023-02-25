import config
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_openapi3 import Info, Tag
from flask_openapi3 import OpenAPI
from flask import Blueprint

db = SQLAlchemy()

def create_app():   

    app = Flask(__name__)
          
    enviroment_configuration = os.environ['CONFIGURATION_SETUP']

    app.config.from_object(enviroment_configuration)

    db.init_app(app)
    migrate = Migrate(app, db)
   
    with app.app_context():
        from .authors_api import author_api_blueprint, SWAGGERUI_BLUEPRINT
        from flask_migrate import upgrade
        from sqlalchemy import text
        
        upgrade()
        stmt = text("INSERT INTO authors (first_name, last_name) SELECT * FROM (VALUES ('nombre1', 'ape1'), ('nombre2', 'ape2'),('nombre3', 'ape3'),('nombre4', 'ape4')) AS temp WHERE NOT EXISTS (SELECT id FROM authors LIMIT 1);")
        db.session.execute(stmt)
        db.session.commit()
        app.register_blueprint(author_api_blueprint)
        app.register_blueprint(SWAGGERUI_BLUEPRINT)
        

        
        return app
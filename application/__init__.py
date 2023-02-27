import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from yoyo import read_migrations, get_backend

db = SQLAlchemy()

def create_app():   

    app = Flask(__name__)
          
    enviroment_configuration = os.environ['CONFIGURATION_SETUP']

    app.config.from_object(enviroment_configuration)
    
    db.init_app(app)
    
    yoyoback = get_backend(f"postgresql://{os.environ['DB_USERNAME']}:{os.environ['DB_PASSWORD']}@{os.environ['DB_HOST']}:{os.environ['DB_PORT']}/{os.environ['DB_NAME']}")       
    migrations_folder = "migraciones"
    migrations = read_migrations(migrations_folder)

    if migrations:
        with yoyoback.lock():
            yoyoback.apply_migrations(yoyoback.to_apply(migrations))
            print("Migraciones realizadas")
    with app.app_context():
        from .authors_api import author_api_blueprint, SWAGGERUI_BLUEPRINT
        app.register_blueprint(author_api_blueprint)
        app.register_blueprint(SWAGGERUI_BLUEPRINT)
        return app
from dotenv import load_dotenv
import dotenv
import os
from decouple import config
dotenv_file_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(dotenv_file_path):
    load_dotenv(dotenv_file_path)

class Config:
    SQLACHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(Config):
    ENV = "development"

    try:
        SQLALCHEMY_DATABASE_URI=os.environ['SQLALCHEMY_DATABASE_URI']
    except:
        SQLALCHEMY_DATABASE_URI="postgresql://postgres:postgres@localhost:5432/grupod"
        
class ProductionConfig(Config):
    pass
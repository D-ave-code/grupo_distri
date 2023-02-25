from application import create_app, db
from application import models
from flask_migrate import Migrate

app = create_app()

if __name__ == '__main__':
    app.run()
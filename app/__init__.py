from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# init SQLAlchemy so we can use it later in our models
app = Flask(__name__)
db_path = 'D:\hackthediff-verycreative\instance\project.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+db_path
db = SQLAlchemy(app) # db intitialized here
#db.init_app(app)

def create_app():

    from . import models

    with app.app_context():
        db.create_all()

    # blueprint for auth routes in our app
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    # blueprint for non-auth parts of app
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
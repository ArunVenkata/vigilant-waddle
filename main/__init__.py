from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os


# init
current_app = Flask(__name__)
current_app.config.from_object("main.settings")
# db = SQLAlchemy(current_app)
engine = create_engine(os.environ.get('DB_URI'), pool_size=5)

def get_session():
    session = sessionmaker(bind=engine)
    return session()

from main.app import mainapp

current_app.register_blueprint(mainapp)

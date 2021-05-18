import os


ENV = os.environ.get("FLASK_ENV", "development")
DEBUG = bool(os.environ.get("FLASK_DEBUG", True))

SQLALCHEMY_TRACK_MODIFICATIONS = False

SECRET_KEY = os.environ.get("SECRET_KEY")

APPS_FOLDER = "apps"